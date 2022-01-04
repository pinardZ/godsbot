import os
import shutil
import sys
import time
import logging

from .logger import BFLog
from . import instance
from . import runtime
from . import shell

log = BFLog().getLogger()

game_account_path = "C:\\Users\\wwly\\AppData\\Roaming\\immutable-launcher\\"


def main():
    """Run the main program. The VPN.program and Immutable.app must be installed."""

    log.info('Program Started. Press Ctrl-C to abort at any time.')
    ctx = runtime.Context(1)
    while True:
        # read_account(ctx)
        # login_vpn(ctx)
        open_app(ctx)
        # check_app_running()
        # time.sleep(5)
        # play_game(ctx)
        # time.sleep(5)
        # close_app(ctx)
        # logout_vpn(ctx)
        # reset_account(ctx)
        # ctx = runtime.Context(ctx.index + 1)
        sys.exit(0)


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


def login_vpn(ctx: runtime.Context):
    """Login vpn program.Args account to acquire same ip if program support."""

    idx = ctx.index
    compute_cli = instance.get_compute_client()
    ip = instance.get_instance_ip(instance.start_instance(compute_cli, idx))
    # TODO ip 填到 vpn


def logout_vpn(ctx: runtime.Context):
    """Logout vpn program."""

    idx = ctx.index
    compute_cli = instance.get_compute_client()
    instance.stop_instance(compute_cli, idx)


def open_app(ctx: runtime.Context):
    """Open Immutable App.TODO check program is alive."""
    shell.open_immutable()


def close_app(ctx: runtime.Context):
    """Close Immutable App.TODO check program is stopped."""

    shell.close_immutable()


def check_app_running():
    """Check Immutable App active use loop"""

    while True:
        time.sleep(5)
        if shell.check_immutable_running():
            return


def play_game(ctx: runtime.Context):
    """Run play_game shell.Args account to plat."""

    logging.info('Runs play_game shell.')
    ret = shell.execute_play_game(ctx.account.id)
    logging.info('Completed play_game shell.Status is %s', ret)
    ctx.account.status = int(ret)


if __name__ == '__main__':
    main()
