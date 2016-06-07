#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Step_Record:
    def __init__(self, count):
        """
        :param count: int default 1

        记录走步,根据当前步数,初始值为1
        颜色是加1模2再加1
        用1和0来区分黑白两色
        先走的1是黑
        后奏的是白
        """
        self.count = count
        self.color = (self.count+1) % 2 + 1;



class Step_Record_Chess_Board:
    def __init__(self):
        """
        初始化棋盘记录
        """
        self.count = 1;
        self.records = [[None for i in range(15)] for j in range(15)]
        #初始化棋盘15x15,如果没有落子,棋盘值是None

    def has_record(self, x, y):
        """

        :param x: 棋子横坐标
        :param y: 棋子中坐标
        :return: 返回某处是否已经落子,通过判断棋盘位置是否是None实现
                 如果不是None就是已经落子的了
        """
        return not self.records[x][y] == None

    def insert_record(self, x, y):
        '''

        :param x: 棋子横坐标
        :param y: 棋子纵坐标
        :return: 没有返回值
        和一般的程序不同的是,棋盘上每个坐标都是一个Step_Record对象
        黑子还是白字看属性,这样开销是否大呢
        根据步数落子,步数可以判断是黑子还是白子
        步数加1
        '''
        self.records[x][y] = Step_Record(self.count)
        print '{0}'.format('white' if ((self.count+1) % 2 + 1) == 1 else 'black') ,'< x:', x, ', y:', y,'>'

        self.count += 1;

    def who_to_play(self):
        '''

        :return: 判断谁改走了
        '''
        return (self.count+1) % 2 + 1

    def check_row(self, x, y):
        """
        :param x:
        :param y:
        :return:

        检测行里是否连续的5个子
        """
        if self.has_record(x, y) and self.has_record(x, y+1) and self.has_record(x, y+2) and self.has_record(x, y+3) and self.has_record(x, y+4):
            #判断一个子右侧是否5个连续有子,如果是判断是否连续的黑色或者白色,返回1或者2代表胜利
            if self.records[x][y].color == 1 and self.records[x][y+1].color == 1 and self.records[x][y+2].color == 1 and self.records[x][y+3].color == 1 and self.records[x][y+4].color == 1:
                return 1;

            elif self.records[x][y].color == 2 and self.records[x][y+1].color == 2 and self.records[x][y+2].color == 2 and self.records[x][y+3].color == 2 and self.records[x][y+4].color == 2:
                return 2;

        else:
            return 0;

    def check_col(self, x, y):
        """
        检测列里是否有连续的5个子
        :param x:
        :param y:
        :return:
        """
        if self.has_record(x, y) and self.has_record(x+1, y) and self.has_record(x+2, y) and self.has_record(x+3, y) and self.has_record(x+4, y):

            if self.records[x][y].color == 1 and self.records[x+1][y].color == 1 and self.records[x+2][y].color == 1 and self.records[x+3][y].color == 1 and self.records[x+4][y].color == 1:
                return 1;

            elif self.records[x][y].color == 2 and self.records[x+1][y].color == 2 and self.records[x+2][y].color == 2 and self.records[x+3][y].color == 2 and self.records[x+4][y].color == 2:
                return 2;

        else:
            return 0;

    def check_up(self, x, y):
        '''
        检测/斜线方向是否有连续的子
        :param x:
        :param y:
        :return:
        '''
        if self.has_record(x, y) and self.has_record(x+1, y+1) and self.has_record(x+2, y+2) and self.has_record(x+3, y+3) and self.has_record(x+4, y+4):

            if self.records[x][y].color == 1 and self.records[x+1][y+1].color == 1 and self.records[x+2][y+2].color == 1 and self.records[x+3][y+3].color == 1 and self.records[x+4][y+4].color == 1:
                return 1;

            elif self.records[x][y].color == 2 and self.records[x+1][y+1].color == 2 and self.records[x+2][y+2].color == 2 and self.records[x+3][y+3].color == 2 and self.records[x+4][y+4].color == 2:
                return 2;

        else:
            return 0;

    def check_down(self, x, y):
        '''
        检测\方向是否有连续的子
        :param x:
        :param y:
        :return:
        '''
        if self.has_record(x, y) and self.has_record(x+1, y-1) and self.has_record(x+2, y-2) and self.has_record(x+3, y-3) and self.has_record(x+4, y-4):

            if self.records[x][y].color == 1 and self.records[x+1][y-1].color == 1 and self.records[x+2][y-2].color == 1 and self.records[x+3][y-3].color == 1 and self.records[x+4][y-4].color == 1:
                return 1;

            elif self.records[x][y].color == 2 and self.records[x+1][y-1].color == 2 and self.records[x+2][y-2].color == 2 and self.records[x+3][y-3].color == 2 and self.records[x+4][y-4].color == 2:
                return 2;

        else:
            return 0;


    def check(self):
        '''
        遍历棋盘,检测是否是全部有子
        这里每次都是全面扫描棋盘,实际上可以优化
        初期有很多列是没有落子的所以不必扫描
        :return:
        '''
        for i in range(15):
            for j in range(11):    #没有必要到15,否则会报错的
                result = self.check_row(i, j)
                if result != 0:
                    return result

        for i in range(11):
            for j in range(15):
                result = self.check_col(i, j)
                if result != 0:
                    return result

        for i in range(11):
            for j in range(11):
                result = self.check_up(i, j)
                if result != 0:
                    return result

        for i in range(11):
            for j in range(4, 15):
                result = self.check_down(i, j)
                if result != 0:
                    return result
