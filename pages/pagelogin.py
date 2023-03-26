from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from webdriver import PLATFORM_NAME, PLATFORM_VERSION, DEVICE_NAME, AUTOMATION_NAME, APP_PACKAGE, APP_ACTIVITY
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains


class login:
    def __init__(self):
        self.desired_caps = {
            "platformName": PLATFORM_NAME,
            "platformVersion": PLATFORM_VERSION,
            "deviceName": DEVICE_NAME,
            "automationName": AUTOMATION_NAME,
            "appPackage": APP_PACKAGE,
            "appActivity": APP_ACTIVITY
        }
        self.driver = None


    def start_driver(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def login_with_google(self):
        try:
            el1 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/action_profile")
            el1.click()
            self.driver.implicitly_wait(10)
            el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="google logo Masuk dengan Google")
            el2.click()
            self.driver.implicitly_wait(15)
            el3 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivSettings")
            el3.click()
            self.driver.implicitly_wait(10)
            el4 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLogout")
            el4.click()
            self.driver.implicitly_wait(10)

            print("Passed, logging in with Google")
        except NoSuchElementException as e:
            print("Error, logging in with Google:", e)

    def login_with_facebook(self):
        try:
            el5 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/action_profile")
            el5.click()
            self.driver.implicitly_wait(10)
            el6 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="facebook logo Masuk dengan Facebook")
            el6.click()
            el7 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Lanjut']")
            el7.click()
            self.driver.implicitly_wait(15)
            el9 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivSettings")
            el9.click()
            self.driver.implicitly_wait(10)
            el10 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLogout")
            el10.click()
            self.driver.implicitly_wait(10)

            print("Passed, logging in with Facebook")
        except NoSuchElementException as e:
            print("Error, logging in with Facebook:", e)

    def login_with_email(self):
            try:
                el11 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/action_profile")
                el11.click()
                self.driver.implicitly_wait(10)
                el12 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@password='false']")
                el12.send_keys("qaidnapp4@gmail.com")
                el13 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@password='true']")
                el13.send_keys("Idntimes1234!")
                el14 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Masuk']")
                el14.click()
                self.driver.implicitly_wait(10)
                el15 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivSettings")
                el15.click()
                self.driver.implicitly_wait(10)
                el16 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLogout")
                el16.click()
                self.driver.implicitly_wait(10)

                print("Passed, logging in with Email")
            except NoSuchElementException as e:
                print("Error, logging in with Email:", e)

                self.driver.close_app()
                self.driver.quit()


# create an instance of Profile
l = login()

# start the driver
l.start_driver()

# call the login_with_google method
l.login_with_google()

# call the login_with_facebook method
l.login_with_facebook()

# call the login_with_email method
l.login_with_email()

#test