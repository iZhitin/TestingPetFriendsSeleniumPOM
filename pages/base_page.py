# для парсинга параметров пути
from urllib.parse import urlparse


class BasePage(object):
    """Класс, предоставляющий общий функционал, для работы со страницей. Но не с
    элементами страницы"""

    # конструктор класса - специальный метод с ключевым словом __init__ (по факту, конструктор __new__,
    # а это - инициализатор нового объекта класса)

    # при создании экземпляра класса в него передаются
    # объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        # добавим неявное ожидание
        self.driver.implicitly_wait(timeout)

    # функция выводит параметры пути URL, например: /search_results
    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path


