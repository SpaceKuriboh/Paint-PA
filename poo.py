import abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

class Desenho:
    def __init__(self, canva, xi, yi, xf, yf, outline, fill=None, expessura, temp):
         self.canva = canva
         self.xi = xi
         self.yi = yi
         self.xf = xf
         self.yf = yf
         self.outline = outline
         self.fill = fill
         self.expessura = expessura
         self.temp = temp
    def obterPosIni(event):
        global xi, yi
        xi = event.x
        yi = event.y

    def atualizar(event):
        if forma.get()=="livre":
            global xi,yi
            xf = event.x
            yf = event.y
            desenhar(xi, yi, xf, yf, "livre", False)
            xi,yi=xf,yf
        else:
            xf = event.x
            yf = event.y
            CanvaGrid.delete("True")
            desenhar(xi, yi, xf, yf, type(self), True)


    def gravar(event):
        xf = event.x
        yf = event.y
        CanvaGrid.delete("True")
        desenhar(xi, yi, xf, yf, type(self), False)
@abstractmethod
class Pincel:
    def __init__(self, canva, xi, yi, xf, yf, outline, expessura, temp):
        self.canva = canva
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.yf = yf
        self.outline = outline
        self.expessura = expessura
        self.temp = temp
    def desenhar(self):
        pass



@abstractmethod
class figura(Pincel):
    def __init__(self, canva, xi, yi, xf, yf, outline, fill, expessura, temp):
        super().__init__(canva, xi, yi, xf, yf, outline, fill, expessura, temp)
        self.fill = fill
    def desenhar():
        pass

class Livre(Pincel):
    def __init__(self, canva, xi, yi, xf, yf, outline, expessura, temp):
         super().__init__(canva, xi, yi, xf, yf, outline, expessura, temp)
    def desenho(self):
            CanvaGrid.create_line(
            self.xi, self.yi, self.xf, self.yf,
            fill=CoresLinha.get(),
            tags=str(temp),
            width=self.expessura
        )

class Reta(Pincel):
    def __init__(self, canva, xi, yi, xf, yf, outline, expessura, temp):
         super().__init__(canva, xi, yi, xf, yf, outline, expessura, temp)
    def desenho(self):
            CanvaGrid.create_line(
            self.xi, self.yi, self.xf, self.yf,
            fill=CoresLinha.get(),
            tags=str(temp),
            width=self.expessura
        )

class Retangulo(figura):
    def __init__(self, canva, xi, yi, xf, yf, outline, fill, expessura, temp):
         super().__init__(canva, xi, yi, xf, yf, outline, fill, expessura, temp)
    def desenho(self):
            CanvaGrid.create_rectangle(
            self.xi, self.yi, self.xf, self.yf,
            fill=CoresPreenchimento.get(),
            outline=CoresLinha.get(),
            tags=str(temp),
            width=self.expessura
        )

class Circulo(figura):
    def __init__(self, canva, xi, yi, xf, yf, outline, fill, expessura, temp):
         super().__init__(canva, xi, yi, xf, yf, outline, fill, expessura, temp)
    def desenho(self):
        CanvaGrid.create_oval(
            self.xi-((self.xf-self.xi)**2+(self.yf-self.yi)**2)**(1/2), self.yi-((self.xf-self.xi)**2+(self.yf-self.fyi)**2)**(1/2), self.xi+((self.xf-self.xi)**2+(self.yf-self.yi)**2)**(1/2), self.yi+((self.xf-self.xi)**2+(self.yf-self.yi)**2)**(1/2),
            fill=CoresPreenchimento.get(),
            outline=CoresLinha.get(),
            tags=str(temp),
            width=self.expessura
        )

class Oval(figura):
    def __init__(self, canva, xi, yi, xf, yf, outline, fill, expessura, temp):
         super().__init__(canva, xi, yi, xf, yf, outline, fill, expessura, temp)
    def desenho(self):
            CanvaGrid.create_oval(
            self.xi, self.yi, self.xf, self.yf,
            fill=CoresPreenchimento.get(),
            outline=CoresLinha.get(),
            tags=str(temp),
            width=self.expessura
        )

