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

Clone the repository from git and use as is.
Doesn't support installations yet. But, will soon. Wait for it.


**Usage:**
```
py essentials.py <project_name>
```

**For Example:**
```
py essentials.py testrepo
```

**Specifying path:**
```
py essentials.py PATH=<path> <repo-name>
```

***Note: there should be no space between 'PATH' '=' and 'given-path'. Otherwise this case fails***
```
py essentials.py PATH=C:/Users/<user>/MyProjects test-repo
```
