import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
browser.config.timeout = 100


def skip_start_screen(browser):
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    time.sleep(2)
    browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/fragment_main_auth_skip')).click()
    time.sleep(2)
    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="ImageView"]')).click()
    time.sleep(2)


def test_id_books():
    with allure.step("Тест добавления в корзину книг по ID и заполнение формы заказа"):
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

        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.EditText')).click()
        time.sleep(2)
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/toolbar_search_et')).type("838271")
        time.sleep(2)
        browser.driver.execute_script("mobile: performEditorAction", {'action': 'search'})
        time.sleep(5)
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/card_product_bottom_panel_btn')).click()
        time.sleep(5)
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/card_product_bottom_panel_btn')).click()
        time.sleep(5)

        browser.element((AppiumBy.ID, 'ru.labirint.android:id/basket_bottom_panel_btn')).click()
        time.sleep(10)
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RadioButton')).click()
        time.sleep(10)
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="список"]')).click()
        time.sleep(10)
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/exw_list_search_et')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/exw_list_search_et')).type("1508")
        time.sleep(10)
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/exw_item_rb')).click()
        time.sleep(10)


        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/order_temp_phone_et')).type("9998555611")
        time.sleep(10)
        # browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText')).type("verypyc@test.ru")
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/order_temp_email_et')).type("verypyc@test.ru")
        time.sleep(5)
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.EditText')).type("Алёна")
        time.sleep(5)
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.EditText')).type("Иванова")


def test_find():
    with allure.step("Тест поиска на странице"):
        skip_start_screen(browser)
        browser.element((AppiumBy.ID, 'ru.labirint.android:id/toolbar_search_et')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/toolbar_search_et')).type("блокнот")
        time.sleep(20)
        browser.driver.execute_script("mobile: performEditorAction",  {'action': 'search'})
        time.sleep(10)


def test_click_office():
    with allure.step("Тест открытия раздела"):
        skip_start_screen(browser)
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TextView')).click()
        browser.config.timeout = 20
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Канцтовары"]/android.widget.TextView')).click()
        browser.config.timeout = 20


def test_school():
    with allure.step("Тест фильтрации по диапазону цены"):
        skip_start_screen(browser)
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TextView')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Школа"]/android.widget.TextView')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android:id/filter_tv')).click()
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout')).click()
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.CheckBox')).click()
        browser.element((AppiumBy.ID, 'ru.labirint.android:id/ok_btn')).click()


def test_shipping_and_payment():
    with allure.step("Тест раздела помощи"):
        skip_start_screen(browser)
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.TextView')).click()
        time.sleep(5)
        browser.element((AppiumBy.ID, 'ru.labirint.android.installed_feature_main:id/info_view')).click()
        time.sleep(5)
        browser.element((AppiumBy.ID, 'ru.labirint.android.otherfeatures:id/info_button_payment')).click()
        time.sleep(10)
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[9]/android.view.View[2]/android.widget.EditText')).type("оплата qr")
        time.sleep(10)
        browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[9]/android.view.View[2]/android.widget.Button')).click()
