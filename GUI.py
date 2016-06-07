#!/usr/bin/env python
#-*- coding: utf-8 -*-

import Tkinter
import math
import Point
import Record

class Chess_Board_Canvas(Tkinter.Canvas):
    #棋盘绘图板,继承自Tkinter.Canvas类
    def __init__(self, master=None, height=0, width=0):
        '''
        棋盘类初始化
        :param master: 画到那个对象
        :param height: 棋盘的高度
        :param width: 棋盘的宽度
        '''
        Tkinter.Canvas.__init__(self, master, height=height, width=width)
        self.step_record_chess_board = Record.Step_Record_Chess_Board()
        #初始化计步器对象
        self.init_chess_board_points()    #画点
        self.init_chess_board_canvas()    #绘制棋盘

    def init_chess_board_points(self):
        '''
        生成各个棋盘点,根据棋盘坐标生成像素表座
        并且保存到 chess_board_points 属性
        :return:
        '''
        self.chess_board_points = [[None for i in range(15)] for j in range(15)]

        for i in range(15):
            for j in range(15):
                self.chess_board_points[i][j] = Point.Point(i, j); #棋盘坐标向像素坐标转化

    def init_chess_board_canvas(self):
        '''
        初始化棋盘
        :return:
        '''

        for i in range(15):  #绘制竖线
            self.create_line(self.chess_board_points[i][0].pixel_x, self.chess_board_points[i][0].pixel_y, self.chess_board_points[i][14].pixel_x, self.chess_board_points[i][14].pixel_y)

        for j in range(15):  #绘制横线
            self.create_line(self.chess_board_points[0][j].pixel_x, self.chess_board_points[0][j].pixel_y, self.chess_board_points[14][j].pixel_x, self.chess_board_points[14][j].pixel_y)

        for i in range(15):  #绘制椭圆,但是这个功能似乎是要加强交点的视觉效果,但是效果一般,视错觉没有出现
            for j in range(15):
                r = 1
                self.create_oval(self.chess_board_points[i][j].pixel_x-r, self.chess_board_points[i][j].pixel_y-r, self.chess_board_points[i][j].pixel_x+r, self.chess_board_points[i][j].pixel_y+r);

    def click1(self, event): #为何是click1因为关键字重复
        '''
        侦听鼠标事件,根据鼠标的位置判断落点
        :param event:
        :return:
        '''
        for i in range(15):
            for j in range(15):
                square_distance = math.pow((event.x - self.chess_board_points[i][j].pixel_x), 2) + math.pow((event.y - self.chess_board_points[i][j].pixel_y), 2)
                #计算鼠标的位置和点的距离
                #距离小于14的点
                #这里其实有更优化的做法就是根据鼠标的位置计算点
                #pyganme开发里面似乎有这个算法

                if (square_distance <= 200) and (not self.step_record_chess_board.has_record(i, j)): #距离小于14并且没有落子
                    if self.step_record_chess_board.who_to_play() == 1:
                        #若果根据步数判断是奇数次,那么白下
                        self.create_oval(self.chess_board_points[i][j].pixel_x-10, self.chess_board_points[i][j].pixel_y-10, self.chess_board_points[i][j].pixel_x+10, self.chess_board_points[i][j].pixel_y+10, fill='red')

                    elif self.step_record_chess_board.who_to_play() == 2:
                        self.create_oval(self.chess_board_points[i][j].pixel_x-10, self.chess_board_points[i][j].pixel_y-10, self.chess_board_points[i][j].pixel_x+10, self.chess_board_points[i][j].pixel_y+10, fill='green')

                    self.step_record_chess_board.insert_record(i, j)
                    #插入落子数据,落子最多225,这个程序没有实现AI

                    result = self.step_record_chess_board.check()
                    #判断是否有五子连珠


                    if result == 1:
                        self.create_text(240, 550, text='the white wins')
                        #解除鼠标左键绑定
                        self.unbind('<Button-1>')
                        # """Unbind for this widget for event SEQUENCE  the
                        #     function identified with FUNCID."""

                    elif result == 2:
                        self.create_text(240, 550, text='the black wins')
                        #解除鼠标左键绑定
                        self.unbind('<Button-1>')


class Chess_Board_Frame(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.create_widgets()

    def create_widgets(self):
        self.chess_board_label_frame = Tkinter.LabelFrame(self, text="Chess Board", padx=5, pady=5)
        self.chess_board_canvas = Chess_Board_Canvas(self.chess_board_label_frame, height=600, width=480)

        self.chess_board_canvas.bind('<Button-1>', self.chess_board_canvas.click1)

        self.chess_board_label_frame.pack();
        self.chess_board_canvas.pack();
