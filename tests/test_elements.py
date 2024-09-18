import time
from pages.elements_page import TextBoxPage


class Test_Elements:
    class Test_TextBox:

        def test_text_box(self, browser):
            text_box_page = TextBoxPage(browser, 'https://demoqa.com/text-box')
            text_box_page.open()
            # text_box_page.fill_all_fields()
            # text_box_page.save_filled_data()

            full_name, email, cur_addr, per_addr = text_box_page.fill_all_fields() # вводные
            output_name, output_email, output_cur_addr, output_per_addr= text_box_page.check_filled_form() # возвращенные
            assert full_name == output_name, 'The full name does not match'
            assert email == output_email, 'The email does not match'
            assert cur_addr == output_cur_addr, 'The current address does not match'
            assert per_addr == output_per_addr, 'The permanent address does not match'

            # Можно сократить и сравнивать не поэлементно, а сразу - но по-отдельности понятнее,
            # где ошибка, если она есть
            # assert text_box_page.fill_all_fields() == text_box_page.check_filled_form()




