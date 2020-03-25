import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as sexep


def createRepo(repository_name):
    # PATH = os.path.join(path, r'/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=r'C:/Webdrivers')

    driver.get('https://github.com/login')
    driver.implicitly_wait(50)

    with open('cred.txt', 'r') as f:
        credentials = f.readlines()
        username = credentials[0]
        password = credentials[1]
        f.close()

    assert 'GitHub' in driver.title

    uField = driver.find_element_by_id('login_field')
    pField = driver.find_element_by_id('password')

    uField.clear()
    pField.clear()

    uField.send_keys(username)
    pField.send_keys(password)
    pField.send_keys(Keys.RETURN)

    driver.get('https://github.com/new')


    repo = driver.find_element_by_id('repository_name')

    repo.clear()

    repo.send_keys(repository_name)
    repo.send_keys(Keys.RETURN)

    gitURL = driver.current_url + '.git'
    
    driver.quit()

    return gitURL
