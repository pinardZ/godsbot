import logging
from main import runtime
import sys
import time


logging.basicConfig(level=logging.INFO, format='replace_account %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')


def main():
    """TODO replace account program"""

    arg = sys.argv[1]
    index = int(arg)
    ctx = runtime.Context(index)
    ret = foo(ctx)
    print(ret)


def foo(ctx: runtime.Context) -> int:
    time.sleep(5)
    return 0


if __name__ == '__main__':
    main()
