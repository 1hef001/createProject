# import os

from cred import username, password

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as sexep


def createRepo(repository_name):
    # PATH = os.path.join(path, r'/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=r'C:/Webdrivers/chromedriver.exe')

    driver.get('https://github.com/login')
    driver.implicitly_wait(50)

    # with open('cred.txt', 'r') as f:
    #     credentials = f.readlines()
    #     username = credentials[0].strip()
    #     password = credentials[1].strip()
    #     f.close()

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
    driver.implicitly_wait(50)
    submit = driver.find_elements_by_xpath('//*[@id="new_repository"]/div[3]/button')[0]
    submit.submit()

    driver.implicitly_wait(50)
    git = driver.find_element_by_id('empty-setup-clone-url')
    gitURL = git.get_attribute('value')
    
    driver.quit()

    return gitURL
