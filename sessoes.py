class Sessoes:

    def __init__(self, iD, data, hora, duracao, outros_dados = ""): #Definindo o construtor da classe
        self.iD = iD
        self.data = data
        self.hora = hora
        self.duracao = duracao
        self.outros_dados = outros_dados


    def to_dict(self):  #Converte um objeto Sessao em um dicionário
        return{
            'iD': self.iD,
            'data': self.data,
            'hora': self.hora,
            'duracao': self.duracao,
            'outros_dados': self.outros_dados
        }
    

    @classmethod
    def from_dict(cls, dict_info):   #Cria um objeto Sessao a partir de um dicionário de informações
        iD = dict_info['iD'] if 'iD' in dict_info else ''
        data = dict_info['data'] if 'data' in dict_info else ''
        hora = dict_info['hora'] if 'hora' in dict_info else ''
        duracao = dict_info['duracao'] if 'duracao' in dict_info else ''
        outros_dados = dict_info['outros_dados'] if 'outros_dados' in dict_info else ''
        return cls(iD, data, hora, duracao, outros_dados)