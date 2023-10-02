from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# desired capabilities

desired_cap = {
    "platformName": "Android",
    "appium:platformVersion": "11.0",
    "appium:deviceName": "MRDIZPVWPB45SO69",
    "appium:app": "C:\\Users\\IDN MEDIA\\Documents\\APK Testing\\Android\\automation\\app-beta (12).apk",
    "automationName": "UiAutomator2",
    "appium:ignoreHiddenApiPolicyError": "true",
    "appium:appWaitActivity": "*",
    "appium:appPackage": "com.idntimes.idntimes",
    "newCommandTimeout": "60",
    "noReset": "true"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.ID, "com.idntimes.idntimes:id/action_profile").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Yuk, daftar']").click()

# Fill in the form

driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@bounds='[72,908][1008,1082]']").send_keys("abc@gmail.com")
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@bounds='[72,1100][1008,1274]']").send_keys("Nanakoot umami")
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@bounds='[72,1292][1008,1466]']").send_keys("Welcome@2022")
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@bounds='[72,1484][1008,1658]']").send_keys("Welcome@2022")
driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Daftar']").click()


