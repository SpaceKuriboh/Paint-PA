from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


class Void:
    def __init__(self):
        self.caminho = None
        self.figuras = None

    def iniciar_forma(self, controller, event, ctrl=False):
        pass

    def atualizar_forma(self, tipo, controller, event):
        pass

    def gravar_forma(self, controller, event):
        pass

    def desenhar(self):
        pass

    def construirtudo(self):
        pass

    def mudar_controlador(self):
        pass

    def verificarpoligono(self):
        pass

    def mudar_cor_selecionada(self, controller, outline=None, fill=None):
        pass

    def mudar_espessura(self, param):
        pass

    def mudar_espessura_selecionada(self, self1, width):
        pass

    def apagar_forma(self, controller, event):
        pass

    def copiar_forma(self, controller, event):
        pass

    def colar_forma(self, controller, event):
        pass

    def adicionar_lado(self, controller, event):
        pass

    def agrupar_selecionada(self, controller):
        pass

    def desagrupar_selecionada(self, controller):
        pass

    def frente_selecionada(self, controller):
        pass

    def tras_selecionada(self, controller):
        pass

    def topo_selecionada(self, controller):
        pass

    def fundo_selecionada(self, controller):
        pass


class Camadas(list):

    def __init__(self, iteravel=()):
        super().__init__(iteravel)
        self.grupos = [None] * len(self)
        self._prox_grupo = 1

    def append(self, figura):
        super().append(figura)
        self.grupos.append(None)

    def adicionar(self, figura):
        self.append(figura)

    def remover(self, indice):
        if 0 <= indice < len(self):
            del self[indice]
            del self.grupos[indice]

    def remover_varios(self, indices):
        for indice in sorted(indices, reverse=True):
            self.remover(indice)

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

    def _dist_ponto_segmento(self, x1, y1, x2, y2, px, py):
        dx = x2 - x1
        dy = y2 - y1
        comp_sq = dx * dx + dy * dy
        if comp_sq == 0:
            return ((px - x1) ** 2 + (py - y1) ** 2) ** 0.5
        t = ((px - x1) * dx + (py - y1) * dy) / comp_sq
        t = max(0.0, min(1.0, t))
        proj_x = x1 + t * dx
        proj_y = y1 + t * dy
        return ((px - proj_x) ** 2 + (py - proj_y) ** 2) ** 0.5

    def _ponto_no_poligono(self, vertices, x, y):
        n = len(vertices)
        if n < 3:
            return False
        dentro = False
        p1x, p1y = vertices[0]
        for i in range(n + 1):
            p2x, p2y = vertices[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        x_inter = p1x
                        if p1y != p2y:
                            x_inter = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= x_inter:
                            dentro = not dentro
            p1x, p1y = p2x, p2y
        return dentro

    def acertou(self, indice, x, y, margem=5):
        pontos, outline, fill, expessura, tipo = self.quebrar_str(indice)
        nums = list(map(int, pontos))
        tol = margem + int(expessura) / 2
        preenchido = bool(fill) and fill != ""

        if tipo == "linha":
            x1, y1, x2, y2 = nums
            return self._dist_ponto_segmento(x1, y1, x2, y2, x, y) <= tol

        if tipo == "retangulo":
            x1, y1, x2, y2 = nums
            xmin, xmax = min(x1, x2), max(x1, x2)
            ymin, ymax = min(y1, y2), max(y1, y2)
            if preenchido:
                return xmin - margem <= x <= xmax + margem and ymin - margem <= y <= ymax + margem
            dentro_caixa = xmin - tol <= x <= xmax + tol and ymin - tol <= y <= ymax + tol
            na_borda = abs(x - xmin) <= tol or abs(x - xmax) <= tol or abs(y - ymin) <= tol or abs(y - ymax) <= tol
            return dentro_caixa and na_borda

        if tipo == "oval":
            x1, y1, x2, y2 = nums
            cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
            rx = abs(x2 - x1) / 2 + margem
            ry = abs(y2 - y1) / 2 + margem
            if rx == 0 or ry == 0:
                return False
            return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1

        if tipo == "circulo":
            xi, yi, xf, yf = nums
            raio = ((xf - xi) ** 2 + (yf - yi) ** 2) ** 0.5
            return ((x - xi) ** 2 + (y - yi) ** 2) ** 0.5 <= raio + margem

        if tipo == "poligono":
            vertices = list(zip(nums[0::2], nums[1::2]))
            if self._ponto_no_poligono(vertices, x, y):
                return True
            n = len(vertices)
            for i in range(n):
                x1, y1 = vertices[i]
                x2, y2 = vertices[(i + 1) % n]
                if self._dist_ponto_segmento(x1, y1, x2, y2, x, y) <= tol:
                    return True
            return False

        return False

    def encontrar(self, x, y, margem=5):
        for indice in range(len(self) - 1, -1, -1):
            if self.acertou(indice, x, y, margem):
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
        pontos, cor_linha, cor_preenchimento, expessura, tipo = self.quebrar_str(indice)
        if width:
            expessura = width
        self[indice] = ",".join(pontos + [cor_linha, cor_preenchimento, expessura, tipo])

    def mover(self, indice, dx, dy):
        pontos, outline, fill, expessura, tipo = self.quebrar_str(indice)
        pontos = [str(int(p) + (dx if i % 2 == 0 else dy)) for i, p in enumerate(pontos)]
        self[indice] = ",".join(pontos + [outline, fill, expessura, tipo])


    def frente(self, indice):
        if indice is None or not (0 <= indice < len(self) - 1):
            return indice
        self[indice], self[indice + 1] = self[indice + 1], self[indice]
        self.grupos[indice], self.grupos[indice + 1] = self.grupos[indice + 1], self.grupos[indice]
        return indice + 1

    def tras(self, indice):
        if indice is None or not (0 < indice < len(self)):
            return indice
        self[indice], self[indice - 1] = self[indice - 1], self[indice]
        self.grupos[indice], self.grupos[indice - 1] = self.grupos[indice - 1], self.grupos[indice]
        return indice - 1

    def topo(self, indice):
        if indice is None or not (0 <= indice < len(self)):
            return indice
        fig, g = self[indice], self.grupos[indice]
        del self[indice]
        del self.grupos[indice]
        super().append(fig)
        self.grupos.append(g)
        return len(self) - 1

    def fundo(self, indice):
        if indice is None or not (0 <= indice < len(self)):
            return indice
        fig, g = self[indice], self.grupos[indice]
        del self[indice]
        del self.grupos[indice]
        self.insert(0, fig)
        self.grupos.insert(0, g)
        return 0

    def _remover_bloco(self, indices):
        ordenados = sorted(indices)
        bloco = [(self[i], self.grupos[i]) for i in ordenados]
        for i in reversed(ordenados):
            del self[i]
            del self.grupos[i]
        return ordenados, bloco

    def _inserir_bloco(self, pos, bloco):
        for desloc, (fig, g) in enumerate(bloco):
            self.insert(pos + desloc, fig)
            self.grupos.insert(pos + desloc, g)
        return set(range(pos, pos + len(bloco)))

    def frente_varios(self, indices):
        if not indices:
            return set()
        ordenados, bloco = self._remover_bloco(indices)
        return self._inserir_bloco(min(min(ordenados) + 1, len(self)), bloco)

    def tras_varios(self, indices):
        if not indices:
            return set()
        ordenados, bloco = self._remover_bloco(indices)
        return self._inserir_bloco(max(min(ordenados) - 1, 0), bloco)

    def topo_varios(self, indices):
        if not indices:
            return set()
        ordenados, bloco = self._remover_bloco(indices)
        return self._inserir_bloco(len(self), bloco)

    def fundo_varios(self, indices):
        if not indices:
            return set()
        ordenados, bloco = self._remover_bloco(indices)
        return self._inserir_bloco(0, bloco)

    def agrupar(self, indices):
        if len(indices) < 2:
            return
        gid = self._prox_grupo
        self._prox_grupo += 1
        for i in indices:
            self.grupos[i] = gid

    def desagrupar(self, indices):
        for i in indices:
            if 0 <= i < len(self.grupos):
                self.grupos[i] = None

    def grupo_de(self, indice):
        if 0 <= indice < len(self.grupos):
            return self.grupos[indice]
        return None

    def indices_do_grupo(self, gid):
        return [i for i, g in enumerate(self.grupos) if g == gid]


class Pincel(ABC):

    def __init__(self, canva, lista, outline, expessura, figuras=None, fill=None, temp=None):
        self.canva = canva
        self.xi, self.yi, self.xf, self.yf = lista[0]
        self.figuras = figuras
        self.outline = outline
        self.expessura = expessura
        self.fill = fill
        self.temp = temp


class Poligono:

    def __init__(self, canva, lista, outline, expessura, fill=None, temp=None, figuras=None):
        self.canva = canva
        self.pontos = lista
        self.xi, self.yi, self.xf, self.yf = lista[0], lista[1], lista[0], lista[1]
        self.outline = outline
        self.fill = fill
        self.expessura = expessura
        self.inix, self.iniy = self.xi, self.yi

    def desenhar(self, tag="True", construir=None):
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


class PoligonoRegular:
    PI = 3.14159265358979323846

    def __init__(self, canva, lista, outline, expessura, fill=None, temp=None, figuras=None):
        self.canva = canva
        self.cx, self.cy = lista[0], lista[1]
        self.raio = 0
        self.n_lados = 3
        self.outline = outline
        self.fill = fill
        self.expessura = expessura
        self.figuras = figuras
        self.temp = temp

    def _sen_cos(self, ang):
        pi = self.PI
        while ang > pi:
            ang -= 2 * pi
        while ang < -pi:
            ang += 2 * pi
        seno = 0.0
        termo = ang
        n = 1
        for _ in range(15):
            seno += termo
            termo *= -ang * ang / ((2 * n) * (2 * n + 1))
            n += 1
        cosseno = 0.0
        termo = 1.0
        n = 1
        for _ in range(15):
            cosseno += termo
            termo *= -ang * ang / ((2 * n - 1) * (2 * n))
            n += 1
        return seno, cosseno

    def vertices(self):
        pts = []
        for k in range(self.n_lados):
            ang = -self.PI / 2 + 2 * self.PI * k / self.n_lados
            seno, cosseno = self._sen_cos(ang)
            pts.append((self.cx + self.raio * cosseno, self.cy + self.raio * seno))
        return pts

    def coords_planas(self):
        planas = []
        for x, y in self.vertices():
            planas.extend([int(round(x)), int(round(y))])
        return planas

    def desenhar(self, construir=None):
        if self.raio <= 0 or self.n_lados < 3:
            return
        self.canva.create_polygon(
            *self.coords_planas(),
            fill=self.fill,
            outline=self.outline,
            width=self.expessura,
            tags=str(self.temp)
        )


class Livre(Pincel):

    def desenhar(self, construir=None):
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

    def desenhar(self, construir=None):
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

    def desenhar(self, construir=None):
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

    def desenhar(self, construir=None):
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

    def desenhar(self, construir=None):
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
