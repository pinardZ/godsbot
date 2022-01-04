from main import dao
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')


def main():
    """Run the timing task program. Will reset all accounts status."""

    logging.info('Timing Task. Will reset all accounts status.')
    dao.reset_accounts()


if __name__ == '__main__':
    main()
