from selenium.webdriver.common.by import By


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    promoCode = (By.CSS_SELECTOR, ".promoCode")
    apply = (By.CSS_SELECTOR, ".promoBtn")
    placeOrder = (By.XPATH, "//button[text()='Place Order']")
    agree = (By.CLASS_NAME, "chkAgree")
    proceed = (By.XPATH, "//button[text()='Proceed']")
    country = (By.XPATH, "//div[@class='wrapperTwo']//div//select")


    def getPromoCode(self):
        return self.driver.find_element(*OrderPage.promoCode)

    def getApply(self):
        return self.driver.find_element(*OrderPage.apply)

    def getPlaceOrder(self):
        return self.driver.find_element(*OrderPage.placeOrder)

    def getAgree(self):
        return self.driver.find_element(*OrderPage.agree)

    def getProceed(self):
        return self.driver.find_element(*OrderPage.proceed)

    def getCountry(self):
        return self.driver.find_element(*OrderPage.country)
