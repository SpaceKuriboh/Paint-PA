from controller import *
from model import Void

class State:
    def iniciar_forma(self, controller, event):
        xi = event.x
        yi = event.y
        controller.objeto = controller.formas[controller.forma.get()](
            controller.canva,
            xi, yi, xi, yi,
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
        controller.figuras.append(f"{vars(controller.objeto)["xi"]},{vars(controller.objeto)["yi"]},{vars(controller.objeto)["xf"]},{vars(controller.objeto)["yf"]},{vars(controller.objeto)["outline"]},{vars(controller.objeto)["fill"]},{vars(controller.objeto)["expessura"]},{controller.forma.get()}")


class Controller_livre(State):
    def __init__(self):
        print("Controlador Atual: Livre")
    def iniciar_forma(self, controller,event):
        xi = event.x
        yi = event.y
        controller.objeto = controller.formas[controller.forma.get()](
            controller.canva,
            xi, yi, xi, yi,
            controller.view.cor_linha,
            controller.espessura.get(),
            figuras=controller.figuras,
            fill=controller.view.cor_preenchimento,
            temp=True
        )
    def atualizar_forma(self, tipo, controller,event):
        if tipo=="B1":
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
    def iniciar_forma(self, controller,event):
        if isinstance(controller.objeto, Poligono):
            if controller.objeto.marcarponto(event):
                controller.figuras.append(f"{str(vars(controller.objeto)["pontos"])[1:-1]},{vars(controller.objeto)["outline"]},{vars(controller.objeto)["fill"]},{vars(controller.objeto)["expessura"]},{controller.forma.get()}")
                controller.objeto = Void()
        else:
            xi = event.x
            yi = event.y
            controller.objeto = controller.formas[controller.forma.get()](
            controller.canva,
            xi, yi, xi, yi,
            controller.view.cor_linha,
            controller.espessura.get(),
            fill=controller.view.cor_preenchimento,
            temp=True
                )
        
    def atualizar_forma(self, tipo, controller,event):
        if tipo=="M" and isinstance(controller.objeto,Poligono):
            controller.objeto.xf = event.x
            controller.objeto.yf = event.y
            controller.canva.delete("True")
            controller.objeto.desenhar()

    def gravar_forma(self, controller,event):
        pass

class Controller_editar(State):
    def __init__(self):
        print("Controlador Atual: Editar")
    def iniciar_forma(self, controller,event):
        controller.posicao_inix = event.x
        controller.posicao_iniy = event.y
    def atualizar_forma(self, tipo, controller, event):
        if tipo == "B1":
            posicao_finalx = event.x
            posicao_finaly = event.y
            direcao_x = posicao_finalx - controller.posicao_inix
            direcao_y = posicao_finaly - controller.posicao_iniy
            controller.canva.move(controller.objeto_atual,direcao_x, direcao_y)
            controller.posicao_inix = posicao_finalx
            controller.posicao_iniy = posicao_finaly
    def apagar_forma(self,controller):
        controller.canva.delete(controller.objeto_atual)
        controller.objeto_atual = None
    def mudar_cor(self,controller):
        controller.canva.itemconfig(controller.objeto_atual,fill=controller.view.cor_preenchimento)
    def subir(self,controller):
        controller.canva.tag_raise(controller.objeto_atual)
    def descer(self,controller):
        controller.canva.tag_lower(controller.objeto_atual)