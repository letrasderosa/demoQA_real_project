from pages.base_page import Base_Page


def test_open(browser):
    page = Base_Page(browser, 'https://demoqa.com/text-box')
    page.open()
    # page.delete_all_cookies()
    # page.get_cookie()
    # page.set_cookie()




