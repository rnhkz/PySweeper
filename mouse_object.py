import pygame as pg

class Mouse_Object:
    def __init__(self):
        self.left_mouse_states = [False, pg.mouse.get_pressed(num_buttons=3)[0]]
        self.right_mouse_states = [False, pg.mouse.get_pressed(num_buttons=3)[2]]
        self.mouse_pos_states = [(0,0), (-1,-1)]

    def update(self):
        self.mouse_pos_states = [self.mouse_pos_states[1], pg.mouse.get_pos()]
        self.left_mouse_states = [self.left_mouse_states[1], pg.mouse.get_pressed(num_buttons=3)[0]]
        self.right_mouse_states = [self.right_mouse_states[1], pg.mouse.get_pressed(num_buttons=3)[2]]

    def has_action(self):
        return (self.mouse_pos_states[0] != self.mouse_pos_states[1] or
                self.left_mouse_states[0] != self.left_mouse_states[1] or
                self.right_mouse_states[0] != self.right_mouse_states[1])