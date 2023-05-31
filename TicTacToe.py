import os
import sys
import time

x = [0,1,2,3,4,5,6,7,8] 
clicks = 1

def Xwin():
    os.system('cls')
    print("Wygrał gracz X")
    time.sleep(2)
    sys.exit()
def Owin():
    os.system('cls')
    print("Wygrał gracz O")
    time.sleep(2)
    sys.exit()

def Board():
    os.system('cls')
    print("┌───┬───┬───┐")
    print("│",x[0],"│",x[1],"│",x[2],"│")
    print("├───┼───┼───┤")
    print("│",x[3],"│",x[4],"│",x[5],"│")
    print("├───┼───┼───┤")
    print("│",x[6],"│",x[7],"│",x[8],"│")
    print("└───┴───┴───┘")

def SetPos(num):
    global clicks,i
    for i in x: 
        if i == num:
          if clicks % 2 == 0:
              x[i] = "X"
          else: x[i] = "O"
    clicks += 1
              
def WinCheck():
    if x[0]== "O" and x[4]== "O" and x[8] == "O": #skos1
        return 1
    elif x[6]== "O" and x[4]== "O" and x[2] == "O": #skos2
        return 1
    elif x[0]== "O" and x[1]== "O" and x[2] == "O": #1w
        return 1
    elif x[3]== "O" and x[4]== "O" and x[5] == "O": #2w
        return 1
    elif x[6] == "O" and x[7]== "O" and x[8] == "O": #3w
        return 1
    elif x[0] == "O" and x[3] == "O" and x[6] == "O": #1k
        return 1
    elif x[1] == "O" and x[4] == "O" and x[7] == "O": #2k
        return 1
    elif x[2] == "O" and x[5] == "O" and x[8] == "O": #3k
        return 1
    elif x[0] == "X" and x[4] == "X" and x[8] == "X": #skos1
        return 2
    elif x[6] == "X" and x[4] == "X" and x[2] == "X": #skos2
        return 2
    elif x[0] == "X" and x[1] == "X" and x[2] == "X": #1w
        return 2
    elif x[3] == "X" and x[4] == "X" and x[5] == "X": #2w
        return 2
    elif x[6] == "X" and x[7] == "X" and x[8] == "X": #3w
        return 2
    elif x[0] == "X" and x[3] == "X" and x[6] == "X": #1k
        return 2
    elif x[1] == "X" and x[4] == "X" and x[7] == "X": #2k
        return 2
    elif x[2] == "X" and x[5] == "X" and x[8] == "X": #3k
        return 2

def Game():
    global num
    p = 0
    while p <= 8:
        Board()
        num = int(input("Podaj ruch: "))
        while x[num] == "X" or x[num] == "O":
            os.system('cls')
            Board()
            num = int(input("Podaj ruch: "))
        SetPos(num)
        if WinCheck() == 2:
            Xwin()
        elif WinCheck() == 1:
            Owin()
        p += 1
    sys.exit()
Game()


       