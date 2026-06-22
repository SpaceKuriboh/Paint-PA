from model import *
class janela:
    def __init__(self):
    # ------ Fazendo a Barra de Escolhas ----
        self.FrameGrid = Frame(janela, bg="lightgray", borderwidth=3, relief="flat")
        self.CanvaGrid = Canvas(janela, bg="white", width=1920, height=1080, borderwidth=3, relief="ridge")
    # ------ Fazendo a Barra de Escolhas ----

    # -------------- BUTOES -----------------
        self.DesenharLinhas =  Radiobutton(
                                self.FrameGrid,
                                text="/",
                                width=5,
                                indicatoron=False,
                                variable=forma,
                                value="linha",
                                bg="lightgrey",
                                command=verificarpoligono
                            )
        self.DesenharLivre = Radiobutton(
                                self.FrameGrid,
                                text="~",
                                width=5,
                                indicatoron=False,
                                variable=forma,
                                value="livre",
                                bg="lightgrey",
                                command=verificarpoligono
                            )
        self.DesenharRetangulos = Radiobutton(
                                    self.FrameGrid,
                                    text="▯",
                                    width=5,
                                    indicatoron=False,
                                    variable=forma,
                                    value="retangulo",
                                    bg="lightgrey",
                                    command=verificarpoligono
                                )
        self.DesenharCirculos = Radiobutton(
                                            self.FrameGrid,
                                            text="O",
                                            width=5,
                                            indicatoron=False,
                                            variable=forma,
                                            value="circulo",
                                            bg="lightgrey",
                                            command=verificarpoligono
                                        )
        self.DesenharPoligonos = Radiobutton(
                                    self.FrameGrid,
                                    text="◊",
                                    width=5,
                                    indicatoron=False,
                                    variable=forma,
                                    value="poligono",
                                    bg="lightgrey"
                                )
        self.DesenharOvais = Radiobutton(
                                    self.FrameGrid,
                                    text="⬭",
                                    width=5,
                                    indicatoron=False,
                                    variable=forma,
                                    value="oval",
                                    bg="lightgrey",
                                    command=verificarpoligono
                                )
        self.ApagarTudo = Button(
                                self.FrameGrid,
                                text="Apagar Tudo",
                                width=12,
                                bg="lightgrey",
                                command=lambda: [CanvaGrid.delete("all"),verificarpoligono()],
                            )
    # -------------- BUTOES -------------------------
    # -------------- Caixas de Selecao --------------
        self.TXTLinha = Label(self.FrameGrid, text="Cor da Linha: ")
        self.CoresLinha = Combobox(
            self.FrameGrid,
            values=["blue", "red", "green", "yellow", "purple", "pink", "black"],
            state="readonly",
            width=10,
        )

        self.TXTPreenchimento = Label(self.FrameGrid, text="Cor do Preenchimento: ")
        self.CoresPreenchimento = Combobox(
            self.FrameGrid,
            values=["blue", "red", "green", "yellow", "purple", "pink", "black"],
            state="readonly",
            width=10,
        )

        self.TXTEspessura = Label(self.FrameGrid, text="Selecione a Expessura: ")
        self.Espessura = Combobox(
            self.FrameGrid,
            values=['1', '2', '3', '4', '5', '6', '7', '8'],
            state="readonly",
            width=10,
        )
    # -------------- Caixas de Selecao --------------
    # -------------- Opcoes Iniciais ----------------
        self.CoresLinha.set("black")
        self.CoresPreenchimento.set("black")
        self.Espessura.set(4)
    # -------------- Opcoes Iniciais ----------------
    # --------------- Grid --------------------------
        self.FrameGrid.grid(row=0, column=0, sticky="ew")
        self.CanvaGrid.grid(row=1, column=0)
    # --------------- ROW 0 ---------------------
        # ----------- Butoes --------------------
        self.DesenharLinhas.grid(row=0, column=0, padx=5, pady=5)
        self.DesenharLivre.grid(row=0, column=1, padx=5, pady=5)
        self.DesenharRetangulos.grid(row=0, column=2, padx=5, pady=5)
        self.DesenharCirculos.grid(row=0, column=3, padx=5, pady=5)
        self.DesenharPoligonos.grid(row=0, column=4, padx=5, pady=5)
        self.DesenharOvais.grid(row=0, column=5, padx=5, pady=5)
        self.ApagarTudo.grid(row=0, column=6, padx=5, pady=5)
        # ----------- Butoes --------------------
        # -------------- Caixas de Selecao --------------
        self.TXTLinha.grid(row=0, column=7, padx=1, pady=5)
        self.CoresLinha.grid(row=0, column=8, padx=5, pady=5)

        self.TXTPreenchimento.grid(row=0, column=9, padx=1, pady=5)
        self.CoresPreenchimento.grid(row=0, column=10, padx=5, pady=5)

        self.TXTEspessura.grid(row=0, column=11, padx=1, pady=5)
        self.Espessura.grid(row=0, column=12, padx=5, pady=5)
        # -------------- Caixas de Selecao --------------








