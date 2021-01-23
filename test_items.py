link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_basket(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    assert browser.find_elements_by_css_selector(".btn-add-to-basket"), "Button is not found"
