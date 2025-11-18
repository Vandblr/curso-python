classs Conta:
    def __init__(self, titular: str, saldo_inicial: float):
        """Construtor da classe. Inicializa o titular e o saldo"""
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor_deposito: float):
        """Adiciona um valor ao saldo da conta."""
        if valor_deposito <= 0:
            print(f"DEPÓSITO: Valor de depósito inválido R${valor_deposito>:.2f}")
            return

           self.saldo = self.saldo + valor_deposito
           print(f"DEPÓSITO: Depósito de R${Valor:.f} realizado com sucesso") 
    
    def sacar(self, valor_saque: float):
        """Remove um valor do saldo da conta, se houver dinheiro suficiente."""
        if valor_saque > self.saldo:
            print(f"SAQUE: Saldo insuficiente para realizar o sque de R${valor_saque:.f}")
            else:
                self.saldo = self.saldo - valor_saque
                print(f"SAQUE: Saque de R${valor_saque:.f} realizado com sucesso")
    
    def exibir_saldo(self):
        """Mostrar o status atual da conta."""
        print(f"EXTRATO: Saldo atual de R${self.saldo:.2f}")



def exemplo_conta():
    """Método para testar a funcionalidade da conta"""
    conta_bradesco = Conta("Vitor", 3900,22)

    conta_bradesco.exibir_saldo()
    conta_bradesco.sacar(800) # 3100.22
    
    conta_bradesco.exibir_saldo()
    conta_bradesco.depositar(100.78) # 3201
    conta_bradesco.depositar(-10)

    conta_bradesco.sacar(4000) # Não permitir pois daldo insuficiente

    conta_bradesco.sacar(3500) # Não permitir pois daldo insuficiente
    conta_bradesco.sacar(3201)
    conta_bradesco.exibir_saldo()


exemplo_conta()



class Aluno:
    def __init__(self, nome: str):
        self.nome = nome
        self.notas = [] 

    def adicionar(self, nota: float):
        self.notas.append(nota)

    def apresentar_notas(self):
        print("Notas do aluno:", self.notas)

    def calcular_media(self):
        soma = 0
        for n in self.notas:
            soma = soma + n
        return soma / len(self.notas)


def exemplo_aluno():
    
    vanderlei = Aluno("Vanderlei")

    vanderlei.adicionar(9.0)
    vanderlei.adicionar(8.7)
    vanderlei.adicionar(9.4)
    vanderlei.apresentar_notas()

    media = vanderlei.calcular_media()

    print(f"A média do aluno {vanderlei.nome} é: {media:.2f}")



exemplo_aluno()




