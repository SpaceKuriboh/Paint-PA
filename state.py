from model import Void, Poligono, PoligonoRegular


class State:
    def iniciar_forma(self, controller, event, ctrl=False):
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

    def mudar_cor_selecionada(self, controller, outline=None, fill=None):
        pass

    def mudar_espessura_selecionada(self, controller, width=None):
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


class Controller_livre(State):
    def __init__(self):
        print("Controlador Atual: Livre")

    def iniciar_forma(self, controller, event, ctrl=False):
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

    def iniciar_forma(self, controller, event, ctrl=False):
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


class Controller_poligono_regular(State):
    def __init__(self):
        print("Controlador Atual: Poligono Regular")

    def iniciar_forma(self, controller, event, ctrl=False):
        if isinstance(controller.objeto, PoligonoRegular):
            # segundo clique: confirma o poligono e reinicia
            o = controller.objeto
            if o.raio > 0 and o.n_lados >= 3:
                planas = ",".join(str(p) for p in o.coords_planas())
                controller.figuras.append(
                    f"{planas},{o.outline},{o.fill},{o.expessura},poligono")
            controller.canva.delete("True")
            controller.objeto = Void()
            controller.canva.delete("all")
            controller.construirtudo()
        else:
            # primeiro clique: fixa o centro e cria o triangulo inicial
            controller.objeto = controller.formas[controller.forma.get()](
                controller.canva,
                [event.x, event.y],
                controller.view.cor_linha,
                controller.espessura.get(),
                fill=controller.view.cor_preenchimento,
                temp=True
            )

    def atualizar_forma(self, tipo, controller, event):
        if tipo == "M" and isinstance(controller.objeto, PoligonoRegular):
            o = controller.objeto
            o.raio = ((event.x - o.cx) ** 2 + (event.y - o.cy) ** 2) ** 0.5
            controller.canva.delete("True")
            o.desenhar()

    def adicionar_lado(self, controller, event):
        # botao direito: triangulo -> quadrado -> pentagono -> ...
        if isinstance(controller.objeto, PoligonoRegular):
            controller.objeto.n_lados += 1
            controller.canva.delete("True")
            controller.objeto.desenhar()

    def gravar_forma(self, controller, event):
        pass


class Controller_selecionar(State):
    def __init__(self):
        print("Controlador Atual: Selecionar")
        self.indices = set()
        self.arrastando = False
        self.laco = False
        self.copiado = []

    def _alvo(self, figuras, indice):
        gid = figuras.grupo_de(indice)
        if gid is not None:
            return set(figuras.indices_do_grupo(gid))
        return {indice}

    def iniciar_forma(self, controller, event, ctrl=False):
        figuras = controller.figuras
        indice = figuras.encontrar(event.x, event.y)
        self.laco = False
        self.arrastando = False

        if indice is None:
            if not ctrl:
                self.indices.clear()
            self.laco = True
            self.ini_x, self.ini_y = event.x, event.y
        else:
            alvo = self._alvo(figuras, indice)
            if ctrl:
                if alvo <= self.indices:
                    self.indices -= alvo
                else:
                    self.indices |= alvo
            else:
                if not (alvo <= self.indices):
                    self.indices = set(alvo)
                self.arrastando = True
                self.ultimo_x, self.ultimo_y = event.x, event.y
        self.redesenhar(controller)

    def atualizar_forma(self, tipo, controller, event):
        if tipo != "B1":
            return
        if self.arrastando and self.indices:
            dx = event.x - self.ultimo_x
            dy = event.y - self.ultimo_y
            for i in self.indices:
                controller.figuras.mover(i, dx, dy)
            self.ultimo_x, self.ultimo_y = event.x, event.y
            self.redesenhar(controller)
        elif self.laco:
            controller.canva.delete("laco")
            controller.canva.create_rectangle(
                self.ini_x, self.ini_y, event.x, event.y,
                outline="red", dash=(3, 2), tags="laco"
            )

    def gravar_forma(self, controller, event):
        if self.laco:
            controller.canva.delete("laco")
            self._selecionar_dentro(controller, self.ini_x, self.ini_y, event.x, event.y)
            self.laco = False
            self.redesenhar(controller)
        self.arrastando = False

    def _selecionar_dentro(self, controller, ax, ay, bx, by):
        figuras = controller.figuras
        lx0, lx1 = min(ax, bx), max(ax, bx)
        ly0, ly1 = min(ay, by), max(ay, by)
        dentro = set()
        for i in range(len(figuras)):
            x0, y0, x1, y1 = figuras.verificar_clique(i)
            if lx0 <= x0 and ly0 <= y0 and x1 <= lx1 and y1 <= ly1:
                dentro.add(i)
        for i in list(dentro):
            gid = figuras.grupo_de(i)
            if gid is not None:
                dentro |= set(figuras.indices_do_grupo(gid))
        self.indices = dentro

    def mudar_cor_selecionada(self, controller, outline=None, fill=None):
        for i in self.indices:
            controller.figuras.mudar_cor(i, outline=outline, fill=fill)
        self.redesenhar(controller)

    def mudar_espessura_selecionada(self, controller, width=None):
        for i in self.indices:
            controller.figuras.mudar_espessura(i, width=width)
        self.redesenhar(controller)

    def apagar_forma(self, controller, event):
        if self.indices:
            controller.figuras.remover_varios(self.indices)
            self.indices = set()
            self.redesenhar(controller)

    def copiar_forma(self, controller, event):
        self.copiado = [controller.figuras.obter(i) for i in sorted(self.indices)]

    def colar_forma(self, controller, event):
        if self.copiado:
            novos = set()
            for figura in self.copiado:
                controller.figuras.adicionar(figura)
                novos.add(len(controller.figuras) - 1)
            self.indices = novos
            self.redesenhar(controller)

    def agrupar_selecionada(self, controller):
        if len(self.indices) >= 2:
            controller.figuras.agrupar(self.indices)
            self.redesenhar(controller)

    def desagrupar_selecionada(self, controller):
        if self.indices:
            controller.figuras.desagrupar(self.indices)
            self.redesenhar(controller)

    def frente_selecionada(self, controller):
        if self.indices:
            self.indices = controller.figuras.frente_varios(self.indices)
            self.redesenhar(controller)

    def tras_selecionada(self, controller):
        if self.indices:
            self.indices = controller.figuras.tras_varios(self.indices)
            self.redesenhar(controller)

    def topo_selecionada(self, controller):
        if self.indices:
            self.indices = controller.figuras.topo_varios(self.indices)
            self.redesenhar(controller)

    def fundo_selecionada(self, controller):
        if self.indices:
            self.indices = controller.figuras.fundo_varios(self.indices)
            self.redesenhar(controller)

    def redesenhar(self, controller):
        controller.canva.delete("all")
        controller.construirtudo()
        self.destacar(controller)

    def destacar(self, controller):
        for i in sorted(self.indices):
            if 0 <= i < len(controller.figuras):
                x0, y0, x1, y1 = controller.figuras.verificar_clique(i)
                controller.canva.create_rectangle(
                    x0 - 3, y0 - 3, x1 + 3, y1 + 3,
                    outline="red", width=2, dash=(4, 2), tags="selecao"
                )
