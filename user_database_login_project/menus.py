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

    do_l = do_login

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

    do_c = do_create

    def do_list(self, _):
        with transaction() as t:
            for user in t.query(User):
                print(user.username)

    do_ll = do_list

    def do_exit(self, _):
        return True

    def do_admin(self, _):
        Admin.verify_exists()
        if User.get(Admin.admin_name).ask_and_verify('enter admin password: '):
            Admin().cmdloop()

    def cmdloop(self, intro=None):
        return super().cmdloop('type "help" or "?" to view available commands')


class LoggedIn(Cmd):
    def __init__(self, user: User):
        super().__init__()
        self.user = user

    def do_delete(self, _):
        if not self.user.ask_and_verify('retype your password to delete this account: '):
            return

        print(f'deleted account {self.user.username}')
        with transaction() as t:
            t.query(User).filter(User.username == self.user.username).delete()

        return self.do_logout(_)

    def do_rename(self, _):
        if not self.user.ask_and_verify('retype password to change your username: '):
            return

        with transaction():
            self.user.username = next(normalize(input('enter new username: ')))

        return self.do_logout(_)

    def do_password(self, _):
        if not self.user.ask_and_verify('retype password to change your password: '):
            return

        with transaction():
            self.user.password = hash_password(next(normalize(input('enter new password: '))))

        return self.do_logout(_)

    def do_logout(self, _):
        print(f'you have logged out of {self.user.username}')
        return True


class Admin(Cmd):
    admin_name = 'admin'

    @classmethod
    def verify_exists(cls):
        if not User.exists(cls.admin_name):
            while not (password := normalize(input('enter new admin password: '))):
                pass
            User.new(cls.admin_name, password)

    def do_delete(self, *args):
        if not args:
            print('missing argument: account name')
            return

        with transaction() as t:
            username = normalize(args[0])
            if not (user := User.get(username)):
                print(f'no such user: {username}')
            elif user.username == self.admin_name:
                print('well done, you played yourself...')
                t.query(User).filter(User.username == self.admin_name).delete()
                return True
            else:
                t.query(User).filter(User.username == user.username).delete()
                print(f'deleted user: {user.username}')

    def do_list(self, _):
        with transaction() as t:
            for user in t.query(User):
                print(user.username)

    do_l = do_list

    def do_logout(self, _):
        print('you logged out of the admin account')
        return True
