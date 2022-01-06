import psutil
import subprocess
import win32api

# env
env_mac = 'mac'
env_win = 'win'
env = env_win

# common
python_cmd = 'python3'
play_game_module = 'play_game'
gods_bot_module = 'gods_bot'
gods_bot_exe = 'gods_bot.exe'
# mac
immutable_app_path = '/Applications/Immutable.app'
gods_game_path = '/gods.app/Contents/MacOS/gods'
# win
immutable_lnk_path = 'Immutable.lnk'
immutable_exe = 'Immutable.exe'
gods_exe = 'gods.exe'


def open_immutable():
    if env == env_mac:
        open_app(immutable_app_path)
    elif env == env_win:
        open_app(immutable_lnk_path)


def close_immutable():
    if env == env_mac:
        kill_process_mac(immutable_app_path)
    elif env == env_win:
        kill_process_win(immutable_exe)


def check_immutable_running():
    if env == env_mac:
        return check_process_running_mac(immutable_app_path)
    elif env == env_win:
        return check_process_running_win(immutable_exe)


def check_gods_running():
    if env == env_mac:
        return check_process_running_mac(gods_game_path)
    elif env == env_win:
        return check_process_running_win(gods_exe)


def execute_play_game(account_id):
    return execute_python_module(play_game_module, [account_id])


def run_gods_bot():
    open_app(gods_bot_exe)


def stop_gods_bot():
    kill_process_win(gods_bot_exe)


def open_app(app):
    if env == env_mac:
        run_cmd("open %s" % app)
    elif env == env_win:
        print('open_app' + app)
        win32api.ShellExecute(0, 'open', app, '', '', 1) 
        # run_cmd("%s" % app)
    

def check_process_running_mac(process):
    ret = run_cmd('ps -ef | grep %s | grep -v grep' % process)
    return ret != ''


def kill_process_mac(process):
    run_cmd("ps -ef | grep %s | grep -v grep |awk '{print $2}' | xargs kill -9" % process)


def check_process_running_win(process):
    pl = psutil.pids()
    for pid in pl:
        # print(psutil.Process(pid).name())
        if psutil.Process(pid).name() == process:
            return True
    return False


def kill_process_win(process):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == process:
            run_cmd('taskkill /F /IM %s' % process)


def execute_python_module(module, args):
    cmd = '%s -m %s' % ('python', module)
    for arg in args:
        cmd += ' ' + str(arg)
    return run_cmd(cmd)


def run_cmd(command):
    """Run shell command."""

    ret = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         encoding="utf-8", timeout=None)
    if ret.returncode != 0:
        print("error:", ret)
        return ''

    print("success:", ret)
    return ret.stdout