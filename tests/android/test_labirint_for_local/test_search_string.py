import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser


def skip_start_screen(browser):
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="ImageView"]')).click()


def test_find():
    with allure.step("Тест поиска на странице"):
        skip_start_screen(browser)
        browser.element((AppiumBy.ID, 'ru.labirint.android:id/toolbar_search_et')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/toolbar_search_et')).type("блокнот")
        browser.driver.execute_script("mobile: performEditorAction",  {'action': 'search'})

