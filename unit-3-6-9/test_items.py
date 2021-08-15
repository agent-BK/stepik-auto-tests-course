import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_css_selector("#add_to_basket_form button[type=submit]")
    assert len(button), "The add to cart button was not found on the page"
