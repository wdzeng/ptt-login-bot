# PTT Login

Login to [PTT](https://www.ptt.cc/index.html).

> **Warning** Do not login everyday at the same time. Your account will be banned.

## Usage

```sh
docker run -it hyperbola/ptt-login:v1 -u username -p password
```

### Options

- `-u`, `--user` ptt username
- `-p`, `--pswd` ptt password
- `-P`, `--pswd-path` ptt password file; less prior than `--pswd`

Noted that environment variable `USERNAME` overrides `--user`, and environment variable `PASSWORD` overrides `--pswd` and `--pswd-path`.
