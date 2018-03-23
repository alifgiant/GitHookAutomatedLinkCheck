# Git Hook - Automated Link Check
Automated recursive link checker triggered by git hooks. Written in Python3.

This tools will automatically:
1. __run on push__ to production (branch master) or uat (branch develop) environtment except you include flag __[AUTO-CHECK-SKIP]__ on your last commit to push, and
2. __run on commit__ if you put flag __[AUTO-CHECK]__ on your commit message and

## Requirements
This tools require
1. Bash
2. Python3 >= 3.6.3
	> To verify, open up your terminal and execute __python3__. If it fails, make sure python3 is added to your environtment path
	
	> For __windows__ user, sometimes python3 installation not showed up as __python3.exe__, all you need to do is:
	
	``` 
	1. Go to your installation directory
	2. Copy and paste python.exe
	3. rename the copied file as python3.exe
	```

## Quick Start
### Setup
1. Clone or download this Repo
2. Copy folder __/WebChecker__ to your project folder
3. Copy folder __/hooks__ to your project folder __/.git__
4. Specify your project URL in __/WebChecker/config.ini__

### Config
Edit file __/WebChecker/config.ini__ to match your configuration need

- __URL__ -> what is your local project url
- __OUT_DIR__ -> where to store automated checker python file object dump
- __LOG_DIR__ -> where to store automated checker .cvs output
- __RUN_ON_COMMIT__ -> flag to run on commit
- __SKIP_ON_PUSH__ -> flag to skip run on push
- __PRODUCTION__ -> branch name for production environtment
- __UAT__ -> branch name for uat environment


### Non hook start
Open up your terminal and execute main.py
```bash
~\WebChecker> python3 main.py
```

## Third party depedencies
You don't need to install these dependency manually, they are either already included or will be installed on first run.
1. PyLinkValidator, This tools is using python library from [here](https://github.com/helloproclub/pylinkvalidator) which forked from [here](https://github.com/bartdag/pylinkvalidator). This tools didn't use the library from pypi since it's not up to date yet.
2. beautifulsoup4 4.6.0, python package
	```bash
	python3 -m pip install beautifulsoup4
	```