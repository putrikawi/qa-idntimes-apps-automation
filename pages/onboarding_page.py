from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from webdriver import DesiredCapabilities

#modulename fiturename_page
#classname CamelCase
#methodname run_fiturename
#variablename buttonname
#commit & push git Fitur : deskripsi
#commit , pull ,check, push


class OnboardingPage:
    def __init__(self):
        self.desired_caps = DesiredCapabilities().to_dict()
        self.driver = None


    def start_driver(self): # start driver in local
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)


    ''' def is_app_open(self):
            try:    
                current_package = self.driver.current_package
                current_activity = self.driver.current_activity

                return (
                        current_package == "com.idntimes.idntimes" and
                        current_activity == "com.idntimes.idntimes.ui.splash.SplashActivity"
                )
            except Exception:
                return False
'''

    def run_onboarding(self):

        try:
            self.driver.implicitly_wait(10)
            skip_button_element = self.driver.find_element(AppiumBy.ID, value="com.idntimes.idntimes.overview:id/btnSkip")
            skip_button_element.click()
            self.driver.implicitly_wait(10)
            nantisaja_button_element = self.driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes.overview:id/tvLater")
            nantisaja_button_element.click()


            # com.idntimes.idntimes.overview:id/btnSkip if skip
            #com.idntimes.idntimes.overview:id/btnNext

            print("Passed, clicking onboarding")
        except NoSuchElementException as e:
            print("Error clicking onboarding:", e)



# initiate driver
ob = OnboardingPage()

# start the driver
ob.start_driver()

# call the onboarding method
ob.run_onboarding()

