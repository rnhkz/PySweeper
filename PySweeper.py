import random as rand
import pygame as pg
import sys

from game_board import Game_Board

pg.init()

def main():
    rows, cols = 10, 10
    mines = 10

    if len(sys.argv) == 4:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
        mines = int(sys.argv[3])
        if mines > (rows * cols) * .75:
            mines = int((rows * cols) * .1)
            print(f"Mine count too large! Setting to 10% of current board size ({mines}).")
    elif len(sys.argv) > 1:
        print("Wrong amount of arguments! Setting to defaults (10 rows, 10 columns, 10 mines).")

    gb = Game_Board(rows, cols, mines)

    gb_tiles = [pg.image.load('tiles/0.jpg'),
                pg.image.load('tiles/1.jpg'),
                pg.image.load('tiles/2.jpg'),
                pg.image.load('tiles/3.jpg'),
                pg.image.load('tiles/4.jpg'),
                pg.image.load('tiles/5.jpg'),
                pg.image.load('tiles/6.jpg'),
                pg.image.load('tiles/7.jpg'),
                pg.image.load('tiles/8.jpg'),
                pg.image.load('tiles/9.jpg')]
    cover = pg.image.load('tiles/cover.jpg')
    select = pg.image.load('tiles/select.jpg')
    win_text = pg.image.load('tiles/win.png')
    lose_text = pg.image.load('tiles/lose.png')
    
    #Set up game window
    background_colour = (255,255,255)
    (width, height) = (cols*50, rows*50)

    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('PySweeper')
    screen.fill(background_colour)
    pg.display.flip()

    mouse_states = [False, pg.mouse.get_pressed(num_buttons=3)[0]]
    clicked_mine = False
    
    #Game loop
    while 1:
        pg.time.Clock().tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        
        x_pos = 0
        y_pos = 0
        mouse_x, mouse_y = pg.mouse.get_pos()

        for row in range(0, rows):
            x_pos = 0
            for col in range(0, cols):
                if mouse_x > x_pos and mouse_x < x_pos+50 and mouse_y > y_pos and mouse_y < y_pos+50:
                    if(pg.mouse.get_pressed(num_buttons=3)[0]):
                        if gb.map[row][col] == 9:
                            clicked_mine = True
                        gb.get_new_revealed_game_board(row, col)
                    else:
                        screen.blit(select ,(x_pos, y_pos))
                elif gb.is_revealed_map[row][col] == 0:
                    screen.blit(cover ,(x_pos, y_pos))
                else:
                    screen.blit(gb_tiles[gb.map[row][col]], (x_pos, y_pos))
                x_pos+=50
            y_pos+=50
        if clicked_mine:
            screen.blit(lose_text, (50, 100))
        else:
            not_revealed = 0
            for row in gb.is_revealed_map:
                not_revealed += row.count(0)
            if not_revealed == mines:
                screen.blit(win_text, (50, 100))
        pg.display.flip()

if __name__ == "__main__" :
    main()