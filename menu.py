# menu
import pygame_menu as pgm
import pygame as pg
pg.init()

def set_difficulty(selected: tuple, value) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')


def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    global userName
    print(f'{userName.get_value()}, Do the job here!')


class SnakeMenu:
    def __init__(self, scr, pos: tuple, title='Hello!',
                 theme = pgm.themes.THEME_DEFAULT):
        self.screen = scr
        self.title = title
        self.x, self.y = pos
        self.theme = theme
        self.menu = pgm.Menu(self.title, width=self.x, height=self.y,
                       theme=self.theme)


    def run(self):
        userName = self.menu.add.text_input('Name :', default=' ', maxchar=15)
        self.menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
        self.menu.add.button('Play', start_the_game)
        self.menu.add.button('Quit', pgm.events.EXIT)
        self.menu.mainloop(self.screen)


screen = pg.display.set_mode((600, 600))
snm = SnakeMenu(screen, (600, 600))
snm.run()
        
