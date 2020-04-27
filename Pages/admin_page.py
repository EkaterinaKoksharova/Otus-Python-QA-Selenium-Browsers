""" Локаторы и методы страницы логина администратора сайта opencart """

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminPage(BasePage):
    """ Локаторы и методы страницы логина администратора сайта opencart """

    admin_login_url = "http://localhost:8080/opencart/admin/"

    login = "admin"
    password = "admin"

    login_panel = (By.CSS_SELECTOR, '.panel-default')
    name_input = (By.CSS_SELECTOR, '#input-username')
    password_input = (By.CSS_SELECTOR, '#input-password')
    submit_button = (By.CSS_SELECTOR, 'button.btn')
    forgotten_password_link = (By.CSS_SELECTOR, '.help-block')
    error_message = (By.CSS_SELECTOR, '.alert-dismissible')

    logout_button = (By.CLASS_NAME, 'fa-sign-out')

<<<<<<< Updated upstream
    menu_catalogue = (By.CSS_SELECTOR, '#menu-catalog')
=======
    menu_catalogue = (By.LINK_TEXT, 'Catalog')
>>>>>>> Stashed changes
    menu_products = (By.CSS_SELECTOR, '#collapse1 > :nth-child(2)')

    alert_danger = (By.CLASS_NAME, 'alert-danger')

<<<<<<< Updated upstream
    @staticmethod
    def go_to_admin_login_page(browser):
        """ Метод перехода на страницу admin login администраторской части opencart """

        browser.get(AdminPage.admin_login_url)

    @staticmethod
    def login_to_admin(browser, login=admin_login, password=admin_password):
        """ Авторизация в админской части магазина opencart """

        browser.find_element(*AdminPage.name_input).send_keys(login)
        browser.find_element(*AdminPage.password_input).send_keys(password)

        browser.find_element(*AdminPage.submit_button).click()

    @staticmethod
    def logout_from_admin(browser):
        """ Выход из аккаунта в админской части магазина opencart """

        browser.find_element(*AdminPage.logout_button).click()
=======
    def go_to_admin_login_page(self):
        """ Метод перехода на страницу admin login администраторской части opencart """

        self.browser.get(self.admin_login_url)

    def login_to_admin(self, login=login, password=password):
        """ Авторизация в админской части магазина opencart """

        self.browser.find_element(*self.name_input).send_keys(login)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.submit_button).click()

    def logout_from_admin(self):
        """ Выход из аккаунта в админской части магазина opencart """

        self.browser.find_element(*self.logout_button).click()
>>>>>>> Stashed changes
