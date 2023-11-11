import os
from time import sleep

from classes.cliente import Cliente
from classes.utilitarios import *


# Inicializando uma lista onde ficaram todos os nossos clientes do tipo objeto Cliente da classe importada.
clientesCadastrados = []

# Usuários padrão, apague essa parte se preferir
meucli = Cliente('Godofredo','Rua dos Morangos',
                 '+5579998432756', '27/05/1988', 0, 'Corrente', 23459)
meucli1 = Cliente('Victoria','Rua das Pedras',
                  '+5579987436492','20/12/1999', 0, 'Poupança', 10000)
meucli2 = Cliente('Julius','Rua do Sol',
                  '+5579987435628', '01/01/01', 0, 'Corrente', 4500)
clientesCadastrados.append(meucli)
clientesCadastrados.append(meucli1)
clientesCadastrados.append(meucli2)

sistema_ativo = True
while sistema_ativo:
    boasVindas('BEM-VINDO')
    print('[0] Para sair')
    navegacao = criarMenuDeNavegacao()
    if navegacao == '0':
      sistema_ativo = False

    # Cadastro de novos clientes
    if navegacao == '1':
        nome = input('Digite seu nome: ')
        endereco = input('Digite seu endereço: ')
        telefone = input('Digite seu telefone: ')
        nascimento = verificarDataNascimento(input('Digite sua data de nascimento: '))
        senha = input('Digite sua senha: ')
        tipo_conta = verificarTipoDaConta(input('Digite o tipo da sua conta (Corrente/Poupança): '))
        saldo = verificarSeNumeroDecimal(input('Quanto quer depositar agora: R$'))
        clientesCadastrados.append(Cliente(nome, endereco, telefone, nascimento, senha, tipo_conta, saldo))
        print('\033[1;32mConta criada com sucesso!\033[m')
        sleep(2)

    # Editar informações do cliente
    if navegacao == '2':
        print('ID       NOME')
        print('-'*20)

        # Enumerando a lista de clientesCadastrados para mostrar na tela o ID do cliente (index),
        # o nome do usuário dentro do objeto users e o tipo da conta dentro do objeto users.
        for index, users in enumerate(clientesCadastrados):
            print(f'{index}. \t {users.informacoes_cliente["nome"]}|{users.informacoes_cliente["tipo_da_conta"]}')
        print('-' * 20)
        print('Deixe em branco para sair')
        id_conta_editar = input('Digite o ID da conta que deseja editar: ')
        if id_conta_editar == '':
            continue
        id_conta_editar = verificarSeNumeroInteiro(id_conta_editar)

        # Varrendo a lista de clientes cadastrados até encontrar aquele que o usuário escolheu pelo ID(index)
        for index, users in enumerate(clientesCadastrados):
            if id_conta_editar == index:
                users.editarDadosDaConta()

    # Excluir informações do cliente
    if navegacao == '3':
        print('ID       NOME')
        print('-'*20)

        # Se a lista de clientes estiver vazia, nada será alterado
        if len(clientesCadastrados) != 0:

            # Varrendo a lista de clientes cadastrados organizados onde o index será o ID
            for index, users in enumerate(clientesCadastrados):
                print(f'{index}. \t {users.informacoes_cliente["nome"]}|{users.informacoes_cliente["tipo_da_conta"]}')
            print('-' * 20)
            print('Deixe em branco para sair')
            id_conta_excluir = input('Digite o ID da conta que deseja excluir: ')
            if id_conta_excluir == '':
                continue
            id_conta_excluir = verificarSeNumeroInteiro(id_conta_excluir)
            are_you_sure = input('Você tem certeza? (S)im/(N)ão: ')[0]

            # Verificando se o usuário tem certeza de que deseja excluir a conta
            if are_you_sure in ['S', 's']:
                try:
                    # Primeiro apaga todas as informações do cliente
                    clientesCadastrados[id_conta_excluir].excluirConta()

                    # Depois remove o cliente da lista de clientesCadastrados
                    clientesCadastrados.remove(clientesCadastrados[id_conta_excluir])
                except Exception as error:
                    continue
        else:
            print('Não há clientes cadastrados')
            sleep(2)

    # Acessar a conta do cliente
    if navegacao == '4':
        menu_clientes_ativo = True
        logado = False

        # Tela de login
        while menu_clientes_ativo:
            print('Deixe os campos vazios para sair')
            if not logado:
                meu_nome = input('LOGIN\n'
                                 'Nome: ')
                minha_senha = input('Senha: ')
                if meu_nome == '' and minha_senha == '':
                    break
                usuario_logado = None

                # Iteração para cada cliente dentro da lista de clientes
                for cli in clientesCadastrados:

                    # Verificando se o nome do cliente está lista
                    if meu_nome == str(cli.informacoes_cliente['nome']):
                        # Verificando se a senha está correta
                        if minha_senha == str(cli.informacoes_cliente['senha']):
                            # Armazenando o objeto Cliente dentro da variável usuario_logado
                            usuario_logado = cli
                            logado = True

            # Usuário está logado
            if logado:
                os.system('cls')
                print(f'LOGADO COMO: {usuario_logado.informacoes_cliente.get("nome")}')
                navegacao_cliente = menuContaCliente()

                # Sacar
                if navegacao_cliente == '1':
                    valor_a_sacar = verificarSeNumeroDecimal(input('Valor: R$'))
                    usuario_logado.sacar(valor_a_sacar)

                # Depositar
                if navegacao_cliente == '2':
                    valor_a_depositar = verificarSeNumeroDecimal(input('Valor: R$'))
                    usuario_logado.depositar(valor_a_depositar)

                # Transferir
                if navegacao_cliente == '3':
                    valor_a_transferir = verificarSeNumeroDecimal(input('Valor: R$'))
                    a_quem_transferir = input('Para quem deseja transferir (digite o nome): ')

                    # Quanto se deseja transferir, a lista com todos os clientes, a quem se deseja transferir
                    usuario_logado.transferir(valor_a_transferir, clientesCadastrados, a_quem_transferir)

                # Consultar saldo
                if navegacao_cliente == '4':
                    print(f'{usuario_logado.consultarSaldo()}')
                    input('Pressione ENTER para sair')

                # Ver histórico
                if navegacao_cliente == '5':
                    for info in usuario_logado.verHistorico():
                        print(info)
                    input('Pressione ENTER para sair')

                # Logout
                if navegacao_cliente == '6':
                    menu_clientes_ativo = False
