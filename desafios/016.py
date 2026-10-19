# Sistema para cadastro de funcionário
class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Meu nome é {self.nome}, trabalho no setor {self.setor} com o cargo {self.cargo}"

func = Funcionario(nome="Yuri", setor="TI", cargo="Desenvolvedor")
print(func.apresentar())