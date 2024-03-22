from recepcao import *
from dentista import *
import json
import os

class Gerenciar(Dentista, Recepcao):

    def __init__(self, pacientes: list, sessoes: list, consultas: list, fila_de_atendimento: list): #Definindo o construtor da classe
        self.pacientes = pacientes
        self.sessoes = sessoes
        self.consultas = consultas
        self.fila = fila_de_atendimento
        self.sessao_atual = None
        self.consulta_atual = None
        self.anotacoes = {}


    def buscar_sessao(self, data, hora):    #Pesquisa a sessão utilizando a data e horário
        for s in self.sessoes:
            if s.data == data and s.hora == hora:
                print(f"""\nSESSÃO ENCONTRADA: \n\nId: {s.iD} \nData: {s.data} \nHorário: {s.hora}
    Duração: {s.duracao}h """)
                if s.outros_dados:
                    print(f"Dados Adicionais: {s.outros_dados}")
                return
        else:
            print("Sessão não encontrada.")


    def iniciar_sessao(self, data, hora, iniciada_pelo_dentista=False):     #Verifica se já existe uma sessão clínica marcada para a data e hora especificadas,
        for sessao in self.sessoes:                                         #se existir e o horário atual permitir, inicia a sessão e define como a sessão atual.
            if sessao.data == data and sessao.hora == hora:                 #se não existir, informa para o usuário.
                data_hora_sessao = datetime.strptime(f"{sessao.data} {sessao.hora}", "%d/%m/%Y %H:%M")
                data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

                if data_hora_sessao < datetime.strptime(data_hora_atual, "%d/%m/%Y %H:%M"):
                    print("O período para iniciar essa sessão já expirou.")
                    return
                else:
                    if iniciada_pelo_dentista:
                        print("Sessão clínica foi iniciada pelo dentista.")
                    else:
                        print("Sessão clínica foi iniciada pela recepção.")
                    self.sessao_atual = sessao
                    return
        else:
            print("Sessão clínica inexistente na data e horário informados.")

    
    def get_id(self):   #retorna o id da sessão atual
        return self.sessao_atual.iD
    

    def get_maior_id(self):    #Retorna o maior ID entre todas as sessões se não houver sessões, retorna 0.
        if not self.sessoes:
            return 0
        maior_id = 0
        for sessao in self.sessoes:
            try:
                sessao_id = int(sessao.iD)
                maior_id = max(maior_id, sessao_id)
            except (ValueError, TypeError):
                pass  
        return maior_id
                                                #Os métodos abaixo são responsáveis por salvar os objetos no arquivo em formato JSON
                                                #e carregar os objetos de um arquivo JSON
    def salvar_sessoes(self, arquivo):
        with open(arquivo, 'w') as a:
            sessoes_dict = []
            for sessao in self.sessoes:
                sessoes_dict.append(sessao.to_dict())
            json.dump(sessoes_dict, a)


    def carregar_sessoes(self, arquivo):
        if os.path.exists(arquivo): 
            try:
                with open(arquivo, 'r') as a:
                    sessoes_dict = json.load(a)
                    self.sessoes = []
                    for dict_info in sessoes_dict:
                        self.sessoes.append(Sessoes.from_dict(dict_info))
            except:
                print("Não foi possível ler o arquivo")


    def salvar_pacientes(self, arquivo):
        with open(arquivo, 'w') as a:
            pacientes_dict = []
            for paciente in self.pacientes:
                pacientes_dict.append(paciente.to_dict())
            json.dump(pacientes_dict, a)

    
    def carregar_pacientes(self, arquivo):
        if os.path.exists(arquivo):
            try:
                with open(arquivo, 'r') as a:
                    pacientes_dict = json.load(a)
                    self.pacientes = []
                    for dict_info in pacientes_dict:
                        self.pacientes.append(Pacientes.from_dict(dict_info))
            except:
                print("Não foi possível ler o arquivo")


    def salvar_consultas(self, arquivo):
        with open(arquivo, 'w') as a:
            consultas_dict = []
            for consulta in self.consultas:
                consultas_dict.append(consulta.to_dict())
            json.dump(consultas_dict, a)


    def carregar_consultas(self, arquivo):
        if os.path.exists(arquivo):
            try:
                with open(arquivo, 'r') as a:
                    consultas_dict = json.load(a)
                    self.consultas = []
                    for dict_info in consultas_dict:
                        self.consultas.append(Consultas.from_dict(dict_info))
            except:
                print("Não foi possível ler o arquivo")