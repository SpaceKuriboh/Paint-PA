from model import *
from view import *
from state import *
class Controller:
    '''Classe responsável por controlar o programa principal, ele recebe a classe da Janela para assim controlar-la utilizando o model'''
    def __init__(self, view):
        self.view = view
        self.canva = view.CanvaGrid
        self.forma = view.forma
        self.controlador=Void()
        self.objeto = view.objeto
        self.espessura = view.Espessura
        self.figuras=[]
        self.caminho=None
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
            "linha": Controller_reta,
            "retangulo": Controller_retangulo,
            "oval": Controller_oval,
            "circulo": Controller_circulo,
            "poligono": Controller_poligono
        }
        
        self.estado = None
    def iniciar(self,eventos):
        self.controlador.iniciar_forma(self,eventos)
    def atualizar(self,eventos):
        self.controlador.atualizar_forma("B1",self,eventos)
    def gravar(self,eventos):
        self.controlador.gravar_forma(self,eventos)
    def atualizarpoligono(self,eventos):
        self.controlador.atualizar_forma("M",self,eventos)
    def eventos(self):
        self.canva.bind("<ButtonPress-1>", self.iniciar)
        self.canva.bind("<B1-Motion>", self.atualizar)
        self.canva.bind("<Motion>", self.atualizarpoligono)
        self.canva.bind("<ButtonRelease-1>", self.gravar)
    def mudar_controlador(self):
        self.controlador=self.estados[self.forma.get()]()
    def verificarpoligono(self):
        if isinstance(self.objeto, Poligono):
            self.objeto = Void()
            self.canva.delete("true2", "True")
    def construirtudo(self):
            for c in self.figuras:
                param_fig=c.split(",")
                self.formas[param_fig[-1]](
                    self.canva,
                    lista=list(map(int,param_fig[:-4])),
                    expessura=int(param_fig[-2]),
                    outline=param_fig[-4],
                    figuras=self.figuras,
                    fill=param_fig[-3],
                    temp=False
                ).desenhar(construir=True)