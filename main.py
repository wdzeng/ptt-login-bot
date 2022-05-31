import sys
import os
import argparse
from PyPtt import PTT

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help='ptt username')
parser.add_argument('-p', '--pswd', help='ptt password')
parser.add_argument('-P', '--pswd-path', help='ptt password file')
args = parser.parse_args()


def get_username():
    return os.environ.get('USERNAME') or args.user


def get_password():
    pswd = os.environ.get('PASSWORD') or args.pswd
    if not pswd and args.pswd_path:
        path = os.path.abspath(args.pswd_path)
        try:
            with open(path, 'r') as f:
                pswd = f.read()
        except:
            sys.stderr.write('Failed to read password from file: ' + path + '\n')
            sys.exit(255)
    return pswd


def ptt_login(username, password):
    ptt_bot = PTT.API(log_level=PTT.log.level.SILENT)
    try:
        ptt_bot.login(username, password, kick_other_login=True)
        print('Login succeeded.')
        return 0
    except (PTT.exceptions.WrongIDorPassword, PTT.exceptions.WrongPassword):
        sys.stderr.write('Wrong password.\n')
        return 87
    except PTT.exceptions.NoSuchUser:
        sys.stderr.write('No such user.\n')
        return 87
    except PTT.exceptions.LoginTooOften:
        sys.stderr.write('Too much login.\n')
        return 1
    except:
        sys.stderr.write('Login failed for unknown reason.\n')
        return 255


def main():
    username = get_username()
    password = get_password()
    if not username or not password:
        sys.stderr.write('Missing username or password.\n')
        sys.exit(87)
    exit_code = ptt_login(username, password)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
