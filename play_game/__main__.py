import logging
import pyautogui
import runtime
import shell
import sys
import time


logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')


def main():
    """Run the main game program. The play button must be visible."""

    logging.info('Game Program Started.')
    arg = sys.argv[1]
    account_id = int(arg)
    ctx = runtime.Context(account_id)
    if ctx.account.status > 0:
        print(ctx.account.status)
        return
    while True:
        if not click_play_btn(ctx):
            print(0)
            return
        wait_game_beg(ctx)
        run_gods_bot(ctx)
        wait_game_end(ctx)
        stop_gods_bot(ctx)
        if remote_check_status(ctx):
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
    pyautogui.click(play_btn_x, play_btn_y)
    return True


def wait_game_beg(ctx: runtime.Context):
    """Waiting until gods program begin"""

    check_game_running(True)


def wait_game_end(ctx: runtime.Context):
    """Waiting until gods program end"""

    check_game_running(False)


def check_game_running(alive: bool):
    """Check gods program alive use loop"""

    while True:
        time.sleep(5)
        ret = shell.run_cmd('ps -ef | grep "GAME PROGRAM" | grep -v grep')
        if (alive and ret == '') or (not alive and ret != ''):
            break


async def run_gods_bot(ctx: runtime.Context):
    """Run gods bot"""

    logging.info('Runs gods_bot shell.')
    ret = shell.run_cmd("python3 -m gods_bot")
    logging.info('Completed gods_bot shell.Status is %s', ret)


def stop_gods_bot(ctx: runtime.Context):
    """Stop gods bot"""

    logging.info('Stop gods_bot shell.')
    shell.run_cmd("ps - ef | python3 -m gods_bot | grep - v grep | awk '{print $2}' | xargs kill - 9")
    logging.info('Killed gods_bot shell.')


def remote_check_status(ctx: runtime.Context) -> bool:
    """Check account status by remote api"""

    return False


if __name__ == '__main__':
    main()
