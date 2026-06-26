from controller import Controller
from view import Janela

janelaPrincipal = Janela()
controller = Controller(janelaPrincipal)
Janela.controller=controller
janelaPrincipal.janela.mainloop()
