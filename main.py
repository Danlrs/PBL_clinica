"""
Autor: Daniel Lucas Rios da Silva
Componente Curricular: EXA 854 - MI - Algoritmos
ConcluÍdo em: INFORME A DATA DE CONCLUSÃO
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

Sistema operacional: Windows
"""
import re
from time import sleep
from gerenciar import *
from recepcao import *
from dentista import *
from clientes import *
from sessoes import *
from consultas import * 


def validar_rg():       #Verifica se o rg digitado está no formato correto
    verificador = False
    formato_rg = re.compile(r'^\d{7,9}-?\d$')
    while not verificador:
        identidade = input("RG do paciente: \n->")
        if formato_rg.match(identidade):
            return identidade
        else:
            print("Formato incorreto!")
    

def verificar_data():   #Verifica se a data digitada está no formato correto
    verificador = False
    formato_data = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    while not verificador:
        dia = input("Informe a data da sessão no formato (dd/mm/aaaa): \n->")
        if formato_data.match(dia):
            return dia
        else:
            print("Formato incorreto!")
    

def verificar_hora():       #Verifica se a hora digitada está no formato correto
    verificador = False
    formato_hora = re.compile(r'^([01]\d|2[0-3]):[0-5]\d$')
    while not verificador:
        horario = input("Informe o horário no formato HH:MM: \n->")
        if formato_hora.match(horario):
            return horario
        else:
            print("Formato incorreto!")


