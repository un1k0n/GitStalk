# GITSTALK
GitStalk is a tool developed to grab all names and email from a github user.

## How it works
This tool uses the public version of the github api to grab all repos from users and inspect each one looking for info in commits. That means that it wont only grab info from the specified used, it will also grab info for all collaborators.

## Comming Soon
- Filters
- Grab more usefull info
- And more and more

## Instalation and use
```
git clone https://github.com/un1k0n/GitStalk.git
cd GitStalk
python3 gitstalk.py $USERNAME_1 ... $USERNAME_N
```

## License
As of October 17, 2019 GitStalk is licensed under http://www.gnu.org/licenses/gpl-3.0.html
