import sqlite3

from objc._objc import function

DB_NAME = 'godsbot'
TABLE_NAME = 'accounts'


class Account(object):
    """Accounts Table Object."""

    def __init__(self, id: int, email: str, password: str, disabled: bool, created_at: str,
                 last_logged_at: str, last_logged_ip: str, status: int):
        self.id = id
        self.email = email
        self.password = password
        self.disabled = disabled
        self.created_at = created_at
        self.last_logged_at = last_logged_at
        self.last_logged_ip = last_logged_ip
        self.status = status


def db_operation(op: function, commit=False):
    """DB operation common function."""

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    res = op(cursor)
    cursor.close()
    if commit:
        conn.commit()
    conn.close()
    return res


def count_accounts() -> int:
    """DB count all accounts."""

    def op(cursor: sqlite3.Cursor):
        cursor.rowcount
        cursor.execute('SELECT COUNT(1) FROM `%s`' % TABLE_NAME)
        res = cursor.fetchone()
        return res[0]

    return db_operation(op)


def get_account(id: int) -> Account:
    """DB get account by id."""

    def op(cursor: sqlite3.Cursor):
        cursor.execute('SELECT * FROM `%s` WHERE id = ?' % TABLE_NAME, (id,))
        res = cursor.fetchone()
        account = Account(*res)
        return account

    return db_operation(op)


def reset_accounts():
    """DB reset all accounts to set status be 0."""

    def op(cursor: sqlite3.Cursor):
        cursor.execute('UPDATE `%s` SET status = ? WHERE id > ?' % TABLE_NAME, (0, 0))
        return 0
    db_operation(op, True)


def set_account_status(id: int, status: int):
    """DB reset all accounts to set status be 0."""

    def op(cursor: sqlite3.Cursor):
        cursor.execute('UPDATE `%s` SET status = ? WHERE id = ?' % TABLE_NAME, (status, id))
        return 0
    db_operation(op, True)


def ban_account(id: int):
    """DB ban account to set disabled be 1."""

    def op(cursor: sqlite3.Cursor):
        cursor.execute('UPDATE `%s` SET disabled = ? WHERE id = ?' % TABLE_NAME, (1, id))
        return 0
    db_operation(op, True)

