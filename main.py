from controller import *
from view import Janela
janelaPrincipal=Janela()
controller = Controller(janelaPrincipal)
janelaPrincipal.controller = controller
JanelaPergunta=JanelaPergunta(janelaPrincipal)
janelaPrincipal.janela.mainloop()
