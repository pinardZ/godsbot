import os
import logging
import shutil
from v1.logger import BFLog
import runtime
import shell

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
log = BFLog().getLogger()

game_account_path = "C:\\Users\\wwly\\AppData\\Roaming\\immutable-launcher\\"

def main():
    """Run the main program. The VPN.program and Immutable.app must be installed."""

    logging.info('Program Started. Press Ctrl-C to abort at any time.')
    ctx = runtime.Context(1)
    while True:
        read_account(ctx)
        login_vpn(ctx)
        # open_game(ctx)
        reset_account(ctx)
        # play_game(ctx)
        # close_game(ctx)
        # logout_vpn(ctx)
        # replace_account(ctx)
        ctx = runtime.Context(ctx.index + 1)

def read_account(ctx: runtime.Context):
    account_path = ctx.account_cfg_dir
    # print(account_path)
    account_file_list = os.listdir(account_path)
    # print(account_file_list)
    # 复制账号文件
    log.info("复制账号 %d cookies 至游戏目录" % ctx.index)
    for file in account_file_list:
        temp_path = os.path.join(account_path, file)
        shutil.copy(temp_path, game_account_path)

def reset_account(ctx: runtime.Context):
	account_path = ctx.account_cfg_dir

	game_file_list = os.listdir(game_account_path)
	game_file_path_list = [os.path.join(game_account_path, file) for file in game_file_list]

	# 复制账号文件
	log.info("重置账号 %d cookies" % ctx.index)
	for filename in game_file_list:
		if filename == "Cookies" or filename == "config.json":
			file_path = os.path.join(game_account_path, filename)
			shutil.copy(file_path, account_path)

def replace_account(ctx: runtime.Context):
    """Run replace_account shell.Return account if shell completed success."""

    logging.info('Runs replace_account shell.')
    ret = shell.run_cmd("python3 -m replace_account %d" % ctx.index)
    logging.info('Completed replace_account shell.Account id is %s', ctx.index)
    index = ctx.index + 1
    ctx.setIndex(index)


def login_vpn(ctx: runtime.Context):
    """Login vpn program.Args account to acquire same ip if program support."""
    ret = shell.run_cmd("python3 -m change_ip %d" % ctx.index)
    pass


def logout_vpn(ctx: runtime.Context):
    """Logout vpn program."""

    pass


def open_game(ctx: runtime.Context):
    """Open Immutable App.TODO check program is alive."""

    shell.run_cmd("open /Applications/Immutable.app")


def close_game(ctx: runtime.Context):
    """Close Immutable App.TODO check program is stopped."""

    shell.run_cmd("ps -ef | grep /Applications/Immutable.app/Contents/MacOS/Immutable "
                  "| grep -v grep |awk '{print $2}' | xargs kill -9")


def play_game(ctx: runtime.Context):
    """Run play_game shell.Args account to plat."""

    logging.info('Runs play_game shell.')
    ret = shell.run_cmd("python3 -m play_game %d" % ctx.account.id)
    logging.info('Completed play_game shell.Status is %s', ret)
    ctx.account.status = int(ret)


if __name__ == '__main__':
    main()
