import random as rand
import pygame as pg
import sys

from game_board import Game_Board
from mouse_object import Mouse_Object

pg.init()

def load_tiles(theme, tile_dim, cols, rows):
    # gb_tiles[0:10] = Non-mine proximity tiles
    # gb_tiles[10] = Cover
    # gb_tiles[11] = Select
    # gb_tiles[12] = Flag
    # gb_tiles[13] = Win Sprite
    # gb_tiles[14] = Lost Sprite
    tiles = [pg.image.load('Themes/' + theme + '/0.jpg'),
            pg.image.load('Themes/' + theme + '/1.jpg'),
            pg.image.load('Themes/' + theme + '/2.jpg'),
            pg.image.load('Themes/' + theme + '/3.jpg'),
            pg.image.load('Themes/' + theme + '/4.jpg'),
            pg.image.load('Themes/' + theme + '/5.jpg'),
            pg.image.load('Themes/' + theme + '/6.jpg'),
            pg.image.load('Themes/' + theme + '/7.jpg'),
            pg.image.load('Themes/' + theme + '/8.jpg'),
            pg.image.load('Themes/' + theme + '/9.jpg'),
            pg.image.load('Themes/' + theme + '/cover.jpg'),
            pg.image.load('Themes/' + theme + '/select.jpg'),
            pg.image.load('Themes/' + theme + '/flag.jpg'),
            pg.image.load('Themes/' + theme + '/win.png'),
            pg.image.load('Themes/' + theme + '/lose.png')]
    
    for x in range(len(tiles) -2):
        tiles[x] = pg.transform.smoothscale(tiles[x], (tile_dim, tile_dim))
    tiles[13] = pg.transform.smoothscale(tiles[13], (cols*tile_dim, rows*tile_dim))
    tiles[14] = pg.transform.smoothscale(tiles[14], (cols*tile_dim, rows*tile_dim))

    return tiles


def main():
    rows, cols, mines = 10, 10, 10
    theme = 'Default'
    tile_dim = 50

    if len(sys.argv) == 5:
        theme = sys.argv[4]
    if len(sys.argv) >= 4:
        rows, cols, mines = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        if mines > (rows * cols) * .75:
            mines = int((rows * cols) * .1)
            print(f"Mine count too large! Setting to 10% of current board size ({mines}).")
    elif len(sys.argv) > 1:
        print("Wrong amount of arguments! Setting to defaults (10 rows, 10 columns, 10 mines).")
    
    #Set up game window
    screen = pg.display.set_mode((cols*tile_dim, rows*tile_dim))
    pg.display.set_caption('PySweeper')
    screen.fill((255,255,255))
    pg.display.flip()

    gb = Game_Board(rows, cols, mines)
    gb_tiles = load_tiles(theme, tile_dim, cols, rows)
    m_obj = Mouse_Object()
    clicked_mine = False
    force_update = False

    #Game loop
    while 1:
        pg.time.Clock().tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_r:
                gb = Game_Board(rows, cols, mines)
                clicked_mine = False
                force_update = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_EQUALS and tile_dim < 80:
                tile_dim += 10
                gb_tiles = load_tiles(theme, tile_dim, cols, rows)
                screen = pg.display.set_mode((cols*tile_dim, rows*tile_dim))
                force_update = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_MINUS and tile_dim > 10:
                tile_dim -= 10
                gb_tiles = load_tiles(theme, tile_dim, cols, rows)
                screen = pg.display.set_mode((cols*tile_dim, rows*tile_dim))
                force_update = True

        x_pos, y_pos = 0, 0
        m_obj.update()
        mouse_x, mouse_y = m_obj.mouse_pos_states[1]
        keystate = pg.key.get_pressed()

        if m_obj.has_action() or force_update:
            force_update = False
            for row in range(0, rows):
                x_pos = 0
                for col in range(0, cols):
                    if mouse_x > x_pos and mouse_x < x_pos+tile_dim and mouse_y > y_pos and mouse_y < y_pos+tile_dim:
                        # Right click activated or held
                        if(m_obj.right_mouse_states[1]):
                            # Left click released
                            if(m_obj.left_mouse_states == [True, False]):
                                if gb.reveal_map[row][col] == 0:
                                    flags = 0
                                    tiles = []
                                    for x in range (row-1, row+2):
                                        for y in range (col-1, col+2):
                                            if min([x,y]) >= 0:
                                                if x < rows and y < cols:
                                                    if gb.reveal_map[x][y] == -1:
                                                        flags += 1
                                                    elif gb.map[x][y] == 9:
                                                        clicked_mine = True
                                                    tiles.append([x, y])
                                    if flags == gb.map[row][col]:
                                        gb.get_new_reveal_map(tiles)
                                        force_update = True
                                    else:
                                        clicked_mine = False
                        # Left cick released
                        elif(m_obj.left_mouse_states == [True, False]):
                            if gb.reveal_map[row][col] == 1:
                                if gb.map[row][col] == 9:
                                    clicked_mine = True
                                gb.get_new_reveal_map([[row, col]])
                                force_update = True
                        # Right click released
                        elif(m_obj.right_mouse_states == [True, False]):
                            if gb.reveal_map[row][col] != 0:
                                gb.change_flag(row, col)
                        else:
                            screen.blit(gb_tiles[11] ,(x_pos, y_pos))
                    elif gb.reveal_map[row][col] == -1:
                        screen.blit(gb_tiles[12] ,(x_pos, y_pos))
                    elif gb.reveal_map[row][col] == 1:
                        screen.blit(gb_tiles[10], (x_pos, y_pos))
                    else:
                        screen.blit(gb_tiles[gb.map[row][col]], (x_pos, y_pos))
                    x_pos+=tile_dim
                y_pos+=tile_dim
            if clicked_mine:
                screen.blit(gb_tiles[14], (0,0))
            else:
                not_revealed = 0
                for row in gb.reveal_map:
                    not_revealed += cols - row.count(0)
                if not_revealed == mines:
                    screen.blit(gb_tiles[13], (0,0))
            pg.display.flip()

if __name__ == "__main__" :
    main()