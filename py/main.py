if __name__ == '__main__':
    from appium import webdriver
    from webdriver import DesiredCapabilities
    from pages.onboarding_page import OnboardingPage
    from pages.login_page import LoginPage

    desired_caps = DesiredCapabilities().to_dict()
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    try:
        onboarding_page = OnboardingPage(driver)
        login_page = LoginPage(driver)

        onboarding_page.run_onboarding()
        login_page.run_login_with_google()
        login_page.run_login_with_facebook()
        login_page.run_login_with_email()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
