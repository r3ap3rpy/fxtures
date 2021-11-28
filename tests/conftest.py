from selenium import webdriver
from pytest import fixture
from time import sleep
@fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    yield browser
    sleep(10)
    print("Well this was all, cleaning up!")