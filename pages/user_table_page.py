from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class UserTablePage(BasePage):
    ADD_USER_BTN = (By.XPATH, "//button[@type='add']")
    FIRST_NAME_INPUT = (By.NAME, "FirstName")
    LAST_NAME_INPUT = (By.NAME, "LastName")
    USERNAME_INPUT = (By.NAME, "UserName")
    PASSWORD_INPUT = (By.NAME, "Password")
    CUSTOMER_RADIO = {
        'Company AAA': (By.XPATH, "//input[@value='15']"),
        'Company BBB': (By.XPATH, "//input[@value='16']")
    }
    ROLE_DROPDOWN = (By.NAME, "RoleId")
    EMAIL_INPUT = (By.NAME, "Email")
    PHONE_INPUT = (By.NAME, "Mobilephone")
    SAVE_BTN = (By.CSS_SELECTOR, ".btn.btn-success")

    def validate_page(self):
        assert "angularjs-protractor/webtables" in self.driver.current_url

    def add_user(self, user_data):
        self.click(self.ADD_USER_BTN)
        #self.wait.until(EC.visibility_of_element_located(self.MODAL))

        self.enter_text(self.FIRST_NAME_INPUT, user_data["First Name"])
        self.enter_text(self.LAST_NAME_INPUT, user_data["Last Name"])
        self.enter_text(self.USERNAME_INPUT, user_data["Username"])
        self.enter_text(self.PASSWORD_INPUT, user_data["Password"])
        self.click(self.CUSTOMER_RADIO[user_data["Customer"]])
        self.get_element(self.ROLE_DROPDOWN).send_keys(user_data["Role"])
        self.enter_text(self.EMAIL_INPUT, user_data["Email"])
        self.enter_text(self.PHONE_INPUT, user_data["Cell Phone"])
        self.click(self.SAVE_BTN)