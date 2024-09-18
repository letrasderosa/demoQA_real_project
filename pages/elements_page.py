from locators.elements_page_locators import TextBoxPage_Locators
from pages.base_page import Base_Page
import pandas as pd
import time


class TextBoxPage(Base_Page):
    '''
    Elements page methods
    '''
    locators = TextBoxPage_Locators()

    def fill_all_fields(self):
        self.is_element_visible(locator=self.locators.FULL_NAME).send_keys(self.locators.FULL_NAME_VALUE)
        self.is_element_visible(locator=self.locators.EMAIL).send_keys(self.locators.EMAIL_VALUE)
        self.is_element_visible(locator=self.locators.CURRENT_ADDRESS).send_keys(self.locators.CURRENT_ADDRESS_VALUE)
        self.is_element_visible(locator=self.locators.PERMANENT_ADDRESS).send_keys(self.locators.PERMANENT_ADDRESS_VALUE)
        self.data_to_send = self.locators.data_to_send
        self.is_element_visible(locator=self.locators.SUBMIT).click()

        return self.data_to_send
        # time.sleep(4)

    def save_filled_data(self):
        """
        Сохраняем данные в файл, чтобы позже сравнить с возвращенными данными.
        """
        with open('person.txt', 'w', encoding='windows-1251') as file:
            [file.write(f"{item}\n") for item  in self.locators.data_to_send]

    def check_filled_form(self):
        """
        Проверяем, что форма заполнена верно.
        """
        output = self.is_element_present(self.locators.CREATED_OUTPUT).text
        output_lst = [el.split(':')[1] for el in output.split('\n')]

        # По-отдельности не работает
        # full_name = self.is_element_present(self.locators.CREATED_FULL_NAME).text
        # email = self.is_element_present(self.locators.CREATED_EMAIL).text
        # current_address = self.is_element_present(self.locators.CREATED_CURRENT_ADDRESS).text
        # permanent_address = self.is_element_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        # return full_name, email, current_address, permanent_address

        with open('person.txt', 'a') as file:
            # file.write(f"{output}\n")
            [file.write(f"{item}\n") for item in output_lst]

        return output_lst



