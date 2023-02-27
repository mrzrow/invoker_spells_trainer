import pygame as pg
from constants import *

pg.init()
clock = pg.time.Clock()

win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Example')

pg.display.flip()

quas = pg.image.load('images/invoker_quas.png').convert()
wex = pg.image.load('images/invoker_wex.png').convert()
exort = pg.image.load('images/invoker_exort.png').convert()
invoke = pg.image.load('images/invoker_invoke.png').convert()
quas = pg.transform.scale(quas, IM_SIZE)
wex = pg.transform.scale(wex, IM_SIZE)
exort = pg.transform.scale(exort, IM_SIZE)
invoke = pg.transform.scale(invoke, IM_SIZE)

zero_rect = exort.get_rect(topleft=(WIDTH // 2, HEIGHT - IM_SIZE[1]))
first_rect = wex.get_rect(topright=(WIDTH // 2, HEIGHT - IM_SIZE[1]))
second_rect = quas.get_rect(topright=first_rect.topleft)
third_rect = invoke.get_rect(topleft=zero_rect.topright)

combination = '333'
comb_cast = {'0': quas, '1': wex, '2': exort}
comb_pos = {'0': second_rect, '1': first_rect, '2': zero_rect}


def draw_combination(_comb):
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
