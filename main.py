import pygame as pg
from objects import *
from time import sleep

screen = pg.display.set_mode((600, 650))
screen.fill(pg.Color('#36454F'))

snake = Snake()
block_dirs = {}.fromkeys(['w', 's', 'a', 'd'], True)

score_counter = Score()

borderLine = Line(pg.Color("red"), [(0, 50), (600, 50)], 4)

apple = Apple()

run = True
clock = pg.time.Clock()
pg.display.flip()

while run:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            run = False
        elif ev.type == pg.KEYDOWN:
            # Matching pressed keys with 'W', 'A', 'D', 'S', processing snake's movement
            match ev.key:
                case pg.K_w if block_dirs['w']:
                    snake.move_x = 0
                    snake.move_y = -1
                    block_dirs = {'w': True, 's': False, 'a': True, 'd': True}
                case pg.K_s if block_dirs['s']:
                    snake.move_x = 0
                    snake.move_y = 1
                    block_dirs = {'w': False, 's': True, 'a': True, 'd': True}
                case pg.K_d if block_dirs['d']:
                    snake.move_x = 1
                    snake.move_y = 0
                    block_dirs = {'w': True, 's': True, 'a': False, 'd': True}
                case pg.K_a if block_dirs['a']:
                    snake.move_x = -1
                    snake.move_y = 0
                    block_dirs = {'w': True, 's': True, 'a': True, 'd': False}
    screen.fill(pg.Color('#36454F'))
    if snake.game_over:
        gameOver = Text("Times New Roman", 40, f"Game Over! Your score was {score_counter.i}", pg.Color("red"),
                        (35, 175))
        restartHint = Text("Times New Roman", 50, "Print R to restart", pg.Color("red"), (125, 325))
        screen.fill(pg.Color("black"))
        del apple, snake
        gameOver.draw(screen)
        restartHint.draw(screen)
        pg.display.update()
        run_inner = True
        while run_inner:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()
                elif i.type == pg.KEYDOWN:
                    if i.key == pg.K_r:
                        snake = Snake()
                        apple = Apple()
                        score_counter.i = 0
                        screen.fill(pg.Color('#36454F'))
                        pg.display.update()
                        clock.tick(30)
                        run_inner = False
                        break


    else:
        snake.is_lose()
        apple.update(scr=screen, snake_=snake, score=score_counter)
        if apple.delete is True:
            del apple
            apple = Apple()
        snake.update(scr=screen)
        """Updating Apple object & checking out whether snake's head touching it, 
            then increasing length of the snake and score, delete apple """

        # Rendering text for score and putting it on the screen if game is not over
        Text("Arial", 44, f"Score : {score_counter.i}", pg.Color('gold'),
             (0, 0), bg_color=pg.Color('black')).draw(screen)
        # Drawing Borderline
        borderLine.draw(screen)

        pg.display.update()
        clock.tick(30)

pg.quit()
