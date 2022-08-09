from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_right_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "Incorrect product price in basket"

    def should_be_right_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Incorrect product name in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_dissapeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message should have disappeared, but should not be"

