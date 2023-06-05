import random as rand

class Game_Board:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.map = self.generate_map()
        self.reveal_map = [[1 for x in range(cols)] for y in range(rows)]
    
    def generate_map(self):
        temp_map = [[0 for x in range(self.cols)] for y in range(self.rows)]
        # Populate board with mines
        mine_count = 0
        while mine_count < self.mines:
            row = rand.randint(0, self.rows-1)
            col = rand.randint(0, self.cols-1)

            if temp_map[row][col] != 9:
                temp_map[row][col] = 9
                mine_count += 1

        #Determine number of adjacent mines for each tile in the board
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                mine_proximity_count = 0
                if temp_map[row][col] != 9:
                    if row-1 >= 0:
                        if col-1 >= 0:
                            if temp_map[row-1][col-1] == 9:
                                mine_proximity_count += 1
                        if temp_map[row-1][col] == 9:
                            mine_proximity_count += 1
                        if col+1 < self.cols:
                            if temp_map[row-1][col+1] == 9:
                                    mine_proximity_count += 1
                    if col-1 >= 0:
                        if temp_map[row][col-1] == 9:
                            mine_proximity_count += 1
                    if col+1 < self.cols:
                        if temp_map[row][col+1] == 9:
                            mine_proximity_count += 1
                    if row+1 < self.rows:
                        if col-1 >= 0:
                            if temp_map[row+1][col-1] == 9:
                                mine_proximity_count += 1
                        if temp_map[row+1][col] == 9:
                            mine_proximity_count += 1
                        if col+1 < self.cols:
                            if temp_map[row+1][col+1] == 9:
                                mine_proximity_count += 1
                    temp_map[row][col] = mine_proximity_count
        return temp_map

    def get_new_reveal_map(self, row, col):
        stack = [[row, col]]
        while len(stack) > 0:
            cur_tile = stack.pop()
            row=cur_tile[0]
            col=cur_tile[1]
            if self.reveal_map[row][col] == 1:
                if self.map[row][col] == 0:
                    if row-1 >= 0:
                        if col-1 >= 0:
                            stack.append([row-1, col-1])
                        stack.append([row-1, col])
                    if col+1 < self.cols:
                        if row-1 >= 0:
                            stack.append([row-1, col+1])
                        stack.append([row, col+1])
                    if row+1 < self.rows:
                        if col+1 < self.cols:
                            stack.append([row+1, col+1])
                        stack.append([row+1, col])
                    if col-1 >= 0:
                        if row+1 < self.rows:
                            stack.append([row+1, col-1])
                        stack.append([row, col-1])
                    self.reveal_map[row][col] = 0
            if self.reveal_map[row][col] != -1:
                self.reveal_map[row][col] = 0

    def change_flag(self, row, col):
        self.reveal_map[row][col] = self.reveal_map[row][col] * -1