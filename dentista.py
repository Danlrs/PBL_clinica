from sessoes import *
from clientes import *
from consultas import *
class Dentista:

    def __init__(self, pacientes: list, sessoes: list, consultas: list, fila_de_atendimento: list): #Definindo o construtor da classe
        self.pacientes = pacientes
        self.sessoes = sessoes
        self.consultas = consultas
        self.fila = fila_de_atendimento
        self.sessao_atual = None
        self.consulta_atual = None
        self.anotacoes = {}


    def atender_paciente(self):     #Verifica se a fila está vazia, se não estiver vazia, remove o próximo paciente da fila e obtém suas
        if not self.fila:           #informações. Depois solicita ao dentista que faça uma anotação, e chama o método criar_primeira_anotacao().
            print("A fila de atendimento está vazia.")
            return

        proxima_consulta = self.fila.pop(0)
        paciente_atual = proxima_consulta.paciente
        sessao = proxima_consulta.sessao
        self.consulta_atual = proxima_consulta

        print(f"Atendendo próximo paciente da fila de atendimento. \nPaciente: {paciente_atual.nome} \nSessão: {sessao.data} às {sessao.hora}")
        print("Antes de finalizar o atendimento, registre uma anotação sobre a visita: ")
        anotacao = input("> ")
        self.criar_primeira_anotacao(paciente_atual.rg, anotacao)


    def ler_prontuario(self):       #Verifica se tem algum paciente em atendimento, caso tenha, vai pegar os dados do paciente, e imprimir
        if not self.consulta_atual: #o prontuário completo.
            print("Nenhum paciente está em atendimento.")
            return
        paciente = self.consulta_atual.paciente
        print(f"Prontuário completo do paciente {paciente.nome}:")
        for anotacao in paciente.prontuario:
            print(f"Anotação: {anotacao['anotacao']}")

    
    def criar_primeira_anotacao(self, rg, anotacao):     #Verifica se há um paciente em atendimento, caso tenha, verifica se o paciente
        if not self.consulta_atual:                     #já tem alguma anotação registrada. Se não tiver, cria a primeira, e se tiver
            print("Nenhum paciente está em atendimento.")   #acrescenta mais uma.
            return
        if rg not in self.anotacoes:
            self.anotacoes[rg] = [anotacao]
            print("Primeira anotação registrada.")
        else:
            self.anotacoes[rg].append(anotacao)
            print("Anotação registrada.")


    def ler_primeira_anotacao(self):                         #Verifica se há um paciente em atendimento, caso tenha, pega os dados do 
        if not self.consulta_atual:                          #paciente,e verifica se ele tem alguma anotação registrada. Se tiver,
            print("Nenhum paciente está em atendimento.")    #vai mostrar a primeira anotação. Se não tiver, vai dizer que não tem.
            return
        paciente = self.consulta_atual.paciente
        rg = paciente.rg

        if rg not in self.anotacoes or not self.anotacoes[rg]:
            print("Nenhuma anotação registrada desse paciente.")
        else:
            primeira_anotacao = self.anotacoes[rg][0]
            print(f"Primeira anotação do paciente {paciente.nome}: ", primeira_anotacao)


    def ler_ultima_anotacao(self):                          #Verifica se há um paciente em atendimento, caso tenha, pega os dados do
        if not self.consulta_atual:                         #paciente,e verifica se ele tem alguma anotação registrada. Se tiver,
            print("Nenhum paciente está em atendimento.")   #vai mostrar a última anotação. Se não tiver, vai dizer que não tem.
            return
        paciente = self.consulta_atual.paciente
        rg = paciente.rg

        if rg not in self.anotacoes or not self.anotacoes[rg]:
            print("Nenhuma anotação registrada desse paciente.")
        else:
            ultima_anotacao = self.anotacoes[rg][-1]
            print(f"Última anotação do paciente {paciente.nome}: ", ultima_anotacao)
        

    def anotar_prontuario(self):                              #Verifica se há um paciente em atendimento, caso tenha, pega os dados dele
        if not self.consulta_atual:                           #e solicita ao dentista para anotar o prontuário, e salva o prontuário num
            print("Nenhum paciente está em atendimento.")     #dicionário. Em seguida, verifica se o paciente já tinha um prontuário. Se
            return                                            #não tiver, cria um; caso tenha, acrescenta o novo prontuário no vetor.
        paciente = self.consulta_atual.paciente
        prontuario = input("Anotação do prontuário: ")
        anotacao = {"anotacao": prontuario}

        if "prontuario" not in paciente.to_dict():
            paciente.prontuario = [anotacao]
        else:
            paciente.prontuario.append(anotacao)
        print(f"Anotação registrada para o paciente {paciente.nome}.")