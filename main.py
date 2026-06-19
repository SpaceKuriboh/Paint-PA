from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox


def iniciarforma(event):
    global xi, yi
    xi = event.x
    yi = event.y

def desenhar(xi, yi , xf , yf , Forma, temp):

    #Verifica se e para desnhar ou se e temporario

    if temp:
        tag = "temp"
    else:
        tag = None
    
    if Forma == "linha":
        CanvaGrid.create_line(
            xi, yi , xf , yf,
            fill = CoresLinha.get(),
            tags = tag,
            width = 3
        )
    
    elif Forma == "retangulo":
        CanvaGrid.create_rectangle(
            xi , yi , xf, yf,
            fill = CoresPreenchimento.get(),
            outline = CoresLinha.get(),
            tags = tag,
            width = 3
        )
    
    elif Forma == "circulo":
        CanvaGrid.create_oval(
            xi, yi , xf, yf,
            fill =  CoresPreenchimento.get(),
            outline = CoresLinha.get(),
            tags = tag,
            width = 3
        )


def atualizarforma(event):
    xf = event.x
    yf = event.y
    CanvaGrid.delete("temp")
    desenhar(xi, yi, xf, yf, forma.get(), True)
    
def gravarforma(event):
    xf = event.x
    yf = event.y
    CanvaGrid.delete("temp")
    desenhar(xi, yi , xf , yf , forma.get(), False)


# ----------- Main ----------------

xi, xf, yi, yf = 0, 0, 0, 0

janela = Tk()
janela.title("Paint 2.0 ULTRA BLASTER SUPER EXTRA CHEDDAR PLUS PLUS PLUS")
forma = StringVar()

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

DesenharRetangulos = Radiobutton(
    FrameGrid,
    text="▯",
    width=5,
    indicatoron=False,
    variable=forma,
    value="retangulo",
    bg="lightgrey",
)
DesenharRetangulos.grid(row=0, column=1, padx=5, pady=5)

DesenharOvais = Radiobutton(
    FrameGrid,
    text="O",
    width=5,
    indicatoron=False,
    variable=forma,
    value="circulo",
    bg="lightgrey",
)
DesenharOvais.grid(row=0, column=2, padx=5, pady=5)

ApagarTudo = Button(
    FrameGrid,
    text="Apagar Tudo",
    width=12,
    bg="lightgrey",
    command=lambda: CanvaGrid.delete("all"),
)
ApagarTudo.grid(row=0, column=3, padx=5, pady=5)
ApagarTudo.grid(row=0, column=3, padx=5, pady=5)

# --------------------- Caixas de Selecao --------------------------

TXTLinha = Label(FrameGrid, text="Cor da Linha: ")
TXTLinha.grid(row=0, column=4, padx=1, pady=5)
CoresLinha = Combobox(
    FrameGrid,
    values=["blue", "red", "green", "yellow", "purple", "pink", "black"],
    state="readonly",
    width=10,
)
CoresLinha.grid(row=0, column=5, padx=5, pady=5)

TXTPreenchimento = Label(FrameGrid, text="Cor do Preenchimento: ")
TXTPreenchimento.grid(row=0, column=6, padx=1, pady=5)
CoresPreenchimento = Combobox(
    FrameGrid,
    values=["blue", "red", "green", "yellow", "purple", "pink", "black"],
    state="readonly",
    width=10,
)
CoresPreenchimento.grid(row=0, column=7, padx=5, pady=5)

# ----------------- Definindo Opcoes Iniciais -------------------

CoresLinha.set("black")
CoresPreenchimento.set("black")

CanvaGrid.bind("<ButtonPress-1>", iniciarforma)
CanvaGrid.bind("<B1-Motion>", atualizarforma)
CanvaGrid.bind("<ButtonRelease-1>", gravarforma)

janela.mainloop()