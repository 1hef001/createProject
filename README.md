# createProject

## Sweat no more with creation of new projects

A simple effort towards automating git repo creation under the same name as the project folder with an empty README.md

## Before you execute the script:

Update your github credentials in cred.py


**Requirements :**

    1. Python

    2. Selenium
    
    3. Chromedriver

## Create folder as said in createRepo or update path of the same to chromedriver

**Installing createProject**

Install using the given command after cloning, make sure to update the cred.py in the createProject folder before installing

```
python setup.py install
```


**Usage:**
```
createProject <project_name>
```

**For Example:**
```
createProject testrepo
```

**Specifying path:**
```
createProject PATH=<path> <repo-name>
```

***Note: there should be no space between 'PATH' '=' and 'given-path'. Otherwise this case fails***
```
createProject PATH=C:/Users/<user>/MyProjects test-repo
```
