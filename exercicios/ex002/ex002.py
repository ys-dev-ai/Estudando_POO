# Declaração de classe
class Gafanhoto:
    def __init__(self, nome = "", idade = 0): # Construtor da Classe
        # Atributo de Instancia
        self.nome = nome
        self.idade = idade

        # Metodo de Instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} e Gafanhoto e tem {self.idade} anos de idade"

    # Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Yuri"
g1.idade = 30
g1.aniversario()
print(g1.mensagem())    

g2 = Gafanhoto()
g2.nome = "Gisele"
g2.idade = 37
g2.aniversario()
print(g2.mensagem())
