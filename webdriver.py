# webdriver.py

class DesiredCapabilities:
    def __init__(self):
        self.platform_name = "Android"
        self.platform_version = "13"
        self.device_name = "emulator-5554"
        self.automation_name = "UiAutomator2"
        self.app_package = "com.idntimes.idntimes"
        self.app_activity = "com.idntimes.idntimes.ui.splash.SplashActivity"
        self.new_command_timeout = 300

    def to_dict(self):
        return {
            "platformName": self.platform_name,
            "platformVersion": self.platform_version,
            "deviceName": self.device_name,
            "automationName": self.automation_name,
            "appPackage": self.app_package,
            "appActivity": self.app_activity,
            "newCommandTimeout": self.new_command_timeout
        }
