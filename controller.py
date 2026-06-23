from model import *
from view import *

class Controller:
    def __init__(self, view):
        self.view = view
        self.canva = view.CanvaGrid
        self.forma = view.forma
        self.espessura = view.Espessura
        self.objeto = void()
        self.eventos()

        self.formas = {
            "retangulo": Retangulo,
            "oval": Oval,
            "circulo": Circulo,
            "livre": Livre,
            "linha": Reta,
            "poligono":Poligono
        }

    def eventos(self):
        self.canva.bind("<ButtonPress-1>", self.iniciarforma)
        self.canva.bind("<B1-Motion>", self.atualizar)
        self.canva.bind("<Motion>", self.atualizarpoligono)
        self.canva.bind("<ButtonRelease-1>", self.gravar)

    def verificarpoligono(self):
        global objeto,void
        if isinstance(objeto, Poligono):
            objeto=void()
            self.CanvaGrid.delete("true2","True")

    def iniciarforma(event,self):
        global forma, objeto
        if (self.forma.get()=="poligono" and not isinstance(self.objeto,Poligono)) or self.forma.get()!="poligono":
            xi = event.x
            yi = event.y
            self.objeto = self.formas[self.forma.get()](
                self.canva,
                xi, yi, xi, yi,
                self.CoresLinha.get(),
                int(self.espessura.get()),
                fill=self.CoresPreenchimento.get(),
                temp=True
            )
        else:
            if self.objeto.marcarponto(event):
                self.objeto=void()

    def atualizar(event,self):
        self.objeto.atualizarforma(event,self)

    def atualizarpoligono(event,self):
        if isinstance(objeto, Poligono):
            self.objeto.atualizarforma(event)
    def gravar(event,self):
        if forma.get()!="poligono":
            self.objeto.gravarforma(event)

