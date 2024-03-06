from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class searchPage:

    def __init__(self, driver):
        self.driver = driver


    searchBox = (By.CLASS_NAME, "search-keyword")
    cart = (By.CSS_SELECTOR, "img[alt='Cart']")
    checkOut = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")


    def getSearch(self):
        return self.driver.find_element(*searchPage.searchBox)

    def getCart(self):
        return self.driver.find_element(*searchPage.cart)

    def getCheckOut(self):
        return self.driver.find_element(*searchPage.checkOut)

