import sys
from . import dao


def get_account_cfg_dir(id: int) ->str:
    return '.\\static\\login_files\\%d' % id
    # return '/static/login_files/%d' % id


class Context(object):
    """Runtime context."""

    def __init__(self, id: int):
        self.index = 0
        self.accounts_cnt = 0
        self.account = None
        self.account_cfg_dir = get_account_cfg_dir(id)
        self.setIndex(id)

    def setIndex(self, id: int):
        self.index = id
        self.accounts_cnt = dao.count_accounts()
        if id > self.accounts_cnt:
            sys.exit(0)
        self.account = dao.get_account(id)
        self.account_cfg_dir = get_account_cfg_dir(id)

    def setStatus(self, status: int):
        self.account.status = status
        dao.set_account_status(self.index, status)
