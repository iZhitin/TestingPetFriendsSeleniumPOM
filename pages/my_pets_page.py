from pages.base_page import BasePage
from pages.locators import MyPetsLocators

# для визуального контроля
import time


class MyPetsPage(BasePage):
    """Класс, наследующий общий функционал работы со страницей, инициализирует элементы страницы и
    методы работы с ними. Предназначен для страницы с животными пользователя"""
    def __init__(self, driver, timeout=10):
        # наследуем функционал, передав параметры
        super().__init__(driver, timeout)
        self.driver = driver
        # открываем страницу
        url = "https://petfriends.skillfactory.ru/my_pets"
        driver.get(url)
        # инициализируем элементы, найденные по локаторам
        # шапка сайта
        self.logo_header = driver.find_element(*MyPetsLocators.LOGO_HEADER)
        self.my_pets = driver.find_element(*MyPetsLocators.MY_PETS)
        self.all_pets = driver.find_element(*MyPetsLocators.ALL_PETS)
        self.log_out = driver.find_element(*MyPetsLocators.LOG_OUT)
        # тело сайта
        #  меню
        self.nickname = driver.find_element(*MyPetsLocators.NICKNAME)
        self.info_board = driver.find_element(*MyPetsLocators.INFO_BOARD)
        #  таблица
        self.photo_column_title = driver.find_element(*MyPetsLocators.PHOTO_COLUMN_TITLE)
        self.name_column_title = driver.find_element(*MyPetsLocators.NAME_COLUMN_TITLE)
        self.type_column_title = driver.find_element(*MyPetsLocators.TYPE_COLUMN_TITLE)
        self.age_column_title = driver.find_element(*MyPetsLocators.AGE_COLUMN_TITLE)
        #   строчки с данными о животных
        self.animal_blocks = driver.find_element(*MyPetsLocators.ANIMAL_BLOCKS)
        #   данные животных
        self.animal_photos = driver.find_element(*MyPetsLocators.ANIMAL_PHOTOS)
        self.animal_names = driver.find_element(*MyPetsLocators.ANIMAL_NAMES)
        self.animal_types = driver.find_element(*MyPetsLocators.ANIMAL_TYPES)
        self.animal_ages = driver.find_element(*MyPetsLocators.ANIMAL_AGES)
        #   кнопка добавления животного
        self.add_animal = driver.find_element(*MyPetsLocators.ADD_ANIMAL)
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
