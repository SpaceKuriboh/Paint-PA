from controller import *
from model import *
from tkinter.colorchooser import askcolor

class Janela:
    def __init__(self):
        self.controller = Void()
        self.janela = Tk()
        self.janela.title("Paint 2.0 ULTRA BLASTER SUPER EXTRA CHEDDAR PLUS PLUS PLUS")
        largura = self.janela.winfo_screenwidth()
        altura = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura}x{altura}+0+0")
        self.objeto = Void()
        self.forma = StringVar()

        self.cor_linha = "black"
        self.cor_preenchimento = "black"
    # ------ Fazendo a Barra de Escolhas ----
        self.FrameGrid = Frame(self.janela, bg="#271450", borderwidth=3, relief="flat")
        self.CanvaGrid = Canvas(self.janela, bg="#FAF6EE", borderwidth=3, relief="ridge")

    # ------ Fazendo a Barra de Escolhas ----

    # -------------- BUTOES -----------------
        self.DesenharLinhas = Radiobutton(
                                self.FrameGrid,
                                text="/",
                                width=5,
                                indicatoron=False,
                                variable=self.forma,
                                value="linha",
                                bg="#3B4C8C",
                                fg="#F2E9E4",
                                activeforeground="#F2E9E4",
                                activebackground="#703892",
                                selectcolor="#703892",
                                font=("Arial", 10, "bold"),
                                command=self.controller.verificarpoligono
                            )
        self.DesenharLivre = Radiobutton(
                                self.FrameGrid,
                                text="~",
                                width=5,
                                indicatoron=False,
                                variable=self.forma,
                                value="livre",
                                bg="#3B4C8C",
                                fg="#F2E9E4",
                                activeforeground="#F2E9E4",
                                activebackground="#703892",
                                selectcolor="#703892",
                                font=("Arial", 10, "bold"),
                                command=self.controller.verificarpoligono
                            )
        self.DesenharRetangulos = Radiobutton(
                                    self.FrameGrid,
                                    text="▯",
                                    width=5,
                                    indicatoron=False,
                                    variable=self.forma,
                                    value="retangulo",
                                    bg="#3B4C8C",
                                    fg="#F2E9E4",
                                    activeforeground="#F2E9E4",
                                    activebackground="#703892",
                                    selectcolor="#703892",
                                    font=("Arial", 10, "bold"),
                                    command=self.controller.verificarpoligono
                                )
        self.DesenharCirculos = Radiobutton(
                                            self.FrameGrid,
                                            text="O",
                                            width=5,
                                            indicatoron=False,
                                            variable=self.forma,
                                            value="circulo",
                                            bg="#3B4C8C",
                                            fg="#F2E9E4",
                                            activeforeground="#F2E9E4",
                                            activebackground="#703892",
                                            selectcolor="#703892",
                                            font=("Arial", 10, "bold"),
                                            command=self.controller.verificarpoligono
                                        )
        self.DesenharPoligonos = Radiobutton(
                                    self.FrameGrid,
                                    text="◊",
                                    width=5,
                                    indicatoron=False,
                                    variable=self.forma,
                                    value="poligono",
                                    bg="#3B4C8C",
                                    fg="#F2E9E4",
                                    activeforeground="#F2E9E4",
                                    activebackground="#703892",
                                    selectcolor="#703892",
                                    font=("Arial", 10, "bold"),
                                    command=self.controller.verificarpoligono
                                )
        self.DesenharOvais = Radiobutton(
                                    self.FrameGrid,
                                    text="⬭",
                                    width=5,
                                    indicatoron=False,
                                    variable=self.forma,
                                    value="oval",
                                    bg="#3B4C8C",
                                    fg="#F2E9E4",
                                    activeforeground="#F2E9E4",
                                    activebackground="#703892",
                                    selectcolor="#703892",
                                    font=("Arial", 10, "bold"),
                                    command=self.controller.verificarpoligono
                                )
        self.ApagarTudo = Button(
                                self.FrameGrid,
                                text="Apagar Tudo",
                                width=12,
                                bg="#9C5592",
                                fg="#F2E9E4",
                                activeforeground="#F2E9E4",
                                activebackground="#703892",
                                font=("Arial", 12, "bold"),
                                command=lambda: [self.CanvaGrid.delete("all"), self.controller.verificarpoligono()],
                            )
    # -------------- BUTOES -------------------------
    # -------------- Caixas de Selecao --------------
        self.TXTLinha = Label(self.FrameGrid, text="Cor da Linha: ", fg="#F2E9E4", bg="#271450", font=("Arial", 12, "bold"))
        self.BotaoCorLinha = Button(
            self.FrameGrid,
            bg=self.cor_linha,
            width=10,
            command=self.escolher_cor_linha
        )

        self.TXTPreenchimento = Label(self.FrameGrid, text="Cor do Preenchimento: ", fg="#F2E9E4", bg="#271450", font=("Arial", 12, "bold"))
        self.BotaoCorPreenchimento = Button(
            self.FrameGrid,
            bg=self.cor_preenchimento,
            width=10,
            command=self.escolher_cor_preenchimento
        )

        self.TXTEspessura = Label(self.FrameGrid, text="Selecione a Expessura: ", fg="#F2E9E4", bg="#271450", font=("Arial", 12, "bold"))
        self.Espessura = Scale(
            self.FrameGrid,
            from_=1,
            to=20,
            orient=HORIZONTAL,
            length=120,
            bg="#3B4C8C",
            fg="#F2E9E4",
            troughcolor="#271450",
            activebackground="#703892",
            font=("Arial", 10, "bold"),
            highlightthickness=0
        )
    # -------------- Caixas de Selecao --------------
    # -------------- Opcoes Iniciais ----------------
        self.Espessura.set(4)
    # -------------- Opcoes Iniciais ----------------
    # --------------- Grid --------------------------
        self.janela.rowconfigure(1, weight=1)
        self.janela.columnconfigure(0, weight=1)
        self.FrameGrid.grid(row=0, column=0, sticky="ew")
        self.CanvaGrid.grid(row=1, column=0, sticky="nsew")
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
        self.BotaoCorLinha.grid(row=0, column=8, padx=5, pady=5)

        self.TXTPreenchimento.grid(row=0, column=9, padx=1, pady=5)
        self.BotaoCorPreenchimento.grid(row=0, column=10, padx=5, pady=5)

        self.TXTEspessura.grid(row=0, column=11, padx=1, pady=5)
        self.Espessura.grid(row=0, column=12, padx=5, pady=5)
        # -------------- Caixas de Selecao --------------

    # -------------- Seletores de Cor --------------
    def escolher_cor_linha(self):
        cor = askcolor(title="Cor da linha", initialcolor=self.cor_linha)
        if cor[1]:
            self.cor_linha = cor[1]
            self.BotaoCorLinha.config(bg=self.cor_linha)

    def escolher_cor_preenchimento(self):
        cor = askcolor(title="Cor do preenchimento", initialcolor=self.cor_preenchimento)
        if cor[1]:
            self.cor_preenchimento = cor[1]
            self.BotaoCorPreenchimento.config(bg=self.cor_preenchimento)
    # -------------- Seletores de Cor --------------