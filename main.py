from tkinter import *
from tkinter.ttk import Combobox


def iniciarforma(event):
    global xi,yi
    xi=event.x
    yi=event.y
def atualizarforma(event):
    global xi,yi,xf,yf,opcoes
    xf=event.x
    yf=event.y
    mesa.delete("temp")
    if opcoes.get()=="linha":
        mesa.create_line(xi,yi,xf,yf, fill=coresforma.get(),tags="temp",width=3)
    elif opcoes.get()=="retangulo":
        mesa.create_rectangle(xi, yi, xf, yf,fill=coresforma.get(), outline=coreslinha.get(),tags="temp",width=3)
    elif opcoes.get()=="circulo":
        mesa.create_oval(xi, yi, xf, yf, tags="temp",fill=coresforma.get(), outline=coreslinha.get(),width=3)
def gravarforma(event):
    global xi, yi, xf, yf
    mesa.delete("temp")
    if opcoes.get() == "linha":
        mesa.create_line(xi, yi, xf, yf,fill=coresforma.get(),width=3)
    elif opcoes.get() == "retangulo":
        mesa.create_rectangle(xi, yi, xf, yf,fill=coresforma.get(), outline=coreslinha.get(),width=3)
    elif opcoes.get()=="circulo":
        mesa.create_oval(xi, yi, xf, yf,fill=coresforma.get(), outline=coreslinha.get(),width=3)
janela=Tk()
janela.title("Paint 2.0 ULTRA BLASTER SUPER EXTRA CHEDDAR PLUS PLUS PLUS")
opcoes= Combobox(janela,values=["linha","retangulo","circulo"])
coreslinha= Combobox(janela,values=["blue","red","green","yellow","purple","pink","black"])
coresforma= Combobox(janela,values=["blue","red","green","yellow","purple","pink","black"])
opcoes.set("linha")
coreslinha.set("black")
coresforma.set("black")
opcoes.pack()
coreslinha.pack()
coresforma.pack()
xi,xf,yi,yf=0,0,0,0
mesa=Canvas(janela,width=800,height=500)
mesa.pack()
mesa.bind('<ButtonPress-1>', iniciarforma)
mesa.bind('<B1-Motion>', atualizarforma)
mesa.bind('<ButtonRelease-1>', gravarforma)
janela.mainloop()