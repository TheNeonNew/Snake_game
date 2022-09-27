import pygame as pg
from math import pi
from random import randrange

pg.font.init()


class Text:
    def __init__(self, font_name: str, font_size: int, text: str, fg_color,
                 pos_text: tuple, smooth=True, bg_color=None):
        self.font = pg.font.SysFont(font_name, font_size)
        self.text = text
        self.pos = pos_text
        self.text_color = fg_color
        self.smoothing = smooth
        self.bg_color = bg_color

    def draw(self, scr):
        scr.blit(self.font.render(self.text, self.smoothing, self.text_color, self.bg_color),
                 self.pos)


class Line:
    """Class for creating lines"""
    def __init__(self, color, coordsArr: list, boldness: int):
        self.color = color
        self.start_coords, self.end_coords = coordsArr
        self.boldness = boldness

    def draw(self, scr):
        pg.draw.line(scr, self.color,
                     self.start_coords,
                     self.end_coords, self.boldness)


class Snake:
    def __init__(self, length=1):
        self.step = 30
        self.x = 300
        self.y = 300

        self.body = [(self.x, self.y)]
        self.len = length
        self.speed = 7
        self.move_x = 0
        self.move_y = 0
        self.timer = 0

        self.game_over = False

    def draw(self, scr):
        [(pg.draw.rect(scr, pg.Color('lightgreen') if (i, j) != self.body[-1] else pg.Color('#39FF14'),
                       (i, j, self.step - 1, self.step - 1))) for i, j in self.body]

    def move(self):
        if not (self.timer % self.speed):
            self.x += self.step * self.move_x
            self.y += self.step * self.move_y
            self.body.append((self.x, self.y))
            self.body = self.body[-self.len:]
        self.timer += 1

    def is_lose(self):
        if len(self.body) != len(set(self.body)): self.game_over = True
        for k in self.body:
            if any([k[0] > 600, k[0] < 0, k[1] < 50, k[1] > 650]):
                self.game_over = True

    def update(self, **kwargs):
        if kwargs.get('scr'):
            self.move()
            self.draw(kwargs.get('scr'))


class Score:
    def __init__(self):
        self.i = 0

    def inc(self):
        self.i += 10


class Apple:
    def __init__(self):
        self.size = 30
        self.x = randrange(30, 540, self.size)
        self.y = randrange(60, 600, self.size)
        self.delete = False

    def draw(self, scr):
        pg.draw.rect(scr, pg.Color('red'), (self.x, self.y, self.size, self.size))

    def is_collide(self, snk, score):
        if pg.Rect.colliderect(pg.Rect((self.x, self.y, self.size, self.size)),
                               pg.Rect((snk.body[0][0], snk.body[0][1], snk.step, snk.step))):
            self.delete = True
            score.i += 1
            snk.len += 1
            snk.speed -= 1
            snk.speed = max(snk.speed, 3)

    def update(self, **kwargs):
        if kwargs.get('scr') and kwargs.get('snake_'):
            self.is_collide(kwargs.get('snake_'), kwargs.get('score'))
            self.draw(kwargs.get('scr'))


if __name__ == "__main__":
    pass
