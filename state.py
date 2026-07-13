from controller import *
from model import Void


class State:
    def iniciar_forma(self, controller, event):
        xi = event.x
        yi = event.y
        controller.objeto = controller.formas[controller.forma.get()](
            controller.canva,
            [[xi, yi, xi, yi]],
            controller.view.cor_linha,
            controller.espessura.get(),
            fill=controller.view.cor_preenchimento,
            temp=True
        )

    def atualizar_forma(self, tipo, controller, event):
        if tipo == "B1":
            controller.objeto.xf = event.x
            controller.objeto.yf = event.y
            controller.canva.delete("True")
            controller.objeto.temp = True
            controller.objeto.desenhar()

    def gravar_forma(self, controller, event):
        controller.objeto.xf = event.x
        controller.objeto.yf = event.y
        controller.canva.delete("True")
        controller.objeto.temp = False
        controller.objeto.desenhar()
        controller.figuras.append(
            f"{vars(controller.objeto)["xi"]},{vars(controller.objeto)["yi"]},{vars(controller.objeto)["xf"]},{vars(controller.objeto)["yf"]},{vars(controller.objeto)["outline"]},{vars(controller.objeto)["fill"]},{vars(controller.objeto)["expessura"]},{controller.forma.get()}")

    # ---- Ações de seleção: no-op aqui, só o Controller_selecionar implementa de verdade ----
    def mudar_cor_selecionada(self, controller, outline=None, fill=None):
        pass

    def apagar_forma(self, controller, event):
        pass

    def copiar_forma(self, controller, event):
        pass

    def colar_forma(self, controller, event):
        pass


class Controller_livre(State):
    def __init__(self):
        print("Controlador Atual: Livre")

    def iniciar_forma(self, controller, event):
        xi = event.x
        yi = event.y
        controller.objeto = controller.formas[controller.forma.get()](
            controller.canva,
            [[xi, yi, xi, yi]],
            controller.view.cor_linha,
            controller.espessura.get(),
            figuras=controller.figuras,
            fill=controller.view.cor_preenchimento,
            temp=True
        )

    def atualizar_forma(self, tipo, controller, event):
        if tipo == "B1":
            controller.objeto.xf = event.x
            controller.objeto.yf = event.y
            controller.objeto.desenhar()
            controller.objeto.temp = False
            controller.objeto.xi, controller.objeto.yi = controller.objeto.xf, controller.objeto.yf


class Controller_reta(State):
    def __init__(self):
        print("Controlador Atual: Reta")


class Controller_retangulo(State):
    def __init__(self):
        print("Controlador Atual: Retangulo")


class Controller_oval(State):
    def __init__(self):
        print("Controlador Atual: Oval")


class Controller_circulo(State):
    def __init__(self):
        print("Controlador Atual: Circullo")


class Controller_poligono(State):
    def __init__(self):
        print("Controlador Atual: Poligono")

    def iniciar_forma(self, controller, event):
        if isinstance(controller.objeto, Poligono):
            if controller.objeto.marcarponto(event):
                controller.figuras.append(
                    f"{str(vars(controller.objeto)["pontos"])[1:-1]},{vars(controller.objeto)["outline"]},{vars(controller.objeto)["fill"]},{vars(controller.objeto)["expessura"]},{controller.forma.get()}")
                controller.objeto = Void()
        else:
            xi = event.x
            yi = event.y
            controller.objeto = controller.formas[controller.forma.get()](
                controller.canva,
                [xi, yi],
                controller.view.cor_linha,
                controller.espessura.get(),
                fill=controller.view.cor_preenchimento,
                temp=True
            )

    def atualizar_forma(self, tipo, controller, event):
        if tipo == "M" and isinstance(controller.objeto, Poligono):
            controller.objeto.xf = event.x
            controller.objeto.yf = event.y
            controller.canva.delete("True")
            controller.objeto.desenhar()

    def gravar_forma(self, controller, event):
        pass


class Controller_selecionar(State):
    def __init__(self):
        print("Controlador Atual: Selecionar")
        self.indice_selecionado = None
        self.arrastando = False
        self.copiado = None

    def iniciar_forma(self, controller, event):
        self.indice_selecionado = controller.figuras.encontrar(event.x, event.y)
        self.arrastando = self.indice_selecionado is not None
        self.ultimo_x, self.ultimo_y = event.x, event.y

    def atualizar_forma(self, tipo, controller, event):
        if tipo == "B1" and self.arrastando and self.indice_selecionado is not None:
            dx = event.x - self.ultimo_x
            dy = event.y - self.ultimo_y
            controller.figuras.mover(self.indice_selecionado, dx, dy)
            self.ultimo_x, self.ultimo_y = event.x, event.y
            self.redesenhar(controller)

    def gravar_forma(self, controller, event):
        self.arrastando = False

    def mudar_cor_selecionada(self, controller, outline=None, fill=None):
        if self.indice_selecionado is not None:
            controller.figuras.mudar_cor(self.indice_selecionado, outline=outline, fill=fill)
            self.redesenhar(controller)

    def mudar_espessura_selecionada(self, controller, width=None):
        if self.indice_selecionado is not None:
            controller.figuras.mudar_espessura(self.indice_selecionado, width=width)
            self.redesenhar(controller)

    def apagar_forma(self, controller, event):
        if self.indice_selecionado is not None:
            controller.figuras.remover(self.indice_selecionado)
            self.indice_selecionado = None
            self.redesenhar(controller)

    def copiar_forma(self, controller, event):
        if self.indice_selecionado is not None:
            self.copiado = controller.figuras.obter(self.indice_selecionado)

    def colar_forma(self, controller, event):
        if self.copiado is not None:
            controller.figuras.adicionar(self.copiado)
            self.indice_selecionado = len(controller.figuras) - 1
            self.redesenhar(controller)

    def redesenhar(self, controller):
        controller.canva.delete("all")
        controller.construirtudo()
