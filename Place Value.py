import tkinter

def PlaceWork(s):
 s1 = []
 for i in range(len(s)):
   s1.append(s[i])
 pv = []
 for i in range(len(s1)):
  pv.append((int(s1[i]))*(10**((len(s1)-i)-1)))
 s = str(pv[0]) + " + "
 for i in range((len(pv))-1):
  s += str(pv[i+1]) + " + "
 s=s.split()
 s[-1]=""
 o = ""
 for i in range(len(s)):
  o += s[i] + " "
 out['text'] = o

def Place():
 s = e.get()
 PlaceWork(s)

def PlaceException():
 try: Place()
 except Exception:
  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            "0","1","2","3","4","5","6","7","8","9"]
  s = e.get()
  l = []
  for i in s:
   l.append(i)
   for i in l:
    if i not in digits:
     l.remove(i)
  s = ""
  for i in range(len(l)):
   l[i] = str(l[i])
   s += l[i]
  PlaceWork(s)

root = tkinter.Tk()
root.title("Place Seperator")
l = tkinter.Label(root, text="Enter an integer: ")
l.grid(row=0, column=0)
e = tkinter.Entry(root)
e.grid(row=0, column=1)
b = tkinter.Button(root, text="Go!", command=PlaceException)
b.grid(row=0, column=2)
out = tkinter.Label(root, text="")
out.grid(row=1, columnspan=3)

root.mainloop()
