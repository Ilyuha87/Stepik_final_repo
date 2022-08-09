from .locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email_field.send_keys(email)
        password1.send_keys(password)
        password2.send_keys(password)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link incorrect"

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Missing email input field in login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Missing password input field in login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Missing email input field in login form"
        assert True

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_EMAIL), "Missing email input field in registration form"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD1), "Missing password input field in registration form"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD2), "Missing confirm password input field in registration form"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_BUTTON), "Missing email input field in registration form"