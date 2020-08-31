from dearpygui.dearpygui import *

WIDTH, HEIGHT = 800, 600

set_main_window_size(WIDTH, HEIGHT)
set_main_window_title('MemoKeeper')

memos = {}


class ID:
    memo_input_add = 'memo name (press enter to confirm)'
    memo_listbox = '##allmemos'
    all_memo_data = '##all_memos_data'


def show_memo(sender, data):
    memo_name = get_value(ID.memo_input_add) if data != 'uselistbox' else get_data(ID.all_memo_data)[get_value(ID.memo_listbox)]
    text_id = f'##{memo_name}_text'
    text_data_id = f'##{text_id}_data'
    save_and_close_id = f'save and close##{memo_name}'

    show = memo_name in memos
    if memo_name not in memos:
        memos[memo_name] = ''
        get_data(ID.all_memo_data).append(memo_name)

    for item in (memo_name, text_id, save_and_close_id):
        if does_item_exist(item):
            delete_item(item)

    add_data(text_data_id, memos[memo_name])

    if show:
        window_width = 400
        add_window(memo_name, width=window_width, height=200)
        add_data(text_data_id, memos[memo_name])
        add_input_text(text_id, multiline=True, data_source=text_data_id, width=window_width)
        add_button(save_and_close_id, callback=save_and_exit_clicked.__name__)
        end_window()

    if sender == ID.memo_input_add:
        set_value(sender, '')


def save_and_exit_clicked(sender: str, data):
    text = get_data(f'##{sender[sender.index("#"):]}_text_data')
    memos[sender[sender.rindex('#') + 1:]] = text
    delete_item(get_active_window())


def listbox_clicked(sender, data):
    show_memo(sender, 'uselistbox')



def main():
    add_input_text(ID.memo_input_add, width=200, callback='show_memo', on_enter=True)
    add_data(ID.all_memo_data, [])
    add_listbox(ID.memo_listbox, [], callback=listbox_clicked.__name__, secondary_data_source=ID.all_memo_data)
    start_dearpygui()


main()
