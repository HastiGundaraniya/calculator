from tkinter import* # type: ignore

def onClick(event):
    
    text = event.widget.cget('text')
    print("text == ",text)
    if text == '=':
        ans=v.get()
        sum = eval(ans)
        value.set(sum)
        v.update()
    elif text == 'C':
        value.set('')
    elif text == '<-':
        ans=v.get()
        ans_l=list(ans)
        ans_l.pop()
        new=''.join(ans_l)
        value.set(new)
        v.update()
    else:
        ans = v.get()
        value.set(ans+text)
        v.update()
    

window = Tk()
window.geometry("180x400")
window.maxsize(250,400)
window.minsize(250,400)

l = Label(text="*--CALCULATER--*")
l.place(x=67,y=10)

value = StringVar()
v = Entry(textvariable=value)
v.place(x=60,y=55)

back = Button(text="<-")
back.place(x=170,y=140)
back.bind("<Button-1>",onClick)

a = Button(text="7")
a.place(x=50,y=180)
a.bind("<Button-1>",onClick)

b = Button(text="8")
b.place(x=90,y=180)
b.bind("<Button-1>",onClick)

c = Button(text="9")
c.place(x=130,y=180)
c.bind("<Button-1>",onClick)

d = Button(text="+")
d.place(x=170,y=180)
d.bind("<Button-1>",onClick)

e = Button(text="4")
e.place(x=50,y=220)
e.bind("<Button-1>",onClick)

f = Button(text="5")
f.place(x=90,y=220)
f.bind("<Button-1>",onClick)

g = Button(text="6")
g.place(x=130,y=220)
g.bind("<Button-1>",onClick)

h = Button(text="-")
h.place(x=170,y=220)
h.bind("<Button-1>",onClick)

i = Button(text="1")
i.place(x=50,y=260)
i.bind("<Button-1>",onClick)

j = Button(text="2")
j.place(x=90,y=260)
j.bind("<Button-1>",onClick)

k = Button(text="3")
k.place(x=130,y=260)
k.bind("<Button-1>",onClick)

m = Button(text="*")
m.place(x=170,y=260)
m.bind("<Button-1>",onClick)

n = Button(text="C")
n.place(x=50,y=300)
n.bind("<Button-1>",onClick)

o = Button(text="0")
o.place(x=90,y=300)
o.bind("<Button-1>",onClick)

p = Button(text="=")
p.place(x=130,y=300)
p.bind("<Button-1>",onClick)

q = Button(text="/")
q.place(x=170,y=300)
q.bind("<Button-1>",onClick)

window.mainloop()