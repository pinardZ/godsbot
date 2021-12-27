# godsbot
godsbot for financial freedom

## Requirements

python version >= 3.7.1
PyAutoGUI version = 0.9.53

## How to start

python3 -m godsbot
    
## Architecture

### Flows

![image](https://github.com/pinardZ/godsbot/blob/main/static/imgs/flow_main.png)

![image](https://github.com/pinardZ/godsbot/blob/main/static/imgs/flow_replace_account.png)

![image](https://github.com/pinardZ/godsbot/blob/main/static/imgs/flow_game_main.png)

![image](https://github.com/pinardZ/godsbot/blob/main/static/imgs/flow_reset_account.png)

### Data persistence

Sqlite3

```
create table accounts
(
    id             integer not null
        constraint accounts_pk
            primary key autoincrement,
    email          varchar    default '' not null,
    password       varchar    default '' not null,
    disabled       tinyint(1) default 0 not null,
    created_at     datetime   default CURRENT_TIMESTAMP not null,
    last_logged_at datetime,
    last_logged_ip varchar    default '' not null,
    status         int        default 0
);

create unique index accounts_email_uindex
    on accounts (email);
```

### Runtime context

Defines the Context type, which carries index, account, game, and other request-scoped values between processes.