pacientes = []
sessoes = []
consultas = []
fila_de_atendimento = []
#Instanciando um objeto Gerenciar preenchendo os argumentos com listas vazias
obj = Gerenciar(pacientes, sessoes, consultas, fila_de_atendimento)
loop = True
while(loop):        #Loop principal do código
    #carregando os dados presentes em arquivos JSON
    obj.carregar_pacientes('pacientes.json')
    obj.carregar_sessoes('sessoes.json')
    obj.carregar_consultas('consultas.json')
    contador = int(obj.get_maior_id()) + 1

    usuario = str(input("Quem está acessando? \n1) Recepção \n2) Dentista \n0) Sair \n\n-> "))
    if(usuario == '1'):
        #Menu recepção
        recepcao = True
        while (recepcao == True):
            print("""\n        <Menu Recepção>:\n
1)  Adicionar nova sessão clínica
2)  Listar sessões clínicas
3)  Buscar sessão clínica
4)  Iniciar sessão clínica
5)  Adicionar novo paciente
6)  Marcar horário para paciente
7)  Listar horários marcados do paciente
8)  Confirmar se paciente está marcado para sessão atual
9)  Colocar paciente na fila de atendimento
10) Listar próximo paciente da fila de atendimento
11) Listar consultas realizadas numa sessão clínica
M)  Voltar ao menu inicial
0)  Sair\n\n""")
            funcao = str(input("-> "))
            if(funcao == '1'):      #Adiciona sessão
                iD = str(contador)
                data = verificar_data()
                hora = verificar_hora()
                validador = False
                while not validador:
                    duracao = int(input("Informe quantas horas vai durar a sessão: \n->"))
                    if(duracao < 3 or duracao > 8):
                        print("A sessão deve durar entre 3 a 8h.")
                    else:
                        validador = True
                        dados = input("Mais informações: (opcional, aperte enter se não for necessário) \n->")
                        obj.add_sessao(iD, data, hora, duracao, dados)
                        obj.salvar_sessoes('sessoes.json')
                        contador+=1
                        print("Sessão adicionada.")
                validador = False
            elif(funcao == '2'):     #Lista as sessões
                print("<Lista de sessões Clínicas>")
                obj.listar_sessoes()
            elif(funcao == '3'):    #Buscando uma sessão
                print("<Buscar sessão>")
                data = verificar_data()
                hora = verificar_hora()
                obj.buscar_sessao(data, hora)
            elif(funcao == '4'):       #Inicia uma sessão
                print("<Iniciar sessão>")     
                data = verificar_data()
                hora = verificar_hora()
                obj.iniciar_sessao(data, hora)
            elif(funcao == '5'):      #Cadastra um paciente
                print("<Cadastro de paciente>")
                nome = input("Nome do paciente: \n->")
                rg = validar_rg()
                dados = input("Dados opcionais: (Opcional, aperte enter se não for necessário) \n->")
                if (obj.add_paciente(nome, rg, dados)):
                    obj.salvar_pacientes('pacientes.json')
            elif(funcao == '6'):     #Marca horário para o paciente
                print("<Marcar horário>")
                rg = validar_rg()
                iD = input("Informe o id da sessão desejada: \n->")
                if iD.isdigit():
                    if (obj.marcar_horario(rg, iD)):
                        obj.salvar_consultas("consultas.json")
                else:
                    print("O id deve ser numérico!")
            elif(funcao == '7'):      #Lista os horários marcados do paciente
                print("<Horários marcados>")
                rg = validar_rg()
                obj.listar_horarios(rg)
            elif(funcao == '8'):      #Confirma se o paciente está agendado para esse horário
                print("<Confirmar paciente>")
                rg = validar_rg()
                obj.confirmar_horario(rg, obj.get_id())
            elif(funcao == '9'):        #Coloca o paciente na lista de espera
                print("<Colocar paciente na fila de atendimento>")
                rg = validar_rg()
                obj.colocar_na_fila(rg, obj.get_id())
            elif(funcao == '10'):       #Lista o próximo paciente
                print("<Listar próximo paciente>")
                obj.proximo_paciente()
            elif(funcao == '11'):       #Exibe as consultas realizadas na sessão
                print("<Lista de consultas realizadas>")
                iD = input("Informe o id da sessão desejada: \n->")
                if iD.isdigit():
                    obj.listar_consultas(iD)
                else:
                    print("O id deve ser numérico!")
            elif(funcao == 'M' or funcao == 'm'):   #Volta ao menu inicial
                usuario = '2'
                recepcao = False
            elif(funcao == '0'):    #Fecha o programa
                recepcao = False
                loop = False
                print("Obrigado por usar o programa!")
            else:
                print("Opção inexistente!")
                sleep(1.5)
    elif(usuario == '2'):       #Menu Dentista
        dentista = True
        while (dentista):
            print("""\n       <Menu Dentista>\n
1) Buscar sessão clínica
2) Iniciar sessão clínica
3) Atender próximo paciente
4) Ler prontuário completo do paciente atual
5) Ler primeira anotação do paciente atual
6) Ler última anotação do paciente atual
7) Anotar prontuário do paciente atual
M) Voltar ao menu inicial
0) Sair\n\n""")
            funcao = input("-> ")
            if(funcao == '1'):      #Busca sessão
                print("<Buscar sessão>")
                data = verificar_data()
                hora = verificar_hora()
                obj.buscar_sessao(data, hora)
            elif(funcao == '2'):        #Inicia sessão, passando True para o parâmetro de ser iniciada pelo dentista
                print("<Iniciar sessão>")
                data = verificar_data()
                hora = verificar_hora()
                obj.iniciar_sessao(data, hora, True)
            elif(funcao == '3'):        #Chama o próximo paciente
                print("<Atender próximo paciente>")
                obj.atender_paciente()
            elif(funcao == '4'):        #Mostra o prontuário completo do paciente
                print("<Ler prontuário completo>")
                obj.ler_prontuario()
            elif(funcao == '5'):        #Mostra a primeira anotação do paciente
                print("<Ler primeira anotação>")
                obj.ler_primeira_anotacao()
            elif(funcao == '6'):        #Mostra a última anotação do paciente
                print("<Ler Anotação mais recente>")
                obj.ler_ultima_anotacao()
            elif(funcao == '7'):        #Anota o prontuário do paciente
                print("<Anotar prontuário>")
                obj.anotar_prontuario()
                obj.salvar_pacientes('pacientes.json')
            elif(funcao == 'M' or funcao == 'm'):       #Volta ao menu inicial
                usuario = '1'
                dentista = False
            elif(funcao == '0'):        #Fecha o programa
                dentista = False
                loop = False
                print("Obrigado por usar o programa!")
            else:
                print("Opção inexistente!")
                sleep(1.5)
    elif(usuario == '0'):       #Fecha o programa
        dentista = False
        recepcao = False
        loop = False
        print("Obrigado por usar o programa!")
    else:   
        print("Opção inexistente!")
        sleep(1.5)