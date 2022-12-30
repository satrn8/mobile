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


def test_id_books():
    with allure.step("Тест добавления в корзину книг по ID и заполнение формы заказа"):
        skip_start_screen(browser)
        browser.element((AppiumBy.ID, 'ru.labirint.android:id/toolbar_search_et')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/toolbar_search_et')).type("848208")
        browser.driver.execute_script("mobile: performEditorAction",  {'action': 'search'})
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/card_product_bottom_panel_btn')).click()

        #  закрыть страницу после добавления
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/activity_card_product_close_ib')).click()

        #  вернуться на шаг назад
        browser.element((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')).click()

        browser.element((AppiumBy.ID, 'ru.labirint.android:id/toolbar_search_et')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/toolbar_search_et')).type("838271")
        browser.driver.execute_script("mobile: performEditorAction", {'action': 'search'})
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/card_product_bottom_panel_btn')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/card_product_bottom_panel_btn')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android:id/basket_bottom_panel_btn')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/order_temp_region_btn')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/region_input_et')).type("Зеленоград")
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RadioButton')).click()
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RadioButton')).click()
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="список"]')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/exw_list_search_et')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/exw_list_search_et')).type("1508")
        browser.driver.execute_script("mobile: performEditorAction", {'action': 'search'})
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/exw_item_rb')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/order_temp_phone_et')).type("9998555611")

        browser.driver.swipe(720, 683, 720, 100, 400)
        browser.driver.swipe(720, 683, 720, 100, 400)
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/order_temp_email_et')).type("verypyc@test.ru")
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/order_temp_name_text_input_layout')).type("Алёна")
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/order_temp_surname_text_input_layout')).type("Иванова")