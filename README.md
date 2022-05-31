# PTT Login

Login to [PTT](https://www.ptt.cc/index.html).

> **Warning** Do not login everyday at the same time. Your account [will be banned](https://www.ptt.cc/bbs/ID_Multi/M.1559453943.A.CBF.html).

## Usage

Use docker.

```sh
docker run -it hyperbola/ptt-login:v1 -u username -p password
```

You may want to run it everyday in a random time so that your account will not be banned. Following crontab tries to login to PTT at random time from 08:10 to 08:59 everyday.

```crontab
0 0 * * * docker run -it hyperbola/ptt-login:v1 -u username -p password | at 08:$(( $RANDOM % 50 + 10 ))
```

### Options

- `-u`, `--user` ptt username
- `-p`, `--pswd` ptt password
- `-P`, `--pswd-path` ptt password file; less prior than `--pswd`

Noted that environment variable `USERNAME` overrides `--user`, and environment variable `PASSWORD` overrides `--pswd` and `--pswd-path`.
