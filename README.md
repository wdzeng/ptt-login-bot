# 批踢踢登入機器人

[![release](https://badgen.net/github/release/wdzeng/ptt-login-bot/stable?color=red)](https://github.com/wdzeng/ptt-login-bot/releases/latest)
[![github](https://badgen.net/badge/icon/github/black?icon=github&label=)](https://github.com/wdzeng/ptt-login-bot)
[![docker](https://badgen.net/badge/icon/docker?icon=docker&label=)](https://hub.docker.com/repository/docker/hyperbola/ptt-login-bot)

需搭配 cron 使用。注意長期在同一時間登入[會被 ban 帳號](https://www.ptt.cc/bbs/ID_Multi/M.1559453943.A.CBF.html)。

## 執行方式

請先準備 [docker](https://docker.io)。

```sh
docker run -it \
    hyperbola/ptt-login-bot:v1 -u username -p password
```

以下 cron 會讓機器人在每日 08:10 ~ 08:59 之間隨機進行登入，這樣就不會被 ban。

```crontab
0 0 * * * docker run hyperbola/ptt-login-bot:v1 -u username -p password | at 08:$(( $RANDOM % 50 + 10 ))
```

## 參數

- `-u`, `--user` 批踢踢帳號
- `-p`, `--pswd` 批踢踢密碼
- `-P`, `--pswd-path` 密碼檔案，優先於 `--pswd`

環境變數 `USERNAME` 優先於 `--user`；環境變數 `PASSWORD` 優先於 `--pswd-path` 和 `--pswd`。

## Exit Code

| Exit code | 描述 |
| --------- | ----------- |
| 0         | 登入成功。   |
| 87        | 密碼錯誤。 |
| 255       | 不明原因錯誤。 |

## 姊妹機器人

- [蝦皮簽到機器人](https://github.com/wdzeng/shopee-coins-bot)
- [Pinkoi 簽到機器人](https://github.com/wdzeng/pinkoi-coins-bot)
- [Telegram ID 覬覦者](https://github.com/wdzeng/telegram-id-pretener)
