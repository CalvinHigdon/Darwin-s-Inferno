#usr/bin/env/python3
import libtcodpy as tcod



#INITIALIZING CONSOLE AND STATING VARIABLES:

SCREEN_WIDTH = 72
SCREEN_HEIGHT = 42
FPS_LIMIT = 30


window_title = "Window Title"
fullscreen = False
tcod.console_set_custom_font("terminal16x16_gr_ro.png",tcod.FONT_LAYOUT_ASCII_INROW | tcod.FONT_TYPE_GREYSCALE)


tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)
tcod.sys_set_fps(FPS_LIMIT)


#MAIN LOOP:

while not tcod.console_is_window_closed():
    tcod.console_flush()