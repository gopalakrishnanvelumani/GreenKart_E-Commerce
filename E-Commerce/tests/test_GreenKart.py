import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.OrderPage import OrderPage
from pageObjects.SearchPage import searchPage
from test_data.GreenKart_data import testData
from utilities.BaseClass import BaseClass


class Test_greenKart(BaseClass):

    def test_greenKart(self, setup, getData):
        veg = searchPage(self.driver)
        veg.getSearch().send_keys(getData["search"])
        time.sleep(2)
        results = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        for result in results:
            result.find_element(By.XPATH, "div/button").click()
        veg.getCart().click()
        veg.getCheckOut().click()

        order = OrderPage(self.driver)
        order.getPromoCode().send_keys(getData["coupon"])
        order.getApply().click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

        order.getPlaceOrder().click()

        country = Select(self.driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select"))
        country.select_by_visible_text(getData["country"])

        order.getAgree().click()
        order.getProceed().click()
        print("Vegetables order placed successfully")


    @pytest.fixture(params=testData.data)
    def getData(self, request):
        return request.param

