from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from py.webdriver import DesiredCapabilities
from appium import webdriver


class LoginPage:
    def __init__(self):
        self.desired_caps = DesiredCapabilities().to_dict()
        self.driver = None

    def start_driver(self):  # Start the driver in local
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)


    def run_login_with_google(self):  # Method to login with Google
        try:
            self.driver.implicitly_wait(10)
            skip_button_element = self.driver.find_element(AppiumBy.ID, value="com.idntimes.idntimes.overview:id/btnSkip")
            skip_button_element.click()

            nantisaja_button_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes.overview:id/tvLater")
            nantisaja_button_element.click()

            self.driver.implicitly_wait(10)

            tooltip_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/cl_tooltip")
            tooltip_element.click()

            self.driver.implicitly_wait(60)


            left_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/btnOutlinedLeft")
            left_element.click()


            profile_element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile")
            profile_element.click()


            google_login_element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="google logo Masuk dengan Google")
            google_login_element.click()

            close_tooltip_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/cl_tooltip")
            close_tooltip_element.click()


            settings_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivSettings")
            settings_element.click()

            logout_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLogout")
            logout_element.click()

            print("Passed, logging in with Google")  # Log success if all the steps above succeed
        except NoSuchElementException as e:
            print("Error, logging in with Google:", e)  # Log failure if any exception occurs


    def run_login_with_facebook(self):
        try:

            self.driver.implicitly_wait(60)
            fb_profile_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/action_profile")
            fb_profile_element.click()


            fb_facebook_login_element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="facebook logo Masuk dengan Facebook")
            fb_facebook_login_element.click()

            fb_continue_element = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Lanjut']")
            fb_continue_element.click()


            fb_settings_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivSettings")
            fb_settings_element.click()


            fb_logout_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLogout")
            fb_logout_element.click()


            print("Passed, logging in with Facebook")
        except NoSuchElementException as e:
            print("Error, logging in with Facebook:", e)


    def run_login_with_email(self):
        try:
            self.driver.implicitly_wait(60)

            email_profile_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/action_profile")
            email_profile_element.click()


            email_user_element = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@password='false']")
            email_user_element.send_keys("qaidnapp4@gmail.com")

            email_password_element = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@password='true']")
            email_password_element.send_keys("Idntimes1234!")

            email_button_masuk_element = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Masuk']")
            email_button_masuk_element.click()


            email_settings_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivSettings")
            email_settings_element.click()


            email_logout_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLogout")
            email_logout_element.click()


            print("Passed, logging in with Email")
        except NoSuchElementException as e:
            print("Error, logging in with Email:", e)

            self.driver.close_app()
            self.driver.quit()

l = LoginPage()

# Start the driver
l.start_driver()
# Call the login_with_google method
l.run_login_with_google()

# Call the login_with_facebook method
l.run_login_with_facebook()

# Call the login_with_email method
l.run_login_with_email()

