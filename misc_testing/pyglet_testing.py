import pyglet
import re


def main():
    window = pyglet.window.Window()
    label = pyglet.text.Label('Hello, world',
                              font_name='Times New Roman',
                              font_size=36,
                              x=window.width // 2, y=window.height // 2,
                              anchor_x='center', anchor_y='center')

    @window.event
    def on_draw():
        window.clear()
        label.draw()

    pyglet.app.run()

    # regex_pattern = '[\d]'
    # compiled_regex = re.compile(regex_pattern)
    # search_string = "abcABC123!@#"
    # result = re.findall(regex_pattern, search_string)
    #
    # final_str = ''
    #
    # for i in result:
    #     final_str += i
    #
    # print(final_str)


if __name__ == '__main__':
    main()
