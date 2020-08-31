from dearpygui.dearpygui import *


class ID:
    option_radio = 'label name##radio1'


set_main_window_size(800, 600)
set_main_window_title('Radio Buttons')
add_data('selection', ['label 1', 'label 2', 'label 3'])

add_label_text('##label', 'NONE')
add_radio_button(ID.option_radio, [], callback='radio_cb', secondary_data_source='selection')


def radio_cb(sender, data):
    set_value('##label', get_data('selection')[get_value(ID.option_radio)])


start_dearpygui()
