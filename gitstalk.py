import requests
import sys

class GithubUser:
    def __init__(self, username):
        self.username = username
        self.userUrl = "https://api.github.com/users/{0}".format(username)
        self.repos = []
        self.identities = []

    def checkUsername(self): # Checks if user exists
        r = requests.get(self.userUrl)
        return r.status_code == 200

    def grabRepos(self): # Grab all repos from a user
        if (self.checkUsername()):
            r = requests.get(f"{self.userUrl}/repos?per_page=100")
            if(r.status_code == 200):
                self.repos = r.json()
                return True
        return False

    def showRepos(self):
        for repo in self.repos:
            print("> " + repo['full_name'])

    def stalkRepo(self, repo): # Grab all names and emails from a repo
        commits_url = repo['commits_url'].replace('{/sha}', '')
        r = requests.get(commits_url)
        if(r.status_code == 200):
            commits = r.json()
            for commit in commits:
                committer = commit['commit']['committer']
                temp = committer['name'] + "|" + committer['email']
                if(temp not in self.identities):
                    self.identities.append(temp)
            return True
        return False

    def stalkRepos(self): # Grab all usefull info from all repos
        for repo in self.repos:
            if(not self.stalkRepo(repo)):
                print("<!> Undumped: " + repo['full_name'])
            else:
                print("<+> Dumped: " + repo['full_name'])

def main():
    if(len(sys.argv) >= 2):
        for i in range(1,len(sys.argv)):
            gitUser = GithubUser(sys.argv[i])
            if(not gitUser.checkUsername()):
                print("Not a valid user named {0}".format(gitUser.username))
                continue
            else:
                print('--- {0} ---'.format(gitUser.username))
            if(gitUser.grabRepos()):
                print("REPOS LIST")
                gitUser.showRepos()
                print("REPOS DUMP")
                gitUser.stalkRepos()
                print("REPOS NAMES AND MAILS")
                for identity in gitUser.identities:
                    print(identity)
    else:
        print("USAGE: python3 gitstalk.py <USERNAME_1 ... USERNAME_N>")
    
if __name__ == "__main__":
    main()
