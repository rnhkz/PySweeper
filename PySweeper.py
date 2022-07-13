import random as rand
import pygame as pg
import sys

pg.init()

def get_new_revealed_game_board(gb, gb_is_revealed, row, col, rows, columns):
    stack = [[row, col]]
    while len(stack) > 0:
        cur_tile = stack.pop()
        row=cur_tile[0]
        col=cur_tile[1]
        if gb_is_revealed[row][col] == 0:
            if gb[row][col] == 0:
                if row-1 >= 0:
                    if col-1 >= 0:
                        stack.append([row-1, col-1])
                    stack.append([row-1, col])
                if col+1 < columns:
                    if row-1 >= 0:
                        stack.append([row-1, col+1])
                    stack.append([row, col+1])
                if row+1 < rows:
                    if col+1 < columns:
                        stack.append([row+1, col+1])
                    stack.append([row+1, col])
                if col-1 >= 0:
                    if row+1 < rows:
                        stack.append([row+1, col-1])
                    stack.append([row, col-1])
                gb_is_revealed[row][col] = 1
        gb_is_revealed[row][col] = 1
    return gb_is_revealed

def main():
    size = rows, columns = 10, 10
    game_board = [[0 for x in range(rows)] for y in range(columns)]
    game_board_is_revealed = [[0 for x in range(rows)] for y in range(columns)]
    game_board_map = [  pg.image.load('tiles/0.jpg'),
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

    # Populate board with mines
    mine_count = 0
    while mine_count < 10:
        x = rand.randint(0, rows-1)
        y = rand.randint(0, columns-1)
        if game_board[x][y] != 9:
            game_board[x][y] = 9
            mine_count += 1
    
    #Determine number of adjacent mines for each tile in the board
    for row in range(0, rows):
        for column in range(0, columns):
            mine_proximity_count = 0
            if game_board[row][column] != 9:
                if row-1 >= 0:
                    if column-1 >= 0:
                        if game_board[row-1][column-1] == 9:
                            mine_proximity_count += 1
                    if game_board[row-1][column] == 9:
                        mine_proximity_count += 1
                    if column+1 < columns:
                        if game_board[row-1][column+1] == 9:
                                mine_proximity_count += 1
                if column-1 >= 0:
                    if game_board[row][column-1] == 9:
                        mine_proximity_count += 1
                if column+1 < columns:
                    if game_board[row][column+1] == 9:
                        mine_proximity_count += 1
                if row+1 < rows:
                    if column-1 >= 0:
                        if game_board[row+1][column-1] == 9:
                            mine_proximity_count += 1
                    if game_board[row+1][column] == 9:
                        mine_proximity_count += 1
                    if column+1 < columns:
                        if game_board[row+1][column+1] == 9:
                            mine_proximity_count += 1
                game_board[row][column] = mine_proximity_count
    
    #Set up game window
    background_colour = (255,255,255)
    (width, height) = (rows*50, columns*50)

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
            for column in range(0, columns):
                if mouse_x > x_pos and mouse_x < x_pos+50 and mouse_y > y_pos and mouse_y < y_pos+50:
                    if(pg.mouse.get_pressed(num_buttons=3)[0]):
                        if game_board[row][column] == 9:
                            clicked_mine = True
                        game_board_is_revealed = get_new_revealed_game_board(game_board, game_board_is_revealed, row, column, rows, columns)
                    else:                  
                        screen.blit(select ,(x_pos, y_pos))
                elif game_board_is_revealed[row][column] == 0:
                    screen.blit(cover ,(x_pos, y_pos))
                else:
                    screen.blit(game_board_map[game_board[row][column]], (x_pos, y_pos))
                x_pos+=50
            y_pos+=50
        if clicked_mine:
            screen.blit(lose_text, (50, 100))
        else:
            not_revealed = 0
            for row in game_board_is_revealed:
                not_revealed += row.count(0)
            if not_revealed == 10:
                screen.blit(win_text, (50, 100))
        pg.display.flip()

if __name__ == "__main__" :
    main()