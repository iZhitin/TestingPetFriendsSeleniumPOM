#!/usr/bin/python3
# -*- encoding=utf8 -*-
# This is example shows how we can manage failed tests
# and make screenshots after any failed test case.
# import allure

# для тестирования
import pytest
# для присвоения id
import uuid

# фикситуры из данного файла работают во всех тестах директории (conftest.py - специальный модуль)


# параметры браузера во время теста
@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    return chrome_options


# ???
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Фикстура передает информацию об упавших тестах в teardown"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):
    """Фикстура настраивает размер окна браузера и, в случае падения тестов,
    делает скриншот и выводит логи"""
    # setUp
    browser = selenium
    browser.set_window_size(1400, 1000)
    # исполнение
    yield browser
    # tearDown (код ниже исполняется после каждого теста)
    # если тест падает: ???
    if request.node.rep_call.failed:
        # попытка сделать скриншот
        try:
            # при помощи js-скрипта обеляем бэкграунд
            browser.execute_script("document.body.bgColor = 'white';")
            # сохранение скриншота с уникальным id в папку screenshots
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
            # информация для успешной отладки
            print('URL: ', browser.current_url)
            print('Browser logs:')
            # почему 'browser' в качестве аргумента ???
            for log in browser.get_log('browser'):
                print(log)
        # пример отличного антипаттерна
        except:
            pass


def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
