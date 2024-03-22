class Pacientes:

    def __init__(self, nome, rg, dados_opcionais = "", prontuario = []): #Definindo o construtor da classe
        self.nome = nome
        self.rg = rg
        self.dados_opcionais = dados_opcionais
        self.prontuario = prontuario
        

    def to_dict(self):    #Converte um objeto Paciente em um dicionário
        return {
            'nome': self.nome,
            'rg': self.rg,
            'dados_opcionais': self.dados_opcionais,
            'prontuario': self.prontuario
        }

    @classmethod
    def from_dict(cls, dict_info):    #Cria um objeto Paciente a partir de um dicionário de informações
        nome = dict_info['nome'] if 'nome' in dict_info else ''
        rg = dict_info['rg'] if 'rg' in dict_info else ''
        dados_opcionais = dict_info['dados_opcionais'] if 'dados_opcionais' in dict_info else ''
        prontuario = dict_info['prontuario']if 'prontuario' in dict_info else []
        paciente = cls(nome, rg, dados_opcionais, prontuario)
        return paciente