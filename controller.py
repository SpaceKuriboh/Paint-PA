from model import *
from view import *
from state import *


class Controller:
    '''Classe responsável por controlar o programa principal, ele recebe a classe da Janela para assim controlar-la utilizando o model'''

    def __init__(self, view):
        self.view = view
        self.canva = view.CanvaGrid
        self.forma = view.forma
        self.controlador = Void()
        self.objeto = view.objeto
        self.espessura = view.Espessura
        self.figuras = Camadas()
        self.caminho = None
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
            "poligono": Controller_poligono,
            "selecionar": Controller_selecionar
        }

        self.estado = None

    def iniciar(self, eventos):
        self.canva.focus_set()
        self.controlador.iniciar_forma(self, eventos)

    def atualizar(self, eventos):
        self.controlador.atualizar_forma("B1", self, eventos)

    def gravar(self, eventos):
        self.controlador.gravar_forma(self, eventos)

    def atualizarpoligono(self, eventos):
        self.controlador.atualizar_forma("M", self, eventos)

    def mudar_cor(self, outline=None, fill=None):
        self.controlador.mudar_cor_selecionada(self, outline=outline, fill=fill)

    def mudar_espessura(self, width=None):
        self.controlador.mudar_espessura_selecionada(self,  width=width)

    def apagar(self, eventos):
        self.controlador.apagar_forma(self, eventos)

    def copiar(self, eventos):
        self.controlador.copiar_forma(self, eventos)

    def colar(self, eventos):
        self.controlador.colar_forma(self, eventos)

    def eventos(self):
        self.canva.bind("<ButtonPress-1>", self.iniciar)
        self.canva.bind("<B1-Motion>", self.atualizar)
        self.canva.bind("<Motion>", self.atualizarpoligono)
        self.canva.bind("<ButtonRelease-1>", self.gravar)
        self.canva.bind("<Delete>", self.apagar)
        self.canva.bind("<BackSpace>", self.apagar)
        self.canva.bind("<Control-c>", self.copiar)
        self.canva.bind("<Control-v>", self.colar)

    def mudar_controlador(self):
        self.controlador = self.estados[self.forma.get()]()

    def verificarpoligono(self):
        if isinstance(self.objeto, Poligono):
            self.objeto = Void()
            self.canva.delete("true2", "True")

    def construirtudo(self):
        for c in self.figuras:
            param_fig = c.split(",")
            pontos = list(map(int, param_fig[:-4]))
            if param_fig[-1] != "poligono":
                pontos = [pontos]
            self.formas[param_fig[-1]](
                self.canva,
                lista=pontos,
                expessura=int(param_fig[-2]),
                outline=param_fig[-4],
                figuras=self.figuras,
                fill=param_fig[-3],
                temp=False
            ).desenhar(construir=True)