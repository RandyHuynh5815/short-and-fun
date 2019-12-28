from tkinter import *

result = ""

root = Tk()
root.title("Interest Calculator")
t = IntVar()
t.set(None)
f = StringVar()
f.set(None)

def OnClick():
 pp = float(p.get())
 rr = float(r.get())
 yy = float(y.get())
 rr /= 100
 if f.get() == "A": ff = 1
 elif f.get() == "B": ff = 2
 elif f.get() == "C": ff = 4
 elif f.get() == "D": ff = 12
 elif f.get() == "E": ff = 24
 elif f.get() == "F": ff = 48
 elif f.get() == "G": ff = 365
 if t.get() == 0:
  a = "$" + str(round(pp*(1+(ff*rr*yy)), 2))
  out['text'] = a
 if t.get() == 1:
  a = "$" + str(round(pp*((1+(rr/ff))**(ff*yy)), 2))
  out['text'] = a

tl = Label(root, text="Interest type: ")
tl.grid(row=0, column=0)
pl = Label(root, text="Principal/Starting value: ")
pl.grid(row=0, column=1)
rl = Label(root, text="Interest rate (in %): ")
rl.grid(row=0, column=2)
fl = Label(root, text="Frequency of interest applied per year: ")
fl.grid(row=0, column=3)
yl = Label(root, text="Time in years: ")
yl.grid(row=0, column=4)
b = Button(root, text="Go!", command=OnClick)
b.grid(row=0, column=5)
out = Label(root, text="")
out.grid(row=9, columnspan=6)

tone = Radiobutton(root, text="Simple", variable=t, value=0)
tone.grid(row=1, column=0)
t2 = Radiobutton(root, text="Compound", variable=t, value=1)
t2.grid(row=2, column=0)

p = Entry(root)
p.grid(row=1, column=1)

r = Entry(root)
r.grid(row=1, column=2)

fone = Radiobutton(root, text="Annually", variable=f, value="A")
fone.grid(row=1, column=3)
f2 = Radiobutton(root, text="Semi-Annually", variable=f, value="B")
f2.grid(row=2, column=3)
f3 = Radiobutton(root, text="Quarterly", variable=f, value="C")
f3.grid(row=3, column=3)
f4 = Radiobutton(root, text="Monthly", variable=f, value="D")
f4.grid(row=4, column=3)
f5 = Radiobutton(root, text="Semi-Monthly", variable=f, value="E")
f5.grid(row=5, column=3)
f6 = Radiobutton(root, text="Weekly", variable=f, value="F")
f6.grid(row=6, column=3)
f7 = Radiobutton(root, text="Daily", variable=f, value="G")
f7.grid(row=7, column=3)

y = Entry(root)
y.grid(row=1, column=4)

lout = Label(root, text="You now have ")
lout.grid(row=8, columnspan=6)            

root.mainloop()
