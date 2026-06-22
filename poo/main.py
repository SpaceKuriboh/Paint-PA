from poo import *
# ----------- Main ----------------
janela = Tk()
janela.title("Paint 2.0 ULTRA BLASTER SUPER EXTRA CHEDDAR PLUS PLUS PLUS")
forma = StringVar(janela)
objeto=void()
formas = {
    "retangulo": Retangulo,
    "oval": Oval,
    "circulo": Circulo,
    "livre": Livre,
    "linha": Reta,
    "poligono":Poligono
}

# ----------- Fazendo a Barra de Escolhas -----------

FrameGrid = Frame(janela, bg="lightgray", borderwidth=3, relief="flat")
FrameGrid.grid(row=0, column=0, sticky="ew")

CanvaGrid = Canvas(
    janela, bg="white", width=1920, height=1080, borderwidth=3, relief="ridge"
)
CanvaGrid.grid(row=1, column=0)

# ------------------ Botoes ------------------------

DesenharLinhas = Radiobutton(
    FrameGrid,
    text="/",
    width=5,
    indicatoron=False,
    variable=forma,
    value="linha",
    bg="lightgrey",
)
DesenharLinhas.grid(row=0, column=0, padx=5, pady=5)


DesenharLivre = Radiobutton(
    FrameGrid,
    text="~",
    width=5,
    indicatoron=False,
    variable=forma,
    value="livre",
    bg="lightgrey",
)
DesenharLivre.grid(row=0, column=1, padx=5, pady=5)


DesenharRetangulos = Radiobutton(
    FrameGrid,
    text="▯",
    width=5,
    indicatoron=False,
    variable=forma,
    value="retangulo",
    bg="lightgrey",
)
DesenharRetangulos.grid(row=0, column=2, padx=5, pady=5)

DesenharCirculos = Radiobutton(
    FrameGrid,
    text="O",
    width=5,
    indicatoron=False,
    variable=forma,
    value="circulo",
    bg="lightgrey",
)
DesenharCirculos.grid(row=0, column=3, padx=5, pady=5)

DesenharPoligonos = Radiobutton(
    FrameGrid,
    text="◊",
    width=5,
    indicatoron=False,
    variable=forma,
    value="poligono",
    bg="lightgrey",
)
DesenharPoligonos.grid(row=0, column=4, padx=5, pady=5)

DesenharOvais = Radiobutton(
    FrameGrid,
    text="⬭",
    width=5,
    indicatoron=False,
    variable=forma,
    value="oval",
    bg="lightgrey",
)
DesenharOvais.grid(row=0, column=5, padx=5, pady=5)

ApagarTudo = Button(
    FrameGrid,
    text="Apagar Tudo",
    width=12,
    bg="lightgrey",
    command=lambda: CanvaGrid.delete("all"),
)
ApagarTudo.grid(row=0, column=6, padx=5, pady=5)

# --------------------- Caixas de Selecao --------------------------

TXTLinha = Label(FrameGrid, text="Cor da Linha: ")
TXTLinha.grid(row=0, column=7, padx=1, pady=5)
CoresLinha = Combobox(
    FrameGrid,
    values=["blue", "red", "green", "yellow", "purple", "pink", "black"],
    state="readonly",
    width=10,
)
CoresLinha.grid(row=0, column=8, padx=5, pady=5)

TXTPreenchimento = Label(FrameGrid, text="Cor do Preenchimento: ")
TXTPreenchimento.grid(row=0, column=9, padx=1, pady=5)
CoresPreenchimento = Combobox(
    FrameGrid,
    values=["blue", "red", "green", "yellow", "purple", "pink", "black"],
    state="readonly",
    width=10,
)
CoresPreenchimento.grid(row=0, column=10, padx=5, pady=5)

TXTEspessura = Label(FrameGrid, text="Selecione a Expessura: ")
TXTEspessura.grid(row=0, column=11, padx=1, pady=5)
Espessura = Combobox(
    FrameGrid,
    values=['1', '2', '3', '4', '5', '6', '7', '8'],
    state="readonly",
    width=10,
)
Espessura.grid(row=0, column=12, padx=5, pady=5)
# ----------------- Definindo Opcoes Iniciais -------------------
CoresLinha.set("black")
CoresPreenchimento.set("black")
Espessura.set(4)

def iniciarforma(event):
    global forma, objeto
    if (forma.get()=="poligono" and not isinstance(objeto,Poligono)) or forma.get()!="poligono":
        xi = event.x
        yi = event.y
        objeto = formas[forma.get()](
            CanvaGrid,
            xi, yi, xi, yi,
            CoresLinha.get(),
            int(Espessura.get()),
            fill=CoresPreenchimento.get(),
            temp=True
        )
    else:
        if objeto.marcarponto(event):
            objeto=void()
def atualizar(event):
    global objeto
    objeto.atualizarforma(event)
def atualizarpoligono(event):
    global objeto
    if isinstance(objeto, Poligono):
        objeto.atualizarforma(event)
def gravar(event):
    if forma.get()!="poligono":
        global objeto
        objeto.gravarforma(event)
CanvaGrid.bind("<ButtonPress-1>", iniciarforma)
CanvaGrid.bind("<B1-Motion>", atualizar)
CanvaGrid.bind("<Motion>", atualizarpoligono)
CanvaGrid.bind("<ButtonRelease-1>", gravar)

janela.mainloop()