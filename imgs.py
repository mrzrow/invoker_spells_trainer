import pygame as pg
from constants import *

pg.init()
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Example')
pg.display.flip()

quas = pg.image.load('images/invoker_quas.png').convert()
wex = pg.image.load('images/invoker_wex.png').convert()
exort = pg.image.load('images/invoker_exort.png').convert()
invoke = pg.image.load('images/invoker_invoke.png').convert()
alacrity = pg.image.load('images/invoker_alacrity.png').convert()
meteor = pg.image.load('images/invoker_chaos_meteor.png').convert()
cold_snap = pg.image.load('images/invoker_cold_snap.png').convert()
blast = pg.image.load('images/invoker_deafening_blast.png').convert()
emp = pg.image.load('images/invoker_emp.png').convert()
forge = pg.image.load('images/invoker_forge_spirit.png').convert()
ghost_walk = pg.image.load('images/invoker_ghost_walk.png').convert()
ice_wall = pg.image.load('images/invoker_ghost_walk.png').convert()
sun_strike = pg.image.load('images/invoker_sun_strike.png').convert()
tornado = pg.image.load('images/invoker_tornado.png').convert()

quas = pg.transform.scale(quas, IM_SIZE)
wex = pg.transform.scale(wex, IM_SIZE)
exort = pg.transform.scale(exort, IM_SIZE)
invoke = pg.transform.scale(invoke, IM_SIZE)

zero_rect = exort.get_rect(topleft=(WIDTH // 2, HEIGHT - IM_SIZE[1]))
first_rect = wex.get_rect(topright=(WIDTH // 2, HEIGHT - IM_SIZE[1]))
second_rect = quas.get_rect(topright=first_rect.topleft)
third_rect = invoke.get_rect(topleft=zero_rect.topright)
