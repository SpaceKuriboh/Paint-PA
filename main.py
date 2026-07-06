from controller import *
from view import Janela

janelaPrincipal = Janela()
controller = Controller(janelaPrincipal)
janelaPrincipal.controller = controller
janelaPrincipal.janela.mainloop()