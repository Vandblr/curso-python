from typing import List

class Aluno:
    def __init__(
        sef,
        nome: str,
        notas: List[float],
        frequencia: float = 75,
        turma: str = "SuperDev",
    ):
        
        self.nome = nome
        self.notas  = notas
        self.frequencia = frequencia
        self.turma = turma

def exemplo_passagem_parametros_nomeados():
    # Pedro terá a freuqncoa de 75%, pq foi utilizado o volaor de default do
    # parametro de freuencia
    # 2 parâmetros seguindo a ordem do construtor e outro parâmetro pelo
    # nome (turma)
    pedro = Aluno(
        "Pedro Silva",
        [8,7,6.5],
        turma="SuperDev 7",
    )

    # Passando todos os parâmetro pelo nome, podendo passar em qualquer ordem
    maria = Aluno(
        notas=[10, 9.75, 3],
        nome="Maria",
        turma="Adas",
        frequencia=100,
    )

class Player:
    def __init__(nick: str = "Wudseven7")