from typing import Dict, Any
from pygame.font import SysFont, Font as PygameFont
from pygame import Surface, Color



class Text:
    def __init__(self, **kw):
        """
        :font_name: name of the font
        :text: the text value
        :size: font size
        :bold: specifies if the font is bold
        :italic:  specifies if the font is italic
        :antialias: specifies if the font has antialiasing
        :color: the font color
        :background: the font background (color?)
        """

        self._text = kw.get('text', '')
        self._antialias = kw.get('antialias', False)
        self._font_name = kw.get('font_name', 'Arial')
        self._bold = kw.get('bold', False)
        self._italic = kw.get('italic', False)
        self._color = kw.get('color', Color('white'))
        self._size = kw.get('size', 16)
        self._background = kw.get('background')
        self._render: Surface = None
        self._needs_sysfont_update = True
        self._needs_render_update = True

        self.last_text = self.text
        self.font: PygameFont = None

        self.update_sysfont()
        self.update_render()

    def update_sysfont(self):
        self.font = SysFont(self.font_name, self.size, self.bold, self.italic)
        self.needs_sysfont_update = False

    def update_render(self):
        self._render = self.font.render(self.text, self.antialias, self.color, self.background)
        self._needs_render_update = False

    @property
    def text_size(self):
        return self.font.size(self.text)

    @property
    def render(self):
        if self._needs_render_update:
            self.update_render()

        if self.needs_sysfont_update:
            self.update_sysfont()

        return self._render

    @property
    def needs_sysfont_update(self):
        return self._needs_sysfont_update

    @needs_sysfont_update.setter
    def needs_sysfont_update(self, value):
        assert isinstance(value, bool), 'new needs_sysfont_update value must be a bool'
        if not self._needs_render_update and value:
            self._needs_render_update = value
        self._needs_sysfont_update = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            value = str(value)
        self._text = value
        self._needs_render_update = True

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        assert isinstance(value, (int, float)), 'new size value must be a int or float'
        self._size = value
        self.needs_sysfont_update = True

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        assert isinstance(value, (Color, tuple, list)), 'new color value must be a Color, or RBG tuple'
        self._color = value
        self._needs_render_update = True

    @property
    def italic(self):
        return self._italic

    @italic.setter
    def italic(self, value):
        assert isinstance(value, bool), 'new italic value must be a bool'
        self._italic = value
        self.needs_sysfont_update = True

    @property
    def bold(self):
        return self._bold

    @bold.setter
    def bold(self, value):
        assert isinstance(value, bool), 'new bold value must be a bool'
        self._bold = value
        self.needs_sysfont_update = True

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        assert isinstance(value, str), 'new font_name must be a str'
        self._font_name = value
        self.needs_sysfont_update = True

    @property
    def antialias(self):
        return self._antialias

    @antialias.setter
    def antialias(self, value):
        assert isinstance(value, bool), 'new antialias value must be a bool'
        self._antialias = value
        self.needs_sysfont_update = True

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        assert isinstance(value, (Color, tuple, list)), 'new background must be a Color/RBG tuple or list'
        self._background = value
        self._needs_render_update = True



class FontCache:
    def __init__(self, **kw):
        """
        :param kw: name/Font value pairs
        """
        self._cache: Dict[Any, Text] = kw

    def update(self, name, font: Text):
        """updates """
        self._cache[name] = font

    def get_text(self, name, default=''):
        if name in self:
            return self[name].text
        return default

    def set_text(self, name, new_text, append=False):
        if not isinstance(new_text, str):
            new_text = str(new_text)

        if name not in self:
            return

        if append:
            self[name].text += new_text
        else:
            self[name].text = new_text

    def get_render(self, name):
        if name in self:
            return self[name].render

    def set_color(self, name, value):
        if name in self:
            self[name].color = value

    def set_size(self, name, value, add=False):
        if name not in self:
            return

        if add:
            self[name].size += value
        else:
            self[name].size = value

    def set_bold(self, name, value):
        if name in self:
            self[name].bold = value

    def set_italic(self, name, value):
        if name in self:
            self[name].italic = value

    def set_antialias(self, name, value):
        if name in self:
            self[name].antialias = value

    def rerender(self, name):
        if name in self:
            self[name].update_render()

    def rerender_all(self):
        for font in self:
            font.update_render()

    def __contains__(self, item):
        return item in self._cache

    def __iter__(self):
        yield from self._cache

    def __getitem__(self, item):
        return self._cache.get(item)

    def __setitem__(self, key, value):
        self._cache[key] = value

    def __delitem__(self, key):
        if key in self:
            del self._cache[key]
