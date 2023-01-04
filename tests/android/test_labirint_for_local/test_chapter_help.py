import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser


def skip_start_screen(browser):
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="ImageView"]')).click()


def test_shipping_and_payment():
    with allure.step("Тест раздела помощи"):
        skip_start_screen(browser)
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/main_mylab_tab_btn')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/info_view')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/info_button_payment')).click()
        browser.driver.swipe(720, 683, 720, 100, 400)
        browser.driver.swipe(720, 683, 720, 100, 400)
        browser.element((AppiumBy.ID, "txtwordsadv")).click("оплата qr")
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View[2]/android.widget.Button')).click()
