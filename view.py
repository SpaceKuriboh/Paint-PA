import controller
from model import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *
class JanelaPergunta:
    def __init__(self,janela):
        self.janela=janela
        self.pergunta=Tk()
        self.pergunta.title("Abrir ou Novo")
        largura = self.pergunta.winfo_screenwidth()
        altura = self.pergunta.winfo_screenheight()
        self.pergunta.geometry(f"{largura}x{altura}+0+0")
        self.pergunta.state("normal")
        self.FramePergunta = Frame(self.pergunta, bg="#271450", borderwidth=3, relief="flat")
        self.Novo = Button(
            self.FramePergunta,
            text="Novo",
            width=12,
            bg="#9C5592",
            fg="#F2E9E4",
            activeforeground="#F2E9E4",
            activebackground="#703892",
            font=("Arial", 12, "bold"),
            command=self.fecharjanela
        )
        self.Abrir = Button(
            self.FramePergunta,
            text="Abrir",
            width=12,
            bg="#9C5592",
            fg="#F2E9E4",
            activeforeground="#F2E9E4",
            activebackground="#703892",
            font=("Arial", 12, "bold"),
            command=self.obter_arquivo
        )
        self.pergunta.rowconfigure(1, weight=1)
        self.pergunta.columnconfigure(0, weight=1)
        self.FramePergunta.grid(row=0, column=0, sticky="ew")
        self.Novo.grid(row=0, column=0, padx=5, pady=5)
        self.Abrir.grid(row=0, column=1, padx=5, pady=5)
        self.pergunta.mainloop()
    def fecharjanela(self):
        self.janela.janela.deiconify()
        self.pergunta.destroy()
    def obter_arquivo(self):
        self.janela.controller.figuras = open(askopenfilename(defaultextension=".chdd",filetypes=(("Arquivos Cheddar", "*.chdd"),("Todos os arquivos", "*.*")))).read().split("|")[:-1]
        print(self.janela.controller.figuras)
        self.janela.controller.construirtudo()
        self.fecharjanela()
class Janela:
    def __init__(self):
        self.controller=Void()
    # ----------- Janela ------------------
        self.janela = Tk()
        self.janela.title("Paint 2.0 ULTRA BLASTER SUPER EXTRA CHEDDAR PLUS PLUS PLUS")
        largura = self.janela.winfo_screenwidth()
        altura = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura}x{altura}+0+0")
        self.janela.state("normal")
    # ----------- Janela ------------------
    
        self.objeto = Void()
        self.forma = StringVar()

    # ------ Fazendo a Barra de Escolhas ----
        self.FrameGrid = Frame(self.janela, bg="#271450", borderwidth=3, relief="flat")
        self.CanvaGrid = Canvas(self.janela, bg="#FAF6EE", borderwidth=3, relief="ridge")
    # ------ Fazendo a Barra de Escolhas ----
    # --------- Cores Iniciais -------------
        self.cor_linha = "#000000"
        self.cor_preenchimento = "#000000"
    # --------- Cores Iniciais -------------
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
                                command=self.mudar_botao
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
                                command=self.mudar_botao
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
                                    command=self.mudar_botao
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
                                            command=self.mudar_botao
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
                                    command=self.mudar_botao
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
                                    command=self.mudar_botao
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
                                command= self.apagartudo
                            )
        self.Salvar = Button(
                    self.FrameGrid,
                    text="Salvar Como",
                    width=12,
                    bg="#9C5592",
                    fg="#F2E9E4",
                    activeforeground="#F2E9E4",
                    activebackground="#703892",
                    font=("Arial", 12, "bold"),
                    command=self.criar_arquivo
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
        self.Salvar.grid(row=0, column=7, padx=5, pady=5)

        # ----------- Butoes --------------------
        # -------------- Caixas de Selecao --------------
        self.TXTLinha.grid(row=0, column=8, padx=1, pady=5)
        self.BotaoCorLinha.grid(row=0, column=9, padx=5, pady=5)

        self.TXTPreenchimento.grid(row=0, column=10, padx=1, pady=5)
        self.BotaoCorPreenchimento.grid(row=0, column=11, padx=5, pady=5)

        self.TXTEspessura.grid(row=0, column=12, padx=1, pady=5)
        self.Espessura.grid(row=0, column=13, padx=5, pady=5)
        # -------------- Caixas de Selecao --------------
        self.janela.withdraw()
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

    def mudar_botao(self):
        self.controller.mudar_controlador()
        self.controller.verificarpoligono()
    def apagartudo(self):
        self.controller.figuras=[]
        self.CanvaGrid.delete("all")
    def criar_arquivo(self):
        self.controller.caminho=asksaveasfilename(defaultextension=".chdd",filetypes=[("Arquivos Cheddar", "*.chdd")])
        with open(self.controller.caminho, "w") as chdd:
            for c in self.controller.figuras:
                chdd.write(c+"|")
