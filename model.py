from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class Void:
    def __init__(self):
        self.caminho=None
        self.figuras=None
    def iniciar_forma(self,controller, event):
        pass
    def atualizar_forma(self,tipo,controller,event):
        pass
    def gravar_forma(self,controller,event):
        pass
    def verificarpoligono(self):
        pass
    def desenhar(self):
        pass
    def mudar_controlador(self):
        pass
    def construirtudo(self):
        pass
    def mudar_cor_selecionada(self, controller, outline=None, fill=None):
        pass
    def apagar_forma(self, controller, event):
        pass
    def copiar_forma(self, controller, event):
        pass
    def colar_forma(self, controller, event):
        pass

    def mudar_espessura(self, param):
        pass

    def mudar_espessura_selecionada(self, self1, width):
        pass


class Camadas(list):

    def adicionar(self, figura):
        self.append(figura)

    def remover(self, indice):
        if 0 <= indice < len(self):
            del self[indice]

    def obter(self, indice):
        return self[indice]

    def quebrar_str(self, indice):
        partes = self[indice].split(",")
        return partes[:-4], partes[-4], partes[-3], partes[-2], partes[-1]

    def verificar_clique(self, indice):
        pontos, outline, fill, expessura, tipo = self.quebrar_str(indice)
        numeros = list(map(int, pontos))
        if tipo == "circulo":
            xi, yi, xf, yf = numeros
            raio = ((xf - xi) ** 2 + (yf - yi) ** 2) ** 0.5
            return xi - raio, yi - raio, xi + raio, yi + raio
        xs, ys = numeros[0::2], numeros[1::2]
        return min(xs), min(ys), max(xs), max(ys)

    def encontrar(self, x, y, margem=5):
        for indice in range(len(self) - 1, -1, -1):
            x0, y0, x1, y1 = self.verificar_clique(indice)
            if x0 - margem <= x <= x1 + margem and y0 - margem <= y <= y1 + margem:
                return indice
        return None

    def mudar_cor(self, indice, outline=None, fill=None):
        pontos, cor_linha, cor_preenchimento, expessura, tipo = self.quebrar_str(indice)
        if outline:
            cor_linha = outline
        if fill:
            cor_preenchimento = fill
        self[indice] = ",".join(pontos + [cor_linha, cor_preenchimento, expessura, tipo])

    def mudar_espessura(self, indice, width=None):
        pontos, cor_linha, cor_preenchimento, expessura, tipo= self.quebrar_str(indice)
        if width:
            expessura = width
        self[indice] = ",".join(pontos + [cor_linha, cor_preenchimento, expessura, tipo])
        print(2)

    def mover(self, indice, dx, dy):
        pontos, outline, fill, expessura, tipo = self.quebrar_str(indice)
        pontos = [str(int(p) + (dx if i % 2 == 0 else dy)) for i, p in enumerate(pontos)]
        self[indice] = ",".join(pontos + [outline, fill, expessura, tipo])


class Pincel(ABC):

    def __init__(self, canva, lista, outline, expessura, figuras=None, fill=None, temp=None):
        self.canva = canva
        self.xi, self.yi, self.xf, self.yf = lista[0]
        self.figuras=figuras
        self.outline = outline
        self.expessura = expessura
        self.fill = fill
        self.temp = temp


class Poligono:

    def __init__(self, canva, lista, outline, expessura, fill=None, temp=None,figuras=None):
        self.canva = canva
        self.pontos = lista
        self.xi, self.yi, self.xf, self.yf = lista[0], lista[1], lista[0], lista[1]
        self.outline = outline
        self.fill = fill
        self.expessura = expessura
        self.inix, self.iniy = self.xi, self.yi

    def desenhar(self, tag="True",construir=None):
        if construir:
            self.poligonoFinal()
        else:
            self.canva.create_line(
                self.xi,
                self.yi,
                self.xf,
                self.yf,
                fill=self.outline,
                tags=tag,
                width=self.expessura
            )
    def poligonoFinal(self):
        self.canva.delete("True")
        self.canva.delete("true2")
        self.canva.create_polygon(*self.pontos, fill=self.fill, outline=self.outline, width=self.expessura)
    def marcarponto(self, event):
        if abs(event.x - self.inix) <= 8 and abs(event.y - self.iniy) <= 8:
            self.poligonoFinal()
            return True
        else:
            self.pontos.extend([event.x, event.y])
            self.canva.delete("True")
            self.desenhar("true2")
            self.xi, self.yi = self.xf, self.yf
            return False


class Livre(Pincel):

    def desenhar(self,construir=None):
        self.canva.create_line(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.outline,
            tags=str(self.temp),
            width=self.expessura,
        )
        self.figuras.append(f"{self.xi},{self.yi},{self.xf},{self.yf},{self.outline},{self.outline},{self.expessura},linha")


class Reta(Pincel):

    def desenhar(self,construir=None):
        self.canva.create_line(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.outline,
            tags=str(self.temp),
            width=self.expessura,
        )


class Retangulo(Pincel):

    def desenhar(self,construir=None):
        self.canva.create_rectangle(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura
        )


class Oval(Pincel):

    def desenhar(self,construir=None):
        self.canva.create_oval(
            self.xi,
            self.yi,
            self.xf,
            self.yf,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura
        )


class Circulo(Pincel):

    def desenhar(self,construir=None):
        raio = ((self.xf - self.xi) ** 2 + (self.yf - self.yi) ** 2) ** 0.5
        self.canva.create_oval(
            self.xi - raio,
            self.yi - raio,
            self.xi + raio,
            self.yi + raio,
            fill=self.fill,
            outline=self.outline,
            tags=str(self.temp),
            width=self.expessura
        )