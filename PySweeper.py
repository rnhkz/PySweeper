import random as rand
import pygame as pg
import sys

from game_board import Game_Board

pg.init()

def main():
    rows, cols, mines = 10, 10, 10
    theme = 'Default'
    print(sys.argv)
    if len(sys.argv) == 5:
        theme = sys.argv[4]
    if len(sys.argv) >= 4:
        rows, cols, mines = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        if mines > (rows * cols) * .75:
            mines = int((rows * cols) * .1)
            print(f"Mine count too large! Setting to 10% of current board size ({mines}).")
    elif len(sys.argv) > 1:
        print("Wrong amount of arguments! Setting to defaults (10 rows, 10 columns, 10 mines).")

    gb = Game_Board(rows, cols, mines)

    gb_tiles = [pg.image.load('Themes/' + theme + '/0.jpg'),
                pg.image.load('Themes/' + theme + '/1.jpg'),
                pg.image.load('Themes/' + theme + '/2.jpg'),
                pg.image.load('Themes/' + theme + '/3.jpg'),
                pg.image.load('Themes/' + theme + '/4.jpg'),
                pg.image.load('Themes/' + theme + '/5.jpg'),
                pg.image.load('Themes/' + theme + '/6.jpg'),
                pg.image.load('Themes/' + theme + '/7.jpg'),
                pg.image.load('Themes/' + theme + '/8.jpg'),
                pg.image.load('Themes/' + theme + '/9.jpg')]
    cover = pg.image.load('Themes/' + theme + '/cover.jpg')
    select = pg.image.load('Themes/' + theme + '/select.jpg')
    flag = pg.image.load('Themes/' + theme + '/flag.jpg')
    win_text = pg.image.load('Themes/' + theme + '/win.png')
    lose_text = pg.image.load('Themes/' + theme + '/lose.png')
    
    #Set up game window
    background_colour = (255,255,255)
    (width, height) = (cols*50, rows*50)

    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('PySweeper')
    screen.fill(background_colour)
    pg.display.flip()

    left_mouse_states = [False, pg.mouse.get_pressed(num_buttons=3)[0]]
    right_mouse_states = [False, pg.mouse.get_pressed(num_buttons=3)[2]]
    clicked_mine = False

    #Game loop
    while 1:
        pg.time.Clock().tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_r:
                gb = Game_Board(rows, cols, mines)
                clicked_mine = False

        x_pos, y_pos = 0, 0
        mouse_x, mouse_y = pg.mouse.get_pos()
        keystate = pg.key.get_pressed()
        left_mouse_states = [left_mouse_states[1], pg.mouse.get_pressed(num_buttons=3)[0]]
        right_mouse_states = [right_mouse_states[1], pg.mouse.get_pressed(num_buttons=3)[2]]
        for row in range(0, rows):
            x_pos = 0
            for col in range(0, cols):
                if mouse_x > x_pos and mouse_x < x_pos+50 and mouse_y > y_pos and mouse_y < y_pos+50:
                    if(right_mouse_states[1]):
                        if(left_mouse_states == [True, False]):
                            if gb.reveal_map[row][col] == 0:
                                flags = 0
                                tiles = []
                                for x in range (row-1, row+2):
                                    for y in range (col-1, col+2):
                                        if min([x,y]) >= 0:
                                            if x < rows and y < cols:
                                                if gb.reveal_map[x][y] == -1:
                                                    flags += 1
                                                tiles.append([x, y])
                                if flags == gb.map[row][col]:
                                    gb.get_new_reveal_map(tiles)
                                else:
                                    print(flags)
                    elif(left_mouse_states == [True, False]):
                        if gb.reveal_map[row][col] == 1:
                            if gb.map[row][col] == 9:
                                clicked_mine = True
                            gb.get_new_reveal_map([[row, col]])
                    elif(right_mouse_states == [True, False]):
                        if gb.reveal_map[row][col] != 0:
                            gb.change_flag(row, col)
                    else:
                        screen.blit(select ,(x_pos, y_pos))
                elif gb.reveal_map[row][col] == -1:
                    screen.blit(flag ,(x_pos, y_pos))
                elif gb.reveal_map[row][col] == 1:
                    screen.blit(cover ,(x_pos, y_pos))
                else:
                    screen.blit(gb_tiles[gb.map[row][col]], (x_pos, y_pos))
                x_pos+=50
            y_pos+=50
        if clicked_mine:
            screen.blit(lose_text, (50, 100))
        else:
            not_revealed = 0
            for row in gb.reveal_map:
                not_revealed += cols - row.count(0)
            if not_revealed == mines:
                screen.blit(win_text, (50, 100))
        pg.display.flip()

if __name__ == "__main__" :
    main()