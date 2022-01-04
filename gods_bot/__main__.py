import logging
import pyautogui
import time


logging.basicConfig(level=logging.INFO, format='gods_bot %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')


def main():
    # TODO
    while True:
        logging.info('gods_bot')
        time.sleep(5)


if __name__ == '__main__':
    main()