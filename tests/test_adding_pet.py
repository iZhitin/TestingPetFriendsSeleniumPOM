from pages.auth_page import AuthPage
from pages.adding_pet_page import AddingPetPage

# для визуального контроля
import time

# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_adding_pet.py


# тестирование добавления животного с фото
def test_adding_of_pet_with_photo(selenium):
    # авторизация
    page = AuthPage(selenium)
    page.enter_email("p@p.p")
    page.enter_password("122333")
    page.click_btn()

    # создаем объект класса страницы со всеми животными пользователя
    p = AddingPetPage(selenium)
    # вводим данные
    p.add_photo_send(
        r"C:\Users\IvanZ\YandexDisk\IT\python_work\AUTOMATION\toGitHub\TestingPetFriendsSeleniumPOM\images\IMG_2569.jpg")
    p.name_field_send('Альфа')
    p.animal_type_field_send('Собака')
    p.age_field_send('5')
    # для показательных целей
    time.sleep(3)
    # отправляем данные
    p.submit_btn_click()
    # переходим к списку своих животных
    p.driver.get('https://petfriends.skillfactory.ru/my_pets')
    # странно, но при публикации кличка собаки получила два пробела - в начале и в конце
    assert p.driver.find_element_by_xpath('//*[text()=" Альфа "]'), "Добавленного животного на странице - нет"
