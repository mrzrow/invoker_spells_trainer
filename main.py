import pygame as pg
from constants import *
from imgs import *


def draw_combination(_comb):
    comb_cast = {'0': quas, '1': wex, '2': exort}
    comb_pos = {'0': second_rect, '1': first_rect, '2': zero_rect}
    for _i, _elem in enumerate(_comb):
        if _elem == '3':
            continue
        cast = comb_cast[_elem]
        pos = comb_pos[str(_i)]
        win.blit(cast, pos)
    pg.draw.rect(win, GREY, second_rect, 2)
    pg.draw.rect(win, GREY, first_rect, 2)
    pg.draw.rect(win, GREY, zero_rect, 2)
    win.blit(invoke, third_rect)
    pg.draw.rect(win, GREY, third_rect, 4)


combination = '333'
clock = pg.time.Clock()
run = True
while run:
    win.fill(bgColor)
    dt = clock.tick(30) / 1000
    pg.key.set_repeat(0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
                break
            elif event.key == pg.K_q:
                combination = combination[1:] + '0'
            elif event.key == pg.K_w:
                combination = combination[1:] + '1'
            elif event.key == pg.K_e:
                combination = combination[1:] + '2'

    draw_combination(combination)

    pg.display.update()

pg.quit()
