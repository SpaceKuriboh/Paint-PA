from netaddr.strategy.ipv6 import width

from model import *
from view import *

class Controller:
    def __init__(self, view):
        self.view = view
        self.canva = view.CanvaGrid
        self.forma = view.forma
        self.CoresLinha=view.CoresLinha
        self.CoresPreenchimento=view.CoresPreenchimento
        self.objeto = view.objeto
        self.espessura=view.Espessura
        self.eventos()

        self.formas = {
            "retangulo": Retangulo,
            "oval": Oval,
            "circulo": Circulo,
            "livre": Livre,
            "linha": Reta,
            "poligono":Poligono
        }

    def atualizarforma(self, event):
        if self.forma.get()!="livre" and self.forma.get()!="poligono":
            self.objeto.xf = event.x
            self.objeto.yf = event.y
            self.canva.delete("True")
            self.objeto.temp = True
            self.objeto.desenhar()#pronto?
        elif self.forma.get()=="poligono":
            self.objeto.xf = event.x
            self.objeto.yf = event.y
            self.canva.delete("True")
            self.objeto.desenhar()
        elif self.forma.get()=="livre":
            self.objeto.xf = event.x
            self.objeto.yf = event.y
            self.objeto.desenhar()
            self.objeto.temp = False
            self.objeto.xi, self.objeto.yi = self.objeto.xf, self.objeto.yf


    def eventos(self):
        self.canva.bind("<ButtonPress-1>", self.iniciarforma)
        self.canva.bind("<B1-Motion>", self.atualizar)
        self.canva.bind("<Motion>", self.atualizarpoligono)
        self.canva.bind("<ButtonRelease-1>", self.gravar)#pronto?

    def gravarforma(self,event):
        self.objeto.xf = event.x
        self.objeto.yf = event.y
        self.canva.delete("True")
        self.objeto.temp=False
        self.objeto.desenhar()

    def verificarpoligono(self):
        global Void,Poligono
        if isinstance(self.objeto, Poligono):
            self.objeto=Void()
            self.canva.delete("true2","True")#pronto?

    def iniciarforma(self,event):
        if (self.forma.get()=="poligono" and not isinstance(self.objeto,Poligono)) or self.forma.get()!="poligono":
            xi = event.x
            yi = event.y
            self.objeto = self.formas[self.forma.get()](
                self.canva,
                xi, yi, xi, yi,
                self.CoresLinha.get(),
                self.espessura.get(),
                fill=self.CoresPreenchimento.get(),
                temp=True
            )
        else:
            if self.objeto.marcarponto(event):
                self.objeto=Void()#pronto?

    def atualizar(self,event):
        self.atualizarforma(event)

    def atualizarpoligono(self,event):
        if isinstance(self.objeto, Poligono):
            self.atualizarforma(event)
    def gravar(self,event):
        if self.forma.get()!="poligono":
            self.gravarforma(event)

