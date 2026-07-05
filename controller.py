from model import *
from view import *
class Controller:
    '''Classe responsável por controlar o programa principal, ele recebe a classe da Janela para assim controlar-la utilizando o model'''
    def __init__(self, view):
        self.view = view
        self.canva = view.CanvaGrid
        self.forma = view.forma
        self.objeto = view.objeto
        self.espessura = view.Espessura
        self.eventos()
        self.formas = {
            "retangulo": Retangulo,
            "oval": Oval,
            "circulo": Circulo,
            "livre": Livre,
            "linha": Reta,
            "poligono": Poligono
        }

    def eventos(self):
        self.canva.bind("<ButtonPress-1>", self.iniciarforma)
        self.canva.bind("<B1-Motion>", self.atualizar)
        self.canva.bind("<Motion>", self.atualizarpoligono)
        self.canva.bind("<ButtonRelease-1>", self.gravar)


    def iniciarforma(self, event):
        if (self.forma.get() == "poligono" and not isinstance(self.objeto, Poligono)) or self.forma.get() != "poligono":
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
        else:
            if self.objeto.marcarponto(event):
                self.objeto = Void()

    def atualizarforma(self, event):
            self.objeto.xf = event.x
            self.objeto.yf = event.y
            if self.forma.get()=="livre":
                self.objeto.desenhar()
                self.objeto.temp = False
                self.objeto.xi, self.objeto.yi = self.objeto.xf, self.objeto.yf
            else:
                self.canva.delete("True")
                if self.forma.get() != "poligono":
                    self.objeto.temp = True
                self.objeto.desenhar()



    def verificarpoligono(self):
        if isinstance(self.objeto, Poligono):
            self.objeto = Void()
            self.canva.delete("true2", "True")

    def atualizar(self, event):
        self.atualizarforma(event)

    def atualizarpoligono(self, event):
        if isinstance(self.objeto, Poligono):
            self.atualizarforma(event)

    def gravar(self, event):
        if self.forma.get() != "poligono":
            self.gravarforma(event)
    
    def gravarforma(self, event):
        self.objeto.xf = event.x
        self.objeto.yf = event.y
        self.canva.delete("True")
        self.objeto.temp = False
        self.objeto.desenhar()