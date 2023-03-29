from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pageObjects.JacketsPage import JacketPage


class HomePage:
    def __init__(self, driver, act, wait):
        self.driver = driver
        self.act = act
        self.wait = wait

    #self.act.click(self.driver.find_element(By.CSS_SELECTOR, "a[id='ui-id-19']")).perform()
    action1 = (By.CSS_SELECTOR, "a[id='ui-id-5']")
    wait1 = (By.CSS_SELECTOR, "a[id='ui-id-17']")
    action2 = (By.CSS_SELECTOR, "a[id='ui-id-17']")
    wait2 = (By.CSS_SELECTOR, "a[id='ui-id-19']")
    action3 = (By.CSS_SELECTOR, "a[id='ui-id-19']")


    def getAction1(self):
        return self.act.move_to_element(self.driver.find_element(*HomePage.action1))

    def getWait1(self):
        return self.wait.until(expected_conditions.visibility_of_element_located((HomePage.wait1)))

    def getAction2(self):
        return self.act.move_to_element(self.driver.find_element(*HomePage.action2))

    def getWait2(self):
        return self.wait.until(expected_conditions.visibility_of_element_located((HomePage.wait2)))

    def getAction3(self):
        self.act.click(self.driver.find_element(*HomePage.action3)).perform()
        jacketPage = JacketPage(self.driver, self.act, self.wait)
        return jacketPage