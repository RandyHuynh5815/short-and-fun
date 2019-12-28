from tkinter import *

root = Tk()
root.title("Bomb Game")

def Start():
 global dc
 import random
 d1 = random.randint(1, 5)
 d2 = random.randint(6, 10)
 d3 = random.randint(11, 15)
 d4 = random.randint(16, 20)
 d5 = random.randint(20, 25)
 dc = [d1, d2, d3, d4, d5]
def Reset():
 import random
 out['text'] = "ALIVE"
 out['background']="green"
 r['text'] = ""
 p['text'] = "Points: 0"
 dc = []
 d1 = random.randint(1, 5)
 d2 = random.randint(6, 10)
 d3 = random.randint(11, 15)
 d4 = random.randint(16, 20)
 d5 = random.randint(20, 25)
 dc.append(d1)
 dc.append(d2)
 dc.append(d3)
 dc.append(d4)
 dc.append(d5)
 global d
 d = dc

Start()
global d
d = dc

def OnClick(obj):
 if (out['text'] == "ALIVE" and out['background'] == "green"):
  if (obj == 1):
   if obj in d:
    out['text'] = "DEAD!"
    out['background'] = "red"
    r['text'] = d
   else: d.append(1)
  if (obj == 2):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(2)
  if (obj == 3):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(3)
  if (obj == 4):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(4)
  if (obj == 5):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(5)
  if (obj == 6):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(6)
  if (obj == 7):
   if obj in d:
    out['text'] = "DEAD!"
    out['background'] = "red"
    r['text'] = d
   else: d.append(7)
  if (obj == 8):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(8)
  if (obj == 9):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(9)
  if (obj == 10):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(10)
  if (obj == 11):
   if obj in d:
    out['text'] = "DEAD!"
    out['background'] = "red"
    r['text'] = d
   else: d.append(11)
  if (obj == 12):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(12)
  if (obj == 13):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(13)
  if (obj == 14):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(14)
  if (obj == 15):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(15)
  if (obj == 16):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(16)
  if (obj == 17):
   if obj in d:
    out['text'] = "DEAD!"
    out['background'] = "red"
    r['text'] = d
   else: d.append(17)
  if (obj == 18):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(18)
  if (obj == 19):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(19)
  if (obj == 20):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(20)
  if (obj == 21):
   if obj in d:
    out['text'] = "DEAD!"
    out['background'] = "red"
    r['text'] = d
   else: d.append(21)
  if (obj == 22):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(22)
  if (obj == 23):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(23)
  if (obj == 24):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(24)
  if (obj == 25):
   if obj in d:
    out['text'] = "DEAD!"
    out['background']= "red"
    r['text'] = d
   else: d.append(25)
  p['text'] = "Points: " + str((len(d)-5)*5)
 else: pass
 
out = Label(root, text="ALIVE", background="green")
out.grid(row=1, columnspan=4)
b = Button(root, text="Reset", command=Reset)
b.grid(row=1, column=4)
r = Label(root, text="")
r.grid(row=7, columnspan=5)
p = Label(root, text="Points: " + str((len(d)-5)*5))
p.grid(row=0, columnspan=5)
b1 = Button(root, text="1", command=lambda:OnClick(1))
b1.grid(row=2, column=0)
b2 = Button(root, text="2", command=lambda:OnClick(2))
b2.grid(row=2, column=1)
b3 = Button(root, text="3", command=lambda:OnClick(3))
b3.grid(row=2, column=2)
b4 = Button(root, text="4", command=lambda:OnClick(4))
b4.grid(row=2, column=3)
b5 = Button(root, text="5", command=lambda:OnClick(5))
b5.grid(row=2, column=4)
b6 = Button(root, text="6", command=lambda:OnClick(6))
b6.grid(row=3, column=0)
b7 = Button(root, text="7", command=lambda:OnClick(7))
b7.grid(row=3, column=1)
b8 = Button(root, text="8", command=lambda:OnClick(8))
b8.grid(row=3, column=2)
b9 = Button(root, text="9", command=lambda:OnClick(9))
b9.grid(row=3, column=3)
b10 = Button(root, text="10", command=lambda:OnClick(10))
b10.grid(row=3, column=4)
b11 = Button(root, text="11", command=lambda:OnClick(11))
b11.grid(row=4, column=0)
b12 = Button(root, text="12", command=lambda:OnClick(12))
b12.grid(row=4, column=1)
b13 = Button(root, text="13", command=lambda:OnClick(13))
b13.grid(row=4, column=2)
b14 = Button(root, text="14", command=lambda:OnClick(14))
b14.grid(row=4, column=3)
b15 = Button(root, text="15", command=lambda:OnClick(15))
b15.grid(row=4, column=4)
b16 = Button(root, text="16", command=lambda:OnClick(16))
b16.grid(row=5, column=0)
b17 = Button(root, text="17", command=lambda:OnClick(17))
b17.grid(row=5, column=1)
b18 = Button(root, text="18", command=lambda:OnClick(18))
b18.grid(row=5, column=2)
b19 = Button(root, text="19", command=lambda:OnClick(19))
b19.grid(row=5, column=3)
b20 = Button(root, text="20", command=lambda:OnClick(20))
b20.grid(row=5, column=4)
b21 = Button(root, text="21", command=lambda:OnClick(21))
b21.grid(row=6, column=0)
b22 = Button(root, text="22", command=lambda:OnClick(22))
b22.grid(row=6, column=1)
b23 = Button(root, text="23", command=lambda:OnClick(23))
b23.grid(row=6, column=2)
b24 = Button(root, text="24", command=lambda:OnClick(24))
b24.grid(row=6, column=3)
b25 = Button(root, text="25", command=lambda:OnClick(25))
b25.grid(row=6, column=4)

root.mainloop()



 
