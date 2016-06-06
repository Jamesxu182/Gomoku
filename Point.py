#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Point:

    def __init__(self, x, y):
        '''
        点,生成棋盘上的交点,并计算每个棋子多赢的实际像素坐标
        棋盘坐标和像素坐标的转换
        :param x:
        :param y:
        '''
        self.x = x;
        self.y = y;
        self.pixel_x = 30 + 30 * self.x
        self.pixel_y = 30 + 30 * self.y
