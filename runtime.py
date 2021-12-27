import dao


class Context(object):
    """Runtime context."""

    def __init__(self, id: int):
        self.index = 0
        self.accounts_cnt = 0
        self.account = None
        self.account_cfg_dir = ''
        self.setIndex(id)

    def setIndex(self, id: int):
        self.index = id
        self.accounts_cnt = dao.count_accounts()
        self.account = dao.get_account(id)
        self.account_cfg_dir = './login_files/%d' % id

    def setStatus(self, status: int):
        self.account.status = status
        dao.set_account_status(self.index, status)
