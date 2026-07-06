from model import *
from view import *
from state import *
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
        
        self.estados = {
            "livre": Controller_livre,
            "reta": Controller_reta,
            "retangulo": Controller_retangulo,
            "oval": Controller_oval,
            "circulo": Controller_circulo,
            "poligono": Controller_poligono
        }
        
        self.estado = None
    
    def eventos(self):
        self.canva.bind("<ButtonPress-1>", self.iniciarforma)
        self.canva.bind("<B1-Motion>", self.atualizar)
        self.canva.bind("<Motion>", self.atualizarpoligono)
        self.canva.bind("<ButtonRelease-1>", self.gravar)