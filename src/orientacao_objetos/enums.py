class  enum import Enum


# region Console
class MarcaEnum(Enum)
      SONY = "Sony"
      MICROSOFT = "Microsoft"


class Console:
    def __init__(self)
    self.marca: MarcaEnum
    self.modelo: str =""


def exemplo_consoles():
    # Instanciar um objeto
    play_station = Console()
    play_station.marca = MarcaEnum.SONY
    play_station.modelo = "PS1"

    play_station_2 = Console()
    play_station_2.marca = MarcaEnum.SONY
    play_station_2.modelo = "PS2"

    xbox = Console()
    xbox.modelo = "Xbox"
    xbox.marca = MarcaEnum.MICROSOFT
# endregion



class PessoaTipo(Enum):
    FISICA = "PF"
    JURIDICA = "PJ"

class Pessoa:
    def __init__(self):
        self.nome: sts
        self.cpf_cnpj: str
        self.tipo: PessoaTipo
    

def exemplo_pessoas():
    creber = Pessoa()
    creber.nome = "Cleiton"
    creber.cpf_cnpj = "01.203.200/0001-20"
    creber.tipo =  PessoaTipo.JURIDICA

    print(
        "PESSOA",
        creber.nome,
        "CPF-CNPJ",
        creber.cpf_cnpj,
        "TIPO",
        creber.tipo.value,
    )

    if __name__ == "__main__":
        exemplo_pessoas()



        #-----exercicios--------

class PersonagemEnum(Enum):
    BATMAN = "Batman"
    SUPERMAN = "Superman"
    BUZZ = "Buzz Lightyear"
    HOMEM_FORMIGA = "Homem Formiga"
    BOB_ESPONJA = "Bob Esponja"
    CATDOG = "CatDog"


class Status(Enum):
    PEDNEDNTE = "Pendente"
    EM_ANDAMENTO = "Em Andamento"
    CANCELADO =  "Cancelado"
    FINALIZADO = "Finalizado"


def Job:
    def __init__(self):
        self.personagem PersonagemEnum = None
         self.valor: float = 2301.20
        self.local: str = "Blumenau"
        self.status: StatusEnum = None


def apresentar_jobs():
    job1 = Job(
        personagem=PersonagemEnum.BATMAN,
        valor=2301.20,
        local="Blumenau",
        status=StatusEnum.EM_ANDAMENTO,
    )

    job2 = Job(
        personagem=PersonagemEnum.BOB_ESPONJA,
        valor=5000.00,
        local="São Paulo",
        status=StatusEnum.FINALIZADO,
    )

    print(
        "JOB 1",
        job1.personagem.value,
        "VALOR:", job1.valor,
        "LOCAL:", job1.local,
        "STATUS:", job1.status.value
    )

    print(
        "JOB 2",
        job2.personagem.value,
        "VALOR:", job2.valor,
        "LOCAL:", job2.local,
        "STATUS:", job2.status.value
    )

