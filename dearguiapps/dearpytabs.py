from dearpygui.dearpygui import *

add_tab_bar('tab bar 1')
add_tab('new tab', closable=False, tip='this tooltip does not work when selected because the tab has a child')
add_button('placeholder')
end_tab()

add_tab('new tab 2', closable=False, tip='this tooltip works because its empty')
end_tab()
end_tab_bar()

set_main_window_size(800, 600)
start_dearpygui()
