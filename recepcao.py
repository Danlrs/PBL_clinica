from datetime import datetime
from sessoes import *
from clientes import *
from consultas import *
class Recepcao:
    
    def __init__(self, pacientes: list, sessoes: list, consultas: list, fila_de_atendimento: list):
        self.pacientes = pacientes                #Definindo o construtor da classe
        self.sessoes = sessoes
        self.consultas = consultas
        self.fila = fila_de_atendimento


    def add_sessao(self, iD, data, hora, duracao, outros_dados = ""):  #Método utilizado para a recepção criar outra sessão
        s = Sessoes(iD, data, hora, duracao, outros_dados)
        self.sessoes.append(s)


    def listar_sessoes(self):   #Método para mostrar todas as sessões
        for s in self.sessoes:
            print(f"\n>\nId: {s.iD} \nData e horário: {s.data} às {s.hora} \nDuração: {s.duracao}")
            if(s.outros_dados != ""):
                print("Outros Dados: {s.outros_dados}\n")


    def add_paciente(self, nome, rg, outros_dados="", prontuario = []):    #Cria um objeto do tipo paciente, antes verificando se o rg
        for paciente in self.pacientes:                                    #desse paciente já está cadastrado
            if paciente.rg == rg:
                print("Já existe um paciente com esse rg!")
                return False
        novo_paciente = Pacientes(nome, rg, outros_dados, prontuario)
        self.pacientes.append(novo_paciente)
        print("Novo paciente cadastrado com sucesso.")
        return True

    
    def marcar_horario(self, rg, iD):      #Verifica se o paciente já está cadastrado, se a sessão na qual o paciente deseja marcar
        paciente_cadastrado = None         #horário existe, e se ela já ocorreu. Se a sessão e o paciente já estiverem cadastrados
        for paciente in self.pacientes:    #e a sessão não tiver ocorrido ainda, o horário é marcado.
            if paciente.rg == rg:
                paciente_cadastrado = paciente

        if not paciente_cadastrado:
            print("Paciente não encontrado.")
            return False

        sessao_encontrada = None
        for sessao in self.sessoes:
            print(f"ID da sessão: {sessao.iD}, ID procurado: {iD}")
            if str(sessao.iD) == iD:
                sessao_encontrada = sessao

        if not sessao_encontrada:
            print("Sessão não encontrada.")
            return False

        data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        data_hora_sessao = f"{sessao.data} {sessao.hora}"
        if data_hora_sessao < data_hora_atual:
            print("Sessão encerrada. Não é possível marcar horário nela")
            return False

        nova_consulta = Consultas(paciente_cadastrado, sessao_encontrada)
        self.consultas.append(nova_consulta)
        print(f"Horário marcado para o paciente {paciente_cadastrado.nome} na sessão {iD}.")
        return True


    def listar_horarios(self, rg):      #Verifica se o paciente existe, cria uma lista vazia de consultas, e acrescenta as consultas 
        paciente_cadastrado = False     #do paciente nela. Se a lista continuar vazia, mostra que o paciente não tem horários marcados
        for paciente in self.pacientes: #se estiver preenchida, mostra os horários.
            if paciente.rg == rg:
                paciente_cadastrado = True

        if not paciente_cadastrado:
            print("Paciente não encontrado.")
            return

        consultas_paciente = []
        for consulta in self.consultas:
            if consulta.paciente.rg == rg:
                consultas_paciente.append(consulta)

        if consultas_paciente:
            print(f"Horários agendados do paciente {consultas_paciente[0].paciente.nome}:")
            for consulta in consultas_paciente:
                print(
                    f"{consulta.sessao.data} {consulta.sessao.hora} - Sessão {consulta.sessao.iD} "
                    f"({consulta.sessao.duracao} horas)"
                )
        else:
            print(f"O paciente {paciente.nome} não possui horários marcados.")


    def confirmar_horario(self, rg, iD):    #Verifica a existência do paciente, se o rg do paciente associado a consulta é igual ao
        paciente_cadastrado = None          #informado, e se o id da sessão atual é igual ao id da sessão que o paciente tem consulta
        for paciente in self.pacientes:     #agendada. Se estiver tudo certo, informa que o paciente está agendado.
            if paciente.rg == rg:
                paciente_cadastrado = paciente

        if not paciente_cadastrado:
            print("Paciente não encontrado.")
            return

        consulta_encontrada = None
        for consulta in self.consultas:
            if consulta.sessao.iD == iD and consulta.paciente.rg == rg:
                consulta_encontrada = consulta

        if consulta_encontrada:
            print(f"{paciente_cadastrado.nome} tem agendamento na sessão de {consulta_encontrada.sessao.data} às {consulta_encontrada.sessao.hora}.")
        else:
            print(f"{paciente_cadastrado.nome} não está agendado para esta sessão.")


    def colocar_na_fila(self, rg, iD):     #Verifica a existência do paciente, e se o paciente tem consulta agendada na sessão atual.
        paciente_cadastrado = False        #Se estiver, adiciona ele à lista de espera. Se não estiver, vai dizer que ele não tem horário marcado.
        consulta_encontrada = False

        for paciente in self.pacientes:
            if paciente.rg == rg:
                paciente_cadastrado= True

        if not paciente_cadastrado:
            print("Paciente não encontrado.")
            return

        for consulta in self.consultas:
            if consulta.sessao.iD == iD and consulta.paciente.rg == rg:
                consulta_encontrada = True

        if not consulta_encontrada:
            print(f"{paciente.nome} não está marcado para a sessão atual.")
            return
        
        for consulta in self.consultas:
            if consulta.sessao.iD == iD and consulta.paciente.rg == rg:
                self.fila.append(consulta)
                print(f"{paciente.nome} foi adicionado à fila de atendimento da sessão de {consulta.sessao.data} às {consulta.sessao.hora}.")
                break


    def proximo_paciente(self):     #Verifica se a fila de atendimento está vazia, se não estiver, atriubui o primeiro paciente que foi 
        if not self.fila:           #adicionada na lista de espera à váriável proximo_paciente, e informa qual o próximo paciente para o usuário
            print("A fila de atendimento está vazia.")
            return

        proximo_paciente = self.fila[0]
        paciente = proximo_paciente.paciente
        sessao = proximo_paciente.sessao
        print(f"Próximo paciente: \nPaciente: {paciente.nome} \nSessão: {sessao.data} às {sessao.hora}")


    def listar_consultas(self, iD):#Cria uma lista vazia para armazenar as consultas existentes na sessão atual, e mostra as consultas 
        consultas_sessao = []      #ao usuário. Se não houver consultas na sessão, informa que não foram realizadas consultas.
        for consulta in self.consultas:
            if consulta.sessao.iD == iD:
                consultas_sessao.append(consulta)

        if not consultas_sessao:
            print(f"Nenhuma consulta realizada na sessão clínica com ID {iD}.")
        else:
            print(f"Consultas realizadas na sessão clínica com ID {iD}:")
            for consulta in consultas_sessao:
                print(f">\nPaciente: {consulta.paciente.nome} \nData: {consulta.sessao.data} \nHorário: {consulta.sessao.hora} \n>\n")
