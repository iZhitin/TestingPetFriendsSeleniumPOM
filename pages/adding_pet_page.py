# точка означает нахождение в одной директории
from .base_page import BasePage
from .my_pets_page import MyPetsPage
from .locators import AddPetLocators

# для визуального контроля
import time


class AddingPetPage(BasePage):
    """Класс, наследующий общий функционал работы со страницей, инициализирует элементы страницы и
    методы работы с ними. Предназначен для страницы добавления питомца"""
    def __init__(self, driver, timeout=10):
        # наследуем функционал, передав параметры
        super().__init__(driver, timeout)
        self.driver = driver
        # открываем страницу
        url = "https://petfriends.skillfactory.ru/my_pets"
        driver.get(url)
        # нажимаем на кнопку 'добавить питомца', чтобы выйти на страницу
        my_pets_page = MyPetsPage(driver)
        my_pets_page.add_animal.click()
        # инициализируем элементы, найденные по локаторам
        # заголовок
        self.adding_title = driver.find_element(*AddPetLocators.ADDING_TITLE)
        # внесение данных
        self.add_photo = driver.find_element(*AddPetLocators.ADD_PHOTO)
        self.name_field = driver.find_element(*AddPetLocators.NAME_FIELD)
        self.animal_type_field = driver.find_element(*AddPetLocators.ANIMAL_TYPE_FIELD)
        self.age_field = driver.find_element(*AddPetLocators.AGE_FIELD)
        # кнопки
        self.close_cross = driver.find_element(*AddPetLocators.CLOSE_CROSS)
        self.close_btn = driver.find_element(*AddPetLocators.CLOSE_BTN)
        self.submit_btn = driver.find_element(*AddPetLocators.SUBMIT_BTN)
        time.sleep(3)

    # функция добавляет переданное фото
    def add_photo_send(self, value):
        self.add_photo.send_keys(value)

    # функция вводит переданное имя
    def name_field_send(self, value):
        self.name_field.send_keys(value)

    # функция вводит переданный тип
    def animal_type_field_send(self, value):
        self.animal_type_field.send_keys(value)

    # функция вводит переданный возраст
    def age_field_send(self, value):
        self.age_field.send_keys(value)

    # функция нажимает на крестик для выхода
    def close_cross_click(self):
        self.close_cross.click()

    # функция нажимает на кнопку "отмена" для выхода
    def close_btn_click(self):
        self.close_btn.click()

    # функция нажимает на кнопку "добавить" для публикации животного
    def submit_btn_click(self):
        self.submit_btn.click()
