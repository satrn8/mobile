import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from mobile_tests.model import app
browser.config.timeout = 100


def skip_start_screen(browser):
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    time.sleep(2)
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    time.sleep(2)
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="ImageView"]')).click()
    time.sleep(2)


# @allure.tag('mobile_tests')
# @allure.title('Search')
# def test_find():
#     skip_start_screen(browser)
#     browser.element((AppiumBy.ID, 'ru.labirint.android:id/toolbar_search_et')).type("блокнот")
#     time.sleep(2)
#     browser.driver.execute_script("mobile: performEditorAction",  {'action': 'search'})
#     time.sleep(5)
#     browser.config.timeout = 100
    # add_video(browser)


# @allure.tag('mobile_tests')
# @allure.title('Test search')
# def test_click_office():
#     skip_start_screen(browser)
#     browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TextView')).click()
#     browser.config.timeout = 20
#     browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Канцтовары"]/android.widget.TextView')).click()
#     browser.config.timeout = 20
    # add_video(browser)


def test_id_books():
    skip_start_screen(browser)
    browser.element((AppiumBy.ID, 'ru.labirint.android:id/toolbar_search_et')).click()
    time.sleep(2)
    browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/toolbar_search_et')).type("848208")
    time.sleep(2)
    browser.driver.execute_script("mobile: performEditorAction",  {'action': 'search'})
    time.sleep(5)
    browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/card_product_bottom_panel_btn')).click()
    time.sleep(2)

    #  закрыть страницу после добавления
    browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/activity_card_product_close_ib')).click()
    time.sleep(2)

    #  вернуться на шаг назад
    browser.element((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
    time.sleep(5)
    browser.element((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
    time.sleep(5)


    browser.element((AppiumBy.ID, 'ru.labirint.android:id/toolbar_search_et')).click()
    time.sleep(2)
    browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/toolbar_search_et')).type("838271")
    time.sleep(2)
    browser.driver.execute_script("mobile: performEditorAction", {'action': 'search'})
    time.sleep(5)
    browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/card_product_bottom_panel_btn')).click()
    time.sleep(5)
    browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/card_product_bottom_panel_btn')).click()
    time.sleep(5)
    browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RadioButton')).click()
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/order_temp_phone_et')).type("89998555611")
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/order_temp_email_et')).type("test@test.ru")
    browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.EditText')).type("Алёна")



