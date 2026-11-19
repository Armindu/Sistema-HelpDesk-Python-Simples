#Criando o menu de entrada e saida
def menu():
    print('\n~~~~ SISTEMA DE CHAMADOS ~~~~')
    print('1 - Abrir chamado')
    print('2 - Listar chamados')
    print('3 - Atualizar chamado')
    print('4 - Encerrar')

#Variaveis que serão utilizadas varias vezes no projeto
proximo_id = 1
chamados = []

#Função que abre o chamado
def abrir_chamado():
    #Tornando a variavel global para não perder ela e conseguir utilizar em varios locais
    global proximo_id

    cliente = str(input('Nome do cliente? '))
    problema = str(input('Descreva o problema? '))

    #Dicionario com as informações importantes
    chamado = {
        'id': proximo_id,
        'nome': cliente,
        'problema': problema,
        'status': 'Aberto'
    }
    #Adicionando cada chamado na lista de chamados
    chamados.append(chamado)
    proximo_id += 1
    
    return print('Chamado registrado com sucesso!')
#Função para mostrar quantos chamados tem
def listar_chamado():
    if len(chamados) == 0: #O len conta quantos chamados tem na lista
        print('~'*13),
        print('Sem chamados')
        print('~'*13)
        return

    for chamado in chamados:
        formato = len(chamado['problema']) + 12 #conta quantos caracteres tem e adiciona 12
        print('~'*formato),
        print(f'Id: {chamado['id']}')
        print(f'Cliente: {chamado['nome']}')
        print(f'Problema: {chamado['problema']}')
        print(f'Status: {chamado['status']}')
        print('~'*formato)

def atualizar_chamado():
    listar_chamado()

    if len(chamados) == 0:
        return
    
    else:
        try:
            id_chamado = input('\nDigite o ID do chamado: ')

        except ValueError:
            print('Id inválido')
            return

        for chamado in chamados:
            if chamado['id'] == id_chamado:
                status = input('Digite o novo status: ')
                chamado['status'] = status
                print('Chamado atualizado com sucesso!')
                return
            print('Chamado não encontrado.')

while True:
    menu()
    opcao = int(input('Digite o número da opção: '))

    if opcao == 1:
        abrir_chamado()

    elif opcao == 2:
        listar_chamado()

    elif opcao == 3:
        atualizar_chamado()

    elif opcao == 4:
        print('Encerrando sistema...')
        break
    else:
        print('Opção inválida!')
