import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser


def skip_start_screen(browser):
    browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).click()
    time.sleep(10)
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="ImageView"]')).click()


def test_click_office():
    with allure.step("Тест открытия раздела"):
        skip_start_screen(browser)
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/main_catalog_tab_btn')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Канцтовары"]')).click()
