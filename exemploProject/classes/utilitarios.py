import os
from datetime import date


def verificarDataNascimento(data: str):
    """
    Essa função irá validar a data fornecida no parâmetro data, essa função realizará:
        - Separar a data fornecida e retornar a data no formato dd/mm/yy
        - Verificar se o dia, mês ou o ano são valores válidos (ex.: dia 32 não existe)

    :param data:
    :return:
    """
    while True:
        # Verificando se a data possui a "/" e se o seu tamanho corresponde ao formato 00/00/00 ou 00/00/0000
        if '/' in data and 7 <= len(data) <= 10:
            formatando_a_data = data.split('/') # Precisamos separar a data fornecida e colocar em uma lista
            # Ao fazer isso, teremos a data fornecida da seguinte forma: formatando_a_data = [24, 09, 1998]

            # Verificando se o dia se encontra no intervalo entre 0 a 31, sendo o 0 exclusivo/ignorado
            if 0 < int(formatando_a_data[0]) <= 31:
                # Verificando se o mês se encontra no intervalo entre 0 a 12, sendo o 0 exclusivo/ignorado
                if 0 < int(formatando_a_data[1]) <= 12:
                    # Verificando se o ano é menor do que o ano atual (ninguém pode ter nascido 1 ano no futuro)
                    if int(formatando_a_data[2]) <= date.today().year:
                        break # Se a data passar nas verificações, o loop é encerrado
                    else:
                        data = ''
                else:
                    data = ''
            else:
                data = ''  # Cada um desses elses fará com que a data receba uma string vazia caso o usuário forneça
                # uma data inválida, isso irá fazer com que o programa execute o último else, onde é pedido que o
                # usúario digite a data corretamente
        else:
            data = input('\033[1;31mFormato inválido!\033[m\nDigite a data corretamente (dd/mm/yy): ')
            continue
    # Ao final cria-se uma variável que armazena a data no formato dd/mm/yy e ela é retornada
    data_formatada = f'{formatando_a_data[0]}/{formatando_a_data[1]}/{formatando_a_data[2]}'
    return data_formatada


def verificarTipoDaConta(tipo_da_conta):
    """
    Essa função validará o tipo da conta, ou a conta é corrente ou é poupança, qualquer coisa
    além disso será inválido.

    :param tipo_da_conta:
    :return:
    """
    # Cria-se um loop onde se o tipo_da_conta não se encontra na lista fornecida o loop continuará sua execução
    # até que seja fornecido um tipo válido para uma conta
    while str(tipo_da_conta).lower() not in ['corrente', 'poupanca', 'poupança']:
        tipo_da_conta = input('Tipo da conta inválido! Digite "Poupança" ou "Corrente": ')
    return tipo_da_conta


def verificarSeNumeroInteiro(numero_a_verificar):
    """
    Essa função irá validar se o usuário forneceu um número do tipo inteiro,
    caso não, será pedido ao usuário que digite um número que seja inteiro.

    :param numero_a_verificar:
    :return:
    """
    naoValidado = True
    # Enquanto o número não for validado, o loop não se encerrará
    while naoValidado:
        try:
            # Primeiro vem a tentativa de converter o número para inteiro
            numero_a_verificar = int(numero_a_verificar)
            # Se não houver erros, ele foi verificado, portanto o loop se encerrará
            naoValidado = False
        # Se, ao tentar converter para inteiro, retornar um erro, o except é chamado
        except ValueError as excp:
            # Ao ser chamado, ele pedirá que o usuário digite um número válido e irá reiniciar o loop após isso
            numero_a_verificar = input('Digite um número inteiro válido: ')
            continue
    return numero_a_verificar


def verificarSeNumeroDecimal(numero_a_verificar):
    """
    Essa função irá validar se o usuário forneceu um número do tipo float,
    caso não, será pedido ao usuário que digite um número que seja float.

    :param numero_a_verificar:
    :return:
    """
    naoValidado = True
    # Enquanto o número não for validado, o loop não se encerrará
    while naoValidado:
        try:
            # Primeiro vem a tentativa de converter o número para float
            numero_a_verificar = float(numero_a_verificar)
            # Se não houver erros, ele foi verificado, portanto o loop se encerrará
            naoValidado = False
        # Se, ao tentar converter para float, retornar um erro, o except é chamado
        except ValueError as excp:
            # Ao ser chamado, ele pedirá que o usuário digite um número válido e irá reiniciar o loop após isso
            numero_a_verificar = input('Digite um número válido: ')
            continue
    return numero_a_verificar


def criarMenuDeNavegacao():
    """
    Essa função simplesment cria um menu de navegação e retorna o número escolhido pelo usuário.

    :return:
    """
    print('[1] Para criar   conta\n'
          '[2] Para editar  conta\n'
          '[3] Para excluir conta\n'
          '[4] Para acessar conta')
    menu_nav = input('>>> ')
    os.system('cls')
    return menu_nav


def menuContaCliente():
    """
    Essa função simplesment cria um menu de navegação e retorna o número escolhido pelo usuário.

    :return:
    """
    print(f'[1] Para sacar\n'
          f'[2] Para depositar\n'
          f'[3] Para transferir\n'
          f'[4] Para consultar saldo\n'
          f'[5] Para historico de transações\n'
          f'[6] Para sair')
    menu_nav = input('>>> ')
    os.system('cls')
    return menu_nav


def boasVindas(texto: str) -> str:
    """
    Essa função cria um texto de boas-vindas.

    :param texto:
    :return:
    """
    os.system('cls')
    print('-' * 32)
    print(f'{texto:^30}')
    print('-' * 32)
