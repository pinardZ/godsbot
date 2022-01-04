import subprocess


def run_cmd(command):
    """Run shell command."""

    ret = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         encoding="utf-8", timeout=None)
    if ret.returncode != 0:
        print("error:", ret)
        return ''

    print("success:", ret)
    return ret.stdout
