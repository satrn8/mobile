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


def test_school():
    with allure.step("Тест фильтрации"):
        skip_start_screen(browser)
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/main_catalog_tab_btn')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Школа"]')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android:id/filter_tv')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/exams_expandable_linear_layout')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/school_filter_ege_check')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android:id/ok_btn')).click()