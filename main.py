#!/usr/bin/env python
#-*- coding: utf-8 -*-

import GUI
import Tkinter

if __name__ == '__main__':
    window = Tkinter.Tk()
    gui_chess_board = GUI.Chess_Board_Frame(window)
    gui_chess_board.pack()
    window.mainloop()
