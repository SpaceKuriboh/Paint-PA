from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class Void:
    def __init__(self):
        self.caminho=None
        self.figuras=None
    def iniciar_forma(self,controller, event):
        pass
    def atualizar_forma(self,tipo,controller,event):
        pass
    def gravar_forma(self,controller,event):
        pass
    def verificarpoligono(self):
        pass
    def desenhar(self):
        pass
    def mudar_controlador(self):
        pass
    def construirtudo(self):
        pass

class Pincel(ABC):

    def __init__(self, canva, lista, outline, expessura, figuras=None, fill=None, temp=None):
        self.canva = canva
        self.xi = lista[0]
        self.yi = lista[1]
        self.xf = lista[2]
        self.yf = lista[3]
        self.figuras=figuras
        self.outline = outline
        self.expessura = expessura
        self.fill = fill
        self.temp = temp


class Poligono:

    def __init__(self, canva, lista, outline, expessura, fill=None, temp=None,figuras=None):
        self.canva = canva
        self.pontos = lista
        self.xi, self.yi, self.xf, self.yf = lista[0], lista[1], lista[0], lista[1]
        self.outline = outline
        self.fill = fill
        self.expessura = expessura
        self.inix, self.iniy = self.xi, self.yi

    def desenhar(self, tag="True",construir=None):
        if construir:
            self.poligonoFinal()
        else:
            self.canva.create_line(
                self.xi,
                self.yi,
                self.xf,
                self.yf,
                fill=self.outline,
                tags=tag,
                width=self.expessura
            )
    def poligonoFinal(self):
        self.canva.delete("True")
        self.canva.delete("true2")
        self.canva.create_polygon(*self.pontos, fill=self.fill, outline=self.outline, width=self.expessura)
    def marcarponto(self, event):
        if abs(event.x - self.inix) <= 8 and abs(event.y - self.iniy) <= 8:
            self.poligonoFinal()
            return True
        else:
            self.pontos.extend([event.x, event.y])
            self.canva.delete("True")
            self.desenhar("true2")
            self.xi, self.yi = self.xf, self.yf
            return False


class Livre(Pincel):

    def desenhar(self,construir=None):
        self.canva.create_line(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.outline,
            tags=str(self.temp),
            width=self.expessura,
        )
        self.figuras.append(f"{self.xi},{self.yi},{self.xf},{self.yf},{self.outline},{self.outline},{self.expessura},linha")


class Reta(Pincel):

    def desenhar(self,construir=None):
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

    def desenhar(self,construir=None):
        self.canva.create_rectangle(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura
        )


class Oval(Pincel):

    def desenhar(self,construir=None):
        self.canva.create_oval(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura
        )


class Circulo(Pincel):

    def desenhar(self,construir=None):
        raio = ((self.xf - self.xi) ** 2 + (self.yf - self.yi) ** 2) ** 0.5
        self.canva.create_oval(
            self.xi - raio,
            self.yi - raio,
            self.xi + raio,
            self.yi + raio,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura
        )