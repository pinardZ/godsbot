import logging


def main():
    logging.log("任务开始")
    while True:
        account = replace_account()
        login_vpn()
        start_game()
        play_game(account)
        end_game()
        logout_vpn()


def replace_account() -> int:
    return 0


def login_vpn():
    pass


def logout_vpn():
    pass


def start_game():
    pass


def end_game():
    pass


def play_game(account: int):
    pass
