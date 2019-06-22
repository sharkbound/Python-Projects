from data import MenuAction
from menus import Menu
from util import str_to_args


def run_menu(base_menu: Menu):
    history = [base_menu]

    def current():
        return history[-1]

    while True:
        raw = current().prompt()
        args = str_to_args(raw)

        if not args:
            continue

        cmd, *args = args
        result = current().handle_input(raw, cmd, *args)

        if result is MenuAction.go_back and len(history) > 1:
            history.pop()

        elif result is MenuAction.exit:
            exit()

        elif isinstance(result, Menu):
            history.append(result)
