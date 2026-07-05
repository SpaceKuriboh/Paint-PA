import controller
from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class State(ABC):
    @abstractmethod
    def iniciar_forma():
        pass
    @abstractmethod
    def atualziar_forma():
        pass
    @abstractmethod
    def gravar_forma():
        pass
    @abstractmethod()
    def desenhar():
        pass

class Controller_oval(State):
    def iniciar_forma(self, event):
        xi = event.x
        yi = event.y
        self.objeto = self.formas[self.forma.get()](
        self.canva,
        xi, yi, xi, yi,
        self.view.cor_linha,
        self.espessura.get(),
        fill=self.view.cor_preenchimento,
        temp=True
            )
    def atualizarforma(self, event):
            self.objeto.xf = event.x
            self.objeto.yf = event.y
            self.canva.delete("True")
            self.objeto.temp = True
            self.objeto.desenhar()
    def gravarforma(self, event):
        self.objeto.xf = event.x
        self.objeto.yf = event.y
        self.canva.delete("True")
        self.objeto.temp = False
        self.objeto.desenhar()

class Controller_circulo(State):
    def iniciar_forma(self, event):
        xi = event.x
        yi = event.y
        self.objeto = self.formas[self.forma.get()](
        self.canva,
        xi, yi, xi, yi,
        self.view.cor_linha,
        self.espessura.get(),
        fill=self.view.cor_preenchimento,
        temp=True
            )
    def atualizarforma(self, event):
            self.objeto.xf = event.x
            self.objeto.yf = event.y
            self.canva.delete("True")
            self.objeto.temp = True
            self.objeto.desenhar()
    def gravarforma(self, event):
        self.objeto.xf = event.x
        self.objeto.yf = event.y
        self.canva.delete("True")
        self.objeto.temp = False
        self.objeto.desenhar()
        
class Controller_circulo(State):
    def iniciar_forma(self, event):
        xi = event.x
        yi = event.y
        self.objeto = self.formas[self.forma.get()](
        self.canva,
        xi, yi, xi, yi,
        self.view.cor_linha,
        self.espessura.get(),
        fill=self.view.cor_preenchimento,
        temp=True
            )
    def atualizarforma(self, event):
            self.objeto.xf = event.x
            self.objeto.yf = event.y
            self.canva.delete("True")
            self.objeto.temp = True
            self.objeto.desenhar()
    def gravarforma(self, event):
        self.objeto.xf = event.x
        self.objeto.yf = event.y
        self.canva.delete("True")
        self.objeto.temp = False
        self.objeto.desenhar()

