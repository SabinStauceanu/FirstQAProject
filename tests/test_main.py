import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from pageObjects.JacketsPage import JacketPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_main(self):
        log = self.getLogger()
        log.info("Start of the Program")
        homePage = HomePage(self.driver,self.act, self.wait)
        homePage.getAction1().perform()
        homePage.getWait1()
        homePage.getAction2().perform()
        homePage.getWait2()
        jacketPage = homePage.getAction3()
        log.info("Home Page test has Passed")

        jacketPage.getSize().click()
        jacketPage.getColor().click()
        jacketPage.getAction1().perform()
        jacketPage.getWait1()
        jacketPage.getAction2().perform()
        time.sleep(6)
        jacketPage.getShowcart().click()
        jacketPage.getWait2()
        jacketPage.getAction3().perform()
        log.info("Jacket Page test has Passed")
