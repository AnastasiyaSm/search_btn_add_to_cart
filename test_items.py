import time


def test_search_btn_add_to_cart(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert len(browser.find_elements_by_css_selector(".btn-primary")) > 0
    "Нет кнопки добавления в корзину"
