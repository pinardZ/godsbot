import logging

import runtime
import shell

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')


def main():
    """Run the main program. The VPN.program and Immutable.app must be installed."""

    logging.info('Program Started. Press Ctrl-C to abort at any time.')
    ctx = runtime.Context(1)
    while True:
        replace_account(ctx)
        login_vpn(ctx)
        open_game(ctx)
        play_game(ctx)
        close_game(ctx)
        logout_vpn(ctx)


def replace_account(ctx: runtime.Context):
    """Run replace_account shell.Return account if shell completed success."""

    logging.info('Runs replace_account shell.')
    ret = shell.run_cmd("python3 -m replace_account %d" % ctx.index)
    logging.info('Completed replace_account shell.Account id is %s', ret)
    ctx.setIndex(int(ret))


def login_vpn(ctx: runtime.Context):
    """Login vpn program.Args account to acquire same ip if program support."""

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