from typing import Dict, Union

def exemplo_dicionario_basico():
     #Dicionário é uma forma de armazenar chaves e valores
     #Cada chave está atrelado a um valor

     #Dicionario terá uma chave do tipo string
     #Pode armazenar string, int ou bool
     #Criarmos um dicionário com 2 chaves (apelido, idade)
     cachorro: Dict[str, Union[str, int, bool, float]] = {
        "apelido": "Tobby",
        "idade": 4,
        "abandonado": True,
        "peso": 22.5
     }

     #Acrescentar uma nova chave com um valor 
     cachorro["raca"] = "Pastor Alemão"

     cachorro["cor"] = "Caramelo"

     #Alterar o valor de uma chave
     cachorro["idade"] = 5

     #Remover uma chave(automaticamente remove o valor)
     cachorro.pop("abandonado")

     # print("Cachorro:", cachorro["apelido"])
     print(f"""
     Cachorro: [cachorro.get("apelido")
     Raça: {cachorro.get("raca")}
     Idade: {cachorro.get("idade")}
     Cor: {cachorro.get("cor")}
     Abandonado: {cachorro.get("abandonado")}
     Peso: {cachorro.get("peso")}""")


     #--------------exercicio-----------


def exemplo_dicionario_aluno():

    aluno = {
        "nome_completo": "Vanderlei Bandeira",
        "nome_mae": "Maria",
        "nome_pai": "João",
        "jogar": True
    }

    print("\nDados iniciais:")
    print(aluno)

    aluno["idade"] = 25

    print("\nIdade atual:")
    print("Idade:", aluno["idade"])

    aluno["idade"] = aluno["idade"] + 1

    aluno.pop("jogar")

    print("\nDados finais:")
    print(aluno)
