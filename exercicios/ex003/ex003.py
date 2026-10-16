class ContaBancaria:
    """"
Cria uma conta bancaria que permite fazer saques e depositos.
    """
    def __init__(self, id, nome, saldo = 0): # contrutor de classe
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} Criada com sucesso saldo atual R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Saque de R${valor:,.2f} autorizado da conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque de {valor:,.2f} NEGADO saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta{self.id}")
            

c1 = ContaBancaria(id=112, nome="Yuri", saldo=3000)
c1.depositar(500)
c1.sacar(5_000_000)          # Docstring da Classe (Coment
print(c1)