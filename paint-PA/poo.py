from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class void:
    def iniciarforma(self):
        pass
    def atualizarforma(self,x):
        pass
    def gravarforma(self,x):
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






