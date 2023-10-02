from appium.webdriver.common.appiumby import AppiumBy #import module
from selenium.common.exceptions import NoSuchElementException
from onboarding_page import OnboardingPage
from webdriver import DesiredCapabilities

class Login:
    def __init__(self):
        self.desired_caps = DesiredCapabilities().to_dict()
        self.driver = None

class login:
    #Class CamelCase
    # Create an instance of onboarding1
    ob =OnboardingPage ()

    # Start the driver for onboarding1
    ob.start_driver()

    # Call the cardonboarding method of onboarding1
    ob.run_onboarding()

    def login_with_google(self): #method login google
        try:

            self.driver.implicitly_wait(10)
            lg1 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/cl_tooltip")
            lg1.click()


            lg2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile")
            lg2.click()
            self.driver.implicitly_wait(10)

            lg3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="google logo Masuk dengan Google")
            lg3.click()
            self.driver.implicitly_wait(20)# This ensures that the driver waits for up to 10 seconds (as specified) for the element to appear on the page before performing the click action

            lg4 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/cl_tooltip")
            lg4.click()
            self.driver.implicitly_wait(10)

            lg5 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/btnFilledRight")
            lg5.click()

            lg6 = self.driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            lg6.click()

            lg7 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivSettings")
            lg7.click()

            lg8 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLogout")
            lg8.click()
            self.driver.implicitly_wait(10)

            print("Passed, logging in with Google") # Log sukses kalo seluruh diatas berhasil
        except NoSuchElementException as e:
            print("Error, logging in with Google:", e)  # Log gagal kalo seluruh diatas berhasil

    def login_with_facebook(self):
        try:
            el5 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/action_profile")
            el5.click()
            self.driver.implicitly_wait(10)
            el6 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="facebook logo Masuk dengan Facebook")
            el6.click()
            el7 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Lanjut']")
            el7.click()
            self.driver.implicitly_wait(10)
            el8 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivSettings")
            el8.click()
            self.driver.implicitly_wait(10)
            el9 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLogout")
            el9.click()
            self.driver.implicitly_wait(10)

            print("Passed, logging in with Facebook")
        except NoSuchElementException as e:
            print("Error, logging in with Facebook:", e)

    def login_with_email(self):
            try:


                el10 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/action_profile")
                el10.click()
                self.driver.implicitly_wait(10)
                el11 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@password='false']")
                el11.send_keys("qaidnapp4@gmail.com")
                el12 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@password='true']")
                el12.send_keys("Idntimes1234!")
                el13 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Masuk']")
                el13.click()
                self.driver.implicitly_wait(10)
                el14 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivSettings")
                el14.click()
                self.driver.implicitly_wait(10)
                el15 = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLogout")
                el15.click()
                self.driver.implicitly_wait(10)

                print("Passed, logging in with Email")
            except NoSuchElementException as e:
                print("Error, logging in with Email:", e)

                self.driver.close_app()
                self.driver.quit()


# create an instance of Profile
# initiate driver
l = login()

# start the driver
l.start_driver()
# call the login_with_google method
l.login_with_google()

# call the login_with_facebook method
#l.login_with_facebook()

# call the login_with_email method
#l.login_with_email()

#test