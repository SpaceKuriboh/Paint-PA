from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class void:
    def iniciarforma(self):
        pass
    def atualizarforma(self):
        pass
    def gravarforma(self):
        pass


class Pincel(ABC):

    def __init__(self, canva, xi, yi, xf, yf, outline,expessura, fill= None, temp=None):
        self.canva = canva
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf
        self.outline = outline
        self.expessura = expessura
        self.fill = fill
        self.temp = temp

    @abstractmethod
    def desenhar(self): ...

    def atualizarforma(self,event):
        self.xf = event.x
        self.yf = event.y
        self.canva.delete("True")
        self.temp=True
        self.desenhar()

    def gravarforma(self,event):
        self.xf = event.x
        self.yf = event.y
        self.canva.delete("True")
        self.temp=False
        self.desenhar()

class Poligono:

    def __init__(self,canva,xi,yi,xf,yf,outline,expessura, fill= None):
        self.canva=canva
        self.pontos=[xi,yi]
        self.xi,self.yi,self.xf,self.yf=xi,yi,xf,yf
        self.outline=outline
        self.fill=fill
        self.expessura=expessura
        self.inix,self.iniy=self.xi,self.yi

    def atualizarforma(self,event):
        self.xf = event.x
        self.yf = event.y
        self.canva.delete("True")
        self.desenhar("True")

    def desenhar(self,tag):
        self.canva.create_line(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.outline,
            tags=tag,
            width=self.expessura,
        )

    def marcarponto(self,event):

        if abs(event.x-self.inix)<=8 and abs(event.y-self.iniy)<=8:
            self.canva.delete("True")
            self.canva.delete("true2")
            self.canva.create_polygon(*self.pontos,fill=self.fill, outline=self.outline,width=self.expessura)

            return True
        
        else:
            self.pontos.extend([event.x,event.y])
            self.canva.delete("True")
            self.desenhar("true2")
            self.xi,self.yi=self.xf,self.yf

            return False
        
class Livre(Pincel):

    def desenhar(self):
        self.canva.create_line(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.outline,
            tags=str(self.temp),
            width=self.expessura,
        )

    def atualizarforma(self,event):
        self.xf = event.x
        self.yf = event.y
        self.desenhar()
        self.temp=False
        self.xi, self.yi = self.xf, self.yf


class Reta(Pincel):

    def desenhar(self):
        self.canva.create_line(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.outline,
            tags=str(self.temp),
            width=self.expessura,
        )


class Retangulo(Pincel):

    def desenhar(self):
        self.canva.create_rectangle(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura,
        )


class Oval(Pincel):

    def desenhar(self):
        self.canva.create_oval(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura,
        )


class Circulo(Pincel):

    def desenhar(self):

        raio = ((self.xf - self.xi) ** 2 + (self.yf - self.yi) ** 2) ** 0.5
        self.canva.create_oval(
            self.xi - raio,
            self.yi - raio,
            self.xi + raio,
            self.yi + raio,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
        )