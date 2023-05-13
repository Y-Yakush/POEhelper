import logging
import sys

from pynput import keyboard
from script import active_elements_search
from exceptions import ExitException

logging.basicConfig(stream=sys.stdout, level=logging.ERROR, format='%(message)s')


def script_work():
    print('Поиск активных элементов начался ...')
    active_elements_search()
    print('Поиск завершен. Нажмите <ctrl>+<alt>+y, чтобы проверить скрин еще раз '
          'или <ctrl>+e для выхода из программы')


def script_exit():
    raise ExitException


def hello_message():
    print('Привет, POEhelper поможет тебе посчитать выделенные карты в твоем хранилище '
          'и пришлет сообщение с их количеством. \n'
          'Для этого сделай скрин хранилища 25х25 или 10х10 и нажми сочетание клавиш <ctrl>+<alt>+y. \n'
          'Программа сама считает картинку из буфера обмена и посчитает количество выделенных рамкой карт.')


def wait_for_hotkey():
    with keyboard.GlobalHotKeys({'<ctrl>+<alt>+y': script_work,
                                 '<ctrl>+e': script_exit}) as start_script:
        start_script.join()


def main():
    try:
        hello_message()
        wait_for_hotkey()
    except Exception as e:
        logging.error('Ошибка: %s', e)


if __name__ == '__main__':
    main()
