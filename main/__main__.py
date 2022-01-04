import logging

from . import runtime
from . import shell
import sys
import time

logging.basicConfig(level=logging.INFO, format='main %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')


def main():
    """Run the main program. The VPN.program and Immutable.app must be installed."""

    logging.info('Program Started. Press Ctrl-C to abort at any time.')
    ctx = runtime.Context(1)
    while True:
        # replace_account(ctx)
        # login_vpn(ctx)
        open_app(ctx)
        check_app_running()
        time.sleep(5)
        play_game(ctx)
        time.sleep(5)
        # close_app(ctx)
        # logout_vpn(ctx)
        sys.exit(0)


def replace_account(ctx: runtime.Context):
    """Run replace_account shell.Return account if shell completed success."""

    logging.info('Runs replace_account shell.')
    ret = shell.run_cmd("python3 -m replace_account %d" % ctx.index)
    logging.info('Completed replace_account shell.Account id is %s', ret)
    ctx.setIndex(int(ret))


def login_vpn(ctx: runtime.Context):
    """Login vpn program.Args account to acquire same ip if program support."""
    ret = shell.run_cmd("python3 -m change_ip %d" % ctx.index)
    pass


def logout_vpn(ctx: runtime.Context):
    """Logout vpn program."""

    pass


def open_app(ctx: runtime.Context):
    """Open Immutable App.TODO check program is alive."""

    shell.run_cmd("open /Applications/Immutable.app")


def close_app(ctx: runtime.Context):
    """Close Immutable App.TODO check program is stopped."""

    shell.run_cmd("ps -ef | grep /Applications/Immutable.app/Contents/MacOS/Immutable "
                  "| grep -v grep |awk '{print $2}' | xargs kill -9")


def check_app_running():
    """Check Immutable App active use loop"""

    while True:
        time.sleep(5)
        ret = shell.run_cmd('ps -ef | grep /Applications/Immutable.app/Contents/MacOS/Immutable | grep -v grep')
        if ret != '':
            break


def play_game(ctx: runtime.Context):
    """Run play_game shell.Args account to plat."""

    logging.info('Runs play_game shell.')
    ret = shell.run_cmd("python3 -m play_game %d" % ctx.account.id)
    logging.info('Completed play_game shell.Status is %s', ret)
    ctx.account.status = int(ret)


if __name__ == '__main__':
    main()
