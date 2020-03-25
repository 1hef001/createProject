import platform
import subprocess
import sys
import os
from createRepo import createRepo

# print(platform.platform())

def execCmd(cmd):
    try:
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return result
    
    except Exception:
        return 'Could not execute function'

    
def getPath():
    
    '''
        Sets path automatically if path is not assigned by the user
    '''
    if 'Windows' in platform.platform():
        try:
            result = execCmd('whoami')
            user = result.stdout.readline().decode('utf-8').split('\\')[1].strip()
            PATH = 'C:/Users/' + user + '/Documents/'
            with open('path.txt', 'r') as f:
                PATH = f.readline()
                f.close()
            print('main')
            
        except AttributeError:
            print(result)
        
        except FileNotFoundError:
            try:
                os.chdir(PATH)
                os.mkdir('Workspace')
                PATH = PATH + 'Workspace'
                # print('FilenotFOund')
        
            except FileExistsError:
                PATH = PATH + 'Workspace'
                # print('FileExistsError')
        
        finally:
            # print('finally')
            return PATH

    else:
        try:
            result = execCmd('whoami')
            user = result.stdout.readline().decode('utf-8').strip()
            PATH = user + '/Documents/'
            with open('path.txt', 'r') as f:
                PATH = f.readline()
                f.close()
        
        except AttributeError:
            print(result)
        
        except FileNotFoundError:
            try:
                os.chdir(PATH)
                os.mkdir('Workspace')
                PATH = PATH + 'Workspace'
                # print('FilenotFOund')
        
            except FileExistsError:
                PATH = PATH + 'Workspace'
                # print('FileExistsError')
        
        finally:
            return PATH


def createFolder(name):

    '''
        Creates the said folder in said directory
    '''
    try:
        # print(os.getcwd())
        create = execCmd(['mkdir', name])
        out = create.stdout.readline().decode('utf-8').strip()
        if 'cannot create dir' in out:
            raise ZeroDivisionError

    except Exception:
        out = 'Folder exists. Try another name.'

    finally:
        return out

def gitInit():
    try:
        result = execCmd(['git', 'init'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)

def gitAdd():
    try:
        os.system('echo > README.md')
        result = execCmd(['git', 'add', '.'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)


def gitCommit():
    try:
        result = execCmd(['git', 'commit', '-m', '\"initial commit\"'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)

def gitPush():
    try:
        result = execCmd(['git', 'push', '-u', 'origin', 'master'])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)

def gitRemote(url):
    try:
        result = execCmd(['git', 'remote', 'add', 'origin', url])
        out = result.stdout.readline().decode('utf-8').strip()
        print(out)

    except AttributeError:
        print(result)


def openCode():
    try:
        '''didn't work with subprocess. need to figure out why and reduce the no. of imports'''
        # result = execCmd(['code', '.'])
        # out = result.stdout.readline().decode('utf-8').strip()
        # print(out)
        os.system('code .')

    except Exception:
        pass


if __name__ == "__main__":
    # print(sys.argv[1])
    os.chdir(getPath())
    # print(os.getcwd())
    # print('path')
    name = sys.argv[-1]
    createFolder(name)
    # print('folder')
    os.chdir(name)
    # print('dir change')
    gitInit() 
    # print('git init')
    gitAdd()
    # print('git add')
    gitCommit()
    # print('git commit')
    gitLink = createRepo(name)
    # print('git link')
    gitRemote(gitLink)
    # print('git remote')
    gitPush()
    # print('git push')
    # print(name)
    openCode()
    