from controller import *
from model import Void


class State(ABC):
    @abstractmethod
    def iniciar_forma(self, controller, event):
        pass
    @abstractmethod
    def atualizar_forma(self, tipo, controller, event):
        pass
    @abstractmethod
    def gravar_forma(self, controller, event):
        pass


class Controller_livre(State):
    def __init__(self):
        pass
    def iniciar_forma(self, controller,event):
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
        if tipo=="B1":
            controller.objeto.xf = event.x
            controller.objeto.yf = event.y
            controller.objeto.desenhar()
            controller.objeto.temp = False
            controller.objeto.xi, controller.objeto.yi = controller.objeto.xf, controller.objeto.yf
    def gravar_forma(self, controller,event):
        controller.objeto.xf = event.x
        controller.objeto.yf = event.y
        controller.canva.delete("True")
        controller.objeto.temp = False
        controller.objeto.desenhar()

class Controller_reta(State):
    def iniciar_forma(self, controller,event):
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
        if tipo=="B1":
            controller.objeto.xf = event.x
            controller.objeto.yf = event.y
            controller.canva.delete("True")
            controller.objeto.temp = True
            controller.objeto.desenhar()
    def gravar_forma(self, controller,event):
        controller.objeto.xf = event.x
        controller.objeto.yf = event.y
        controller.canva.delete("True")
        controller.objeto.temp = False
        controller.objeto.desenhar()

class Controller_retangulo(State):
    def iniciar_forma(self, controller,event):
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
    def atualizar_forma(self, tipo,controller,event):
        if tipo=="B1":
            controller.objeto.xf = event.x
            controller.objeto.yf = event.y
            controller.canva.delete("True")
            controller.objeto.temp = True
            controller.objeto.desenhar()
    def gravar_forma(self, controller,event):
        controller.objeto.xf = event.x
        controller.objeto.yf = event.y
        controller.canva.delete("True")
        controller.objeto.temp = False
        controller.objeto.desenhar()

class Controller_oval(State):
    def iniciar_forma(self, controller,event):
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
        if tipo == "B1":
            controller.objeto.xf = event.x
            controller.objeto.yf = event.y
            controller.canva.delete("True")
            controller.objeto.temp = True
            controller.objeto.desenhar()
    def gravar_forma(self, controller,event):
        controller.objeto.xf = event.x
        controller.objeto.yf = event.y
        controller.canva.delete("True")
        controller.objeto.temp = False
        controller.objeto.desenhar()

class Controller_circulo(State):
    def iniciar_forma(self, controller,event):
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
        if tipo == "B1":
            controller.objeto.xf = event.x
            controller.objeto.yf = event.y
            controller.canva.delete("True")
            controller.objeto.temp = True
            controller.objeto.desenhar()
    def gravar_forma(self, controller,event):
        controller.objeto.xf = event.x
        controller.objeto.yf = event.y
        controller.canva.delete("True")
        controller.objeto.temp = False
        controller.objeto.desenhar()

class Controller_poligono(State):
    def iniciar_forma(self, controller,event):
        if isinstance(controller.objeto, Poligono):
            if controller.objeto.marcarponto(event):
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