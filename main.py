import pygame as pg
from random import choice, randint
from constants import *
from imgs import *

ticks = 0
spawn_delta = 100
clock = pg.time.Clock()


def convert_ticks(t):
    t %= 1000
    t += 1
    return t


def spawn_spell():
    global spawn_delta
    if ticks % spawn_delta == 0:
        if spawn_delta > 50:
            spawn_delta -= 10
        spell = choice(spells)
        curr_rect = spell.get_rect(bottomleft=(randint(0, WIDTH - IM_SIZE[0]), -10))
        spells_queue.append((spell, curr_rect))


def move_spells():
    for _i, spell in enumerate(spells_queue):
        spell[1].bottom += VEL * dt
        if spell[1].top > HEIGHT:
            spells_queue.pop(_i)


def draw_spells():
    for _i, spell in enumerate(spells_queue):
        win.blit(spell[0], spell[1])


def check_cast():
    for _i, spell in enumerate(spells_queue):
        if combination == spells_to_spheres[spell[0]]:
            spells_queue.pop(_i)
            return


def draw_combination(_comb):
    comb_cast = {'q': quas, 'w': wex, 'e': exort}
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

spells = (alacrity, meteor, cold_snap, blast, emp, forge, ghost_walk,
          ice_wall, sun_strike, tornado)
spheres_combinations = ('wwe', 'eew', 'qqq', 'qwe', 'www', 'eeq', 'qqw',
                        'qqe', 'eee', 'wwq')

spheres_to_spells = {spheres_combinations[i]: spells[i] for i in range(len(spells))}
spells_to_spheres = {spells[i]: spheres_combinations[i] for i in range(len(spells))}

spells_queue = []

print(*spells_to_spheres.items(), sep='\n')

run = True
while run:
    win.fill(bgColor)

    dt = clock.tick(60) / 1000
    ticks = convert_ticks(ticks)

    pg.key.set_repeat(0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
                break
            elif event.key == pg.K_q:
                combination = combination[1:] + 'q'
            elif event.key == pg.K_w:
                combination = combination[1:] + 'w'
            elif event.key == pg.K_e:
                combination = combination[1:] + 'e'
            elif event.key == pg.K_r:
                check_cast()

    # print(combination)
    spawn_spell()
    move_spells()

    draw_spells()
    draw_combination(combination)

    pg.display.update()

pg.quit()
