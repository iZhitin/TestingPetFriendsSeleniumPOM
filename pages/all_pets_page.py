# точка означает нахождение в одной директории
from .base_page import BasePage
from .locators import AllPetsLocators

# для визуального контроля
import time


class AllPetsPage(BasePage):
    """Класс, наследующий общий функционал работы со страницей, инициализирует элементы страницы и
    методы работы с ними. Предназначен для главной страницы со всеми животными"""
    def __init__(self, driver, timeout=10):
        # наследуем функционал, передав параметры
        super().__init__(driver, timeout)
        self.driver = driver
        # открываем страницу
        url = "https://petfriends.skillfactory.ru/all_pets"
        driver.get(url)
        # инициализируем элементы, найденные по локаторам
        # шапка сайта
        self.logo_header = driver.find_element(*AllPetsLocators.LOGO_HEADER)
        self.my_pets = driver.find_element(*AllPetsLocators.MY_PETS)
        self.all_pets = driver.find_element(*AllPetsLocators.ALL_PETS)
        self.log_out = driver.find_element(*AllPetsLocators.LOG_OUT)
        # тело сайта
        self.center_title = driver.find_element(*AllPetsLocators.CENTER_TITLE)
        self.description = driver.find_element(*AllPetsLocators.DESCRIPTION)
        self.animal_cards = driver.find_element(*AllPetsLocators.ANIMAL_CARDS)
        self.animal_photos = driver.find_element(*AllPetsLocators.ANIMAL_PHOTOS)
        self.animal_names = driver.find_element(*AllPetsLocators.ANIMAL_PHOTOS)
        self.animal_types_and_ages = driver.find_element(*AllPetsLocators.ANIMAL_TYPES_AND_AGES)
        time.sleep(3)

    # клик на лого в хэдере
    def logo_header_click(self):
        self.logo_header.click()

    # клик на вкладку "мои питомцы"
    def my_pets_click(self):
        self.my_pets.click()

    # клик на вкладку "все питомцы"
    def all_pets_click(self):
        self.all_pets.click()

    # клик на кнопку "выйти"
    def log_out_click(self):
        self.log_out.click()

