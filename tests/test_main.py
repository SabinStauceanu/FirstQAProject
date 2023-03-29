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

        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "input[id='customer-email']").send_keys("stauceanus@gmail.com")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Stauceanu")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Sabin")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("No Company")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='street[0]']").send_keys("Home")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='street[1]']").send_keys("Sweet")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='street[2]']").send_keys("Home")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Botosani")
        sel2 = Select(self.driver.find_element(By.CSS_SELECTOR, "select[name='country_id']"))
        sel2.select_by_visible_text("Romania")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='postcode']").send_keys("717101")
        time.sleep(1)
        sel1 = Select(self.driver.find_element(By.CSS_SELECTOR, "select[name='region_id']"))
        sel1.select_by_index(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='telephone']").send_keys("0756671715")
        radioButtons = self.driver.find_element(By.XPATH, "//input[@type='radio']")
        self.driver.find_element(By.CSS_SELECTOR, ".continue").click()
