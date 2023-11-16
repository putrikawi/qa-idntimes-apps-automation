from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

desire_caps = {}
desire_caps['platformName'] = 'Android'
desire_caps['deviceName'] = 'emulator-5554'
desire_caps['automationName'] = 'UiAutomator2'
desire_caps['appPackage'] ='com.idntimes.idntimes'
desire_caps['appActivity'] = 'com.idntimes.idntimes.ui.main.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile").click()
driver.implicitly_wait(10)

#Testcase Logout & Login Gmail
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="google logo Masuk dengan Google")
el1.click()
time.sleep(4)
el2 = driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/action_edit")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/fab_create_write")
el3.click()
el4 = driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlTopic")
el4.click()
el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")
el5.click()
el6 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.webkit.WebView[1]/android.webkit.WebView/android.view.View/android.widget.EditText")
el6.send_keys("Judul Test Regresi")
el7 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.widget.EditText")
el7.send_keys("Cuplikan Test Regresi")
el8 = driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/rlLine")
el8.click()
el9 = driver.find_element(by=AppiumBy.ID, value="com.idntimes.idntimes:id/ivItemGallery")
el9.click()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(473, 2149)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(514, 339)
actions.w3c_actions.pointer_action.release()
actions.perform()



driver.quit()