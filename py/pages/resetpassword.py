from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# desired capabilities

desired_cap = {
    "platformName": "Android",
   # "appium:platformVersion": "11.0",
    "appium:deviceName": "Android Emulator",
    "appium:app": "C:\\Users\\IDN MEDIA\\Documents\\APK Testing\\Android\\automation\\app-beta (12).apk",
   "automationName": "UiAutomator2",
   # "appium:ignoreHiddenApiPolicyError": "true",
    "appium:appWaitActivity": "*",
    "appium:appPackage": "com.idntimes.idntimes",
    "newCommandTimeout": "100",
   #"noReset": "true"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.ID, "com.idntimes.idntimes:id/action_profile").click()
driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Atur ulang password']").click()

# Fill the lupa password form
driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.widget.EditText").send_keys("tamiramedina048@gmail.com")
driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Lanjutkan']").click()

# Fill ubah password form
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Isi Form...']").send_keys("123456")
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@bounds='[72,1046][1008,1220]']").send_keys("Welcome@2019")
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@bounds='[72,1238][1008,1412]']").send_keys("Welcome@2019")
#driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Ubah Password']").click()


