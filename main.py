from controller import Controller
from view import Janela

janelaPrincipal = Janela()
controller = Controller(janelaPrincipal)
janelaPrincipal.janela.mainloop()
