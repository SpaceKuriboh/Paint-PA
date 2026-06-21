from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class Pincel(ABC):
    def __init__(self, canva, xi, yi, xf, yf, outline, expessura, temp=None):
        self.canva = canva
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf
        self.outline = outline
        self.expessura = expessura
        self.temp = temp

    @abstractmethod
    def desenhar(self):
        ...


class Figura(Pincel):
    def __init__(self, canva, xi, yi, xf, yf, outline, fill, expessura, temp=None):
        super().__init__(canva, xi, yi, xf, yf, outline, expessura, temp)
        self.fill = fill

    @abstractmethod
    def desenhar(self):
        ...


class Livre(Pincel):
    def desenhar(self):
        self.canva.create_line(
            self.xi, self.yi, self.xf, self.yf,
            fill=self.outline.get(),
            tags=str(self.temp),
            width=self.expessura,
        )


class Reta(Pincel):
    def desenhar(self):
        self.canva.create_line(
            self.xi, self.yi, self.xf, self.yf,
            fill=self.outline.get(),
            tags=str(self.temp),
            width=self.expessura,
        )


class Retangulo(Figura):
    def desenhar(self):
        self.canva.create_rectangle(
            self.xi, self.yi, self.xf, self.yf,
            fill=self.fill.get(),
            outline=self.outline.get(),
            tags=str(self.temp),
            width=self.expessura,
        )


class Oval(Figura):
    def desenhar(self):
        self.canva.create_oval(
            self.xi, self.yi, self.xf, self.yf,
            fill=self.fill.get(),
            outline=self.outline.get(),
            tags=str(self.temp),
            width=self.expessura,
        )


class Circulo(Figura):
    def desenhar(self):
        raio = ((self.xf - self.xi) ** 2 + (self.yf - self.yi) ** 2) ** 0.5
        self.canva.create_oval(
            self.xi - raio, self.yi - raio, self.xi + raio, self.yi + raio,
            fill=self.fill.get(),
            outline=self.outline.get(),
            tags=str(self.temp),
            width=self.expessura,
        )