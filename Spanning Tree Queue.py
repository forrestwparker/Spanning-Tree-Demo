# Created by:
# Forrest Parker
# 10/20/2016
#
# Version 0.8
# Last Edit: 10/23/2016
#
# Written for Python 3

from tkinter import *
from random import randrange
from time import sleep

class Game:

    def __init__(self, master):

        self.makeboardarray()
        self.makeboardwindow2(master)

    # Begin methods

    def makeboardarray(self):
        self.board = []
        for i in range(0,25):
            self.board.append([])
            for j in range(0,25):
                self.board[i].append(0)
        highest = 625
        for mines in range(0,75):
            place = randrange(0,highest)
            selector = -1
            while place > 0:
                selector += 1
                j = selector % 25
                i = int((selector - j)/25)
                if self.board[i][j] != -1:
                    place -= 1
            self.board[i][j] = -1
            highest -= 1

    def makeboardwindow2(self,master):
        self.mainframe = Frame(master, bd = 10, bg = "black")
        self.mainframe.pack()
        self.canvasarray = []
        for i in range(0,25):
            for j in range(0,25):
                pos = 25*i+j
                self.canvasarray.append(Canvas(self.mainframe,
                                                  bg = "pink",
                                                  bd = 0,
                                                  cursor = "arrow",
                                                  width = 20,
                                                  height = 20))
                self.canvasarray[pos].create_text((13,13), text = self.fillstring(i,j))
                self.canvasarray[pos].grid(row = i, column = j, sticky = '', padx = 0, pady = 0, ipadx = 0, ipady = 0)
                self.canvasarray[pos].bind("<Button-1>", self.clickedsquare)

    def clickedsquare(self, event):
        pos = self.canvasarray.index(event.widget)
        col = pos % 25
        row = int((pos - col)/25)
        checkthese = [[row,col]]
        self.board[row][col] += 100
        while len(checkthese) > 0:
            row = checkthese[0][0]
            col = checkthese[0][1]
            checkthese.remove([row,col])
            pos = 25*row+col
            self.canvasarray[pos].unbind("<Button-1>")
            if self.board[row][col] == 100:
                self.canvasarray[pos].config(bg = "green")
            elif self.board[row][col] == 99:
                self.canvasarray[pos].config(bg = "red")
            else:
                self.canvasarray[pos].config(bg = "blue")
            self.mainframe.update()
            #sleep(0.1)
            if self.board[row][col] == 100:
                for i in range(max(0,row-1), min(25,row+2)):
                    for j in range(max(0,col-1), min(25,col+2)):
                        if not self.board[i][j] > 50:
                            self.board[i][j] += 100
                            checkthese.append([i,j])
                            self.canvasarray[25*i+j].config(bg = "yellow")
                            self.mainframe.update()
                            #sleep(0.1)

    def fillstring(self, row, col):
        if self.board[row][col] != -1:
            for i in range(max(0,row-1),min(25,row+2)):
                for j in range(max(0,col-1),min(25,col+2)):
                    if self.board[i][j] == -1:
                        self.board[row][col] += 1
        if self.board[row][col] == -1:
            string = "X"
        elif self.board[row][col] == 0:
            string = ""
        else:
            string = str(self.board[row][col])
        return string

        

rootWindow = Tk()
minesweeper = Game(rootWindow)
