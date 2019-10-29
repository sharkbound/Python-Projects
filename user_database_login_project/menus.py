from cmd import Cmd
import shlex

from userlogindb import *


def split(string):
    try:
        return shlex.split(string)
    except:
        return string.split()


class MainMenu(Cmd):
    def do_login(self, cmd):
        if len(args := split(cmd)) != 2:
            print('login must be passed the username and login, and must be exactly 2 arguments')
            return

        username, password = normalize(*args)
        if (user := User.get(username)) is None:
            print(f'{username} does not exists, you can create "{username}" by doing "create {username} PASSWORD"')
            return

        if not user.verify(password):
            print(f'password did not match for {user.username}')
            return

        LoggedIn(user).cmdloop(f'you are logged in as {user.username}')

    def do_create(self, cmd):
        if len(args := split(cmd)) != 2:
            print('create must be passed the username and password for the created account')
            return

        username, password = normalize(*args)
        if User.exists(username):
            print(f'account {username!r} already exists')
            return

        User.new(username, password)
        print(f'created account {username}, type "login {username} PASSWORD" to login into it')

    def do_exit(self, _):
        return True

    def cmdloop(self, intro=None):
        return super().cmdloop('type "help" or "?" to view available commands')


class LoggedIn(Cmd):
    def __init__(self, user: User):
        super().__init__()
        self.user = user

    def do_delete(self, _):
        if not self.user.verify(input('retype your password to delete this account: ')):
            print('passwords did not match, cancelling deletion')
            return

        print(f'deleted account {self.user.username}')
        with transaction() as t:
            t.query(User).filter(User.username == self.user.username).delete()

        return self.do_logout(_)

    def do_logout(self, _):
        print(f'you have logged out of {self.user.username}')
        return True
