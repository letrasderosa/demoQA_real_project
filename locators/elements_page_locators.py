from  selenium.webdriver.common.by import By
from data.person_data import PersonData
from generator.generator import generated_person

class TextBoxPage_Locators(PersonData):
    personData = PersonData()
    # form_fields
    # FULL_NAME = (By.CSS_SELECTOR, "input[@id='userName']")
    # CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[@id='currentAddress']")
    # SUBMIT = (By.CSS_SELECTOR, "button[@id='submit']")

    # created form
    # CREATED_FULL_NAME = (By.CSS_SELECTOR, "p[@id='name']")
    # CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR,
    #                            "p[@id='currentAddress']") # или так: (By.CSS_SELECTOR, "p#currentAddress")

    # можно так сделать
    FULL_NAME = (By.CSS_SELECTOR, "input#userName")
    EMAIL = (By.CSS_SELECTOR, "input#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea#permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "button#submit")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
    CREATED_OUTPUT = (By.CSS_SELECTOR, "#output")

    # Это были пробные данные из моего файла person_data.py, сгенерированные через Faker
    # FULL_NAME_VALUE = personData.fname
    # EMAIL_VALUE = personData.femail
    # CURRENT_ADDRESS_VALUE = personData.faddress
    # PERMANENT_ADDRESS_VALUE = personData.faddress2
    # data_to_send = [FULL_NAME_VALUE, EMAIL_VALUE, CURRENT_ADDRESS_VALUE, PERMANENT_ADDRESS_VALUE]

    # А это локаторы из generator.py, как было в курсе
    person_info = next(generated_person())
    FULL_NAME_VALUE = person_info.fullname
    EMAIL_VALUE = person_info.email
    CURRENT_ADDRESS_VALUE = person_info.current_address
    PERMANENT_ADDRESS_VALUE = person_info.permanent_address
    data_to_send = [FULL_NAME_VALUE, EMAIL_VALUE, CURRENT_ADDRESS_VALUE, PERMANENT_ADDRESS_VALUE]