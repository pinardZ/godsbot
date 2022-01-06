import asyncio
import logging
import pyautogui
from main import runtime, shell
import sys
import time


logging.basicConfig(level=logging.INFO, format='play_game %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')


def main():
    """Run the main game program. The play button must be visible."""

    logging.info('Game Program Started.')
    arg = sys.argv[1]
    account_id = int(arg)
    ctx = runtime.Context(account_id)
    if ctx.account.status > 0:
        logging.info("account %d status is %d" % (ctx.account.id, ctx.account.status))
        print(0)
        return
    time.sleep(5)
    while True:
        if not click_play_btn(ctx):
            logging.info("play btn is not clickable")
            print(0)
            return
        wait_game_beg(ctx)
        time.sleep(5)
        asyncio.run(run_gods_bot(ctx))
        wait_game_end(ctx)
        time.sleep(5)
        stop_gods_bot(ctx)
        if remote_check_status(ctx):
            logging.info("account %d status is %d" % (ctx.account.id, ctx.account.status))
            print(1)
            return


def click_play_btn(ctx: runtime.Context) -> bool:
    """Click play button. Return true if button visible and clickable"""

    screen_width, screen_height = pyautogui.size()
    print(screen_width, screen_height)

    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)

    # play 位置： 17 - 18.5, 总 34 * 9   5.5-6.5

    play_btn_x = screen_width * 18.0 / 34.0
    play_btn_y = screen_height * 5.5 / 9.0
    print(play_btn_x, play_btn_y)

    pyautogui.moveTo(play_btn_x, play_btn_y, 3)
    print(currentMouseX, currentMouseY)

    pyautogui.click(play_btn_x, play_btn_y)
    # pyautogui.click(play_btn_x, play_btn_y)
    return True


def wait_game_beg(ctx: runtime.Context):
    """Waiting until gods program begin"""

    check_game_until(True)


def wait_game_end(ctx: runtime.Context):
    """Waiting until gods program end"""

    check_game_until(False)


def check_game_until(active: bool):
    """Check gods program active use loop"""

    while True:
        time.sleep(5)
        running = shell.check_gods_running()
        print('check_game_until running %d' % running)
        if (active and running) or (not active and not running):
            break


async def run_gods_bot(ctx: runtime.Context):
    """Run gods bot"""

    logging.info('Runs gods_bot shell.')
    print('Runs gods_bot shell.')
    asyncio.create_task(async_run_gods_bot())
    

async def async_run_gods_bot():
    ret = shell.run_gods_bot()
    print('Completed gods_bot shell.Status is %s' % ret)
    logging.info('Completed gods_bot shell.Status is %s', ret)


def stop_gods_bot(ctx: runtime.Context):
    """Stop gods bot"""

    logging.info('Stop gods_bot shell.')
    print('Stop gods_bot shell')
    shell.stop_gods_bot()
    logging.info('Killed gods_bot shell.')
    print('Killed gods_bot shell')


def remote_check_status(ctx: runtime.Context) -> bool:
    """Check account status by remote api"""

    return True


if __name__ == '__main__':
    main()
