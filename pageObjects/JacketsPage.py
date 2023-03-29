from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class JacketPage:
    def __init__(self, driver, act, wait):
        self.driver = driver
        self.act = act
        self.wait = wait


    size = (By.XPATH,"//li[7]//div[@option-id='169']")
    color = (By.XPATH,"//li[7]//div[@option-id='52']")
    action1 = (By.XPATH, "//li[7]")
    wait1 = (By.XPATH, "//li[7]//button[@type='submit']")
    action2 = (By.XPATH, "//li[7]//button[@type='submit']")
    showcart = (By.CSS_SELECTOR, ".showcart")
    wait2 = (By.ID, "top-cart-btn-checkout")
    action3 = (By.ID, "top-cart-btn-checkout")

    def getSize(self):
        return self.driver.find_element(*JacketPage.size)

    def getColor(self):
        return self.driver.find_element(*JacketPage.color)

    def getAction1(self):
        return self.act.move_to_element(self.driver.find_element(*JacketPage.action1))

    def getWait1(self):
        return self.wait.until(expected_conditions.visibility_of_element_located((JacketPage.wait1)))

    def getAction2(self):
        return self.act.click(self.driver.find_element(*JacketPage.action2))

    def getShowcart(self):
        return self.driver.find_element(*JacketPage.showcart)

    def getWait2(self):
        return self.wait.until(expected_conditions.visibility_of_element_located((JacketPage.wait2)))

    def getAction3(self):
        return self.act.click(self.driver.find_element(*JacketPage.action3))

