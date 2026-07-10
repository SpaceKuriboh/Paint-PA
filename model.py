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
        print(1)
        pass

class Pincel(ABC):

    def __init__(self, canva,pontos, outline, expessura, figuras=None, fill=None, temp=None):
        self.canva = canva
        self.pontos = pontos
        self.figuras=figuras
        self.outline = outline
        self.expessura = expessura
        self.fill = fill
        self.temp = temp


class Poligono(Pincel):

    def __init__(self, canva,pontos, outline, expessura, fill=None, temp=None):
        super().__init__(canva,pontos,outline,expessura,fill=fill, temp = temp)
        self.inix = pontos[0]
        self.iniy = pontos[1]

    def desenhar(self, tag="True"):
        if len(self.pontos) >= 4:
            self.canva.create_line(
                *self.pontos[-4:],
                fill=self.outline,
                tags=tag,
                width=self.expessura
            )

    def marcarponto(self, event):
        if abs(event.x - self.inix) <= 8 and abs(event.y - self.iniy) <= 8:
            self.canva.delete("True")
            self.canva.delete("true2")
            self.canva.create_polygon(*self.pontos, fill=self.fill, outline=self.outline, width=self.expessura)
            return True
        else:
            self.pontos.extend([event.x, event.y])
            self.canva.delete("True")
            self.desenhar("true2")
            return False


class Livre(Pincel):

    def desenhar(self):
        if len(self.pontos) >= 4:
            self.canva.create_line(
                *self.pontos[-4:],
                fill=self.outline,
                tags=str(self.temp),
                width=self.expessura
            )

class Reta(Pincel):

    def desenhar(self):
        self.canva.create_line(
            *self.pontos,
            fill=self.outline,
            tags=str(self.temp),
            width=self.expessura,
        )


class Retangulo(Pincel):

    def desenhar(self):
        self.canva.create_rectangle(
            *self.pontos,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura
        )


class Oval(Pincel):

    def desenhar(self):
        self.canva.create_oval(
            *self.pontos,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura
        )


class Circulo(Pincel):

    def desenhar(self):
        raio = ((self.pontos[2] - self.pontos[0]) ** 2 + (self.pontos[3] - self.pontos[1]) ** 2) ** 0.5
        self.canva.create_oval(
            self.pontos[0] - raio,
            self.pontos[1] - raio,
            self.pontos[0] + raio,
            self.pontos[1] + raio,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura
        )