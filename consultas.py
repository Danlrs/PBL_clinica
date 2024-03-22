from clientes import Pacientes
from sessoes import Sessoes

class Consultas:
    def __init__(self, paciente, sessao):   #Definindo o construtor da classe
        self.paciente = paciente
        self.sessao = sessao
    

    def to_dict(self):  #Converte um objeto Consulta em um dicionário
        return{
            'paciente': self.paciente.to_dict(),
            'sessao': self.sessao.to_dict()
        }
    

    @classmethod
    def from_dict(cls, dict_info):     #Cria um objeto Consulta a partir de um dicionário de informações
        paciente_dict = dict_info['paciente'] if 'paciente' in dict_info else {}
        sessao_dict = dict_info['sessao'] if 'sessao' in dict_info else {}
        paciente = Pacientes.from_dict(paciente_dict)
        sessao = Sessoes.from_dict(sessao_dict)
        return cls(paciente, sessao)
