from tkinter import *

root = Tk()
root.title("Addition on the Edge")

def Start():
 global m
 global p1s
 global p2s
 global ns
 import random
 m = random.randint(0, 200)
 p1s = [0]
 p2s = [0]
 ns = [0]

def Reset():
 Start()
 turn['text'] = "Player 1's Turn"
 c['text'] = "0"
 p1p['text'] = "P1: 0"
 p2p['text'] = "P2: 0"
 
Start()

def OnClick(i):
 if (turn['text'] == "Player 1's Turn" or turn['text'] == "Player 2's Turn"):
  n = ns[len(ns)-1]
  p1 = p1s[len(p1s)-1]
  p2 = p2s[len(p2s)-1]
  n += i
  if (n <= m):
   ns.append(n)
   if turn['text'] == "Player 1's Turn":
    p1 += i
    p1s.append(p1)
    p1p['text'] = "P1: " + str(p1)
    turn['text'] = "Player 2's Turn"
   elif turn['text'] == "Player 2's Turn":
    p2 += i
    p2s.append(p2)
    p2p['text'] = "P2: " + str(p2)
    turn['text'] = "Player 1's Turn"
   c['text'] = str(n)
  elif (n > m):
   c['text'] = str(n) + "/" + str(m)
   if turn['text'] == "Player 1's Turn":
    p1 -= i
    p1s.append(p1)
    p1p['text'] = "P1: " + str(p1)
   elif turn['text'] == "Player 2's Turn":
    p2 -= i
    p2s.append(p2)
    p2p['text'] = "P2: " + str(p2)
   if (p1 > p2): turn['text'] = "Player 1 Wins"
   elif (p1 < p2): turn['text'] = "Player 2 Wins"
   else: turn['text'] = "DRAW"
 elif (turn['text'] == "Player 1 Wins" or turn['text'] == "Player 2 Wins" or turn['text'] == "DRAW"): pass
  
turn = Label(root, text="Player 1's Turn")
turn.grid(row=0, columnspan=6)
b0 = Button(root, text="1", command=lambda:OnClick(1))
b0.grid(row=3, column=0)
b1 = Button(root, text="2", command=lambda:OnClick(2))
b1.grid(row=3, column=1)
b2 = Button(root, text="3", command=lambda:OnClick(3))
b2.grid(row=3, column=2)
b3 = Button(root, text="4", command=lambda:OnClick(4))
b3.grid(row=3, column=3)
b4 = Button(root, text="5", command=lambda:OnClick(5))
b4.grid(row=3, column=4)
b5 = Button(root, text="6", command=lambda:OnClick(6))
b5.grid(row=4, column=0)
b6 = Button(root, text="7", command=lambda:OnClick(7))
b6.grid(row=4, column=1)
b7 = Button(root, text="8", command=lambda:OnClick(8))
b7.grid(row=4, column=2)
b8 = Button(root, text="9", command=lambda:OnClick(9))
b8.grid(row=4, column=3)
b9 = Button(root, text="10", command=lambda:OnClick(10))
b9.grid(row=4, column=4)
reset = Button(root, text="Reset", command=Reset)
reset.grid(row=3, column=5)
p1p = Label(root, text="P1: 0")
p1p.grid(row=1, columnspan=2)
c = Label(root, text="0")
c.grid(row=1, column=2, columnspan=2)
p2p = Label(root, text="P2: 0")
p2p.grid(row=1, column=4, columnspan=2)
entry = Entry(root)
entry.grid(row=2, columnspan=6)

root.mainloop()
