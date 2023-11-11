import os
from time import sleep

from classes.utilitarios import verificarSeNumeroInteiro, verificarDataNascimento, verificarTipoDaConta

# Criando a classe Cliente
class Cliente:
    def __init__(self, nome, endereco, telefone, data_nascimento, senha, tipo_da_conta, saldo: float):
        """
        Quando esta classe for instanciada (chamada para dentro de uma variável) ela inicializará
        todos os parâmetros fornecidos pelo usuário.

        :param nome:
        :param endereco:
        :param telefone:
        :param data_nascimento:
        :param senha:
        :param tipo_da_conta:
        :param saldo:
        """
        # Onde serão armazenadas as transações
        self.historico = []
        self.informacoes_cliente = dict(nome=nome,
                                        endereco=endereco,
                                        telefone=telefone,
                                        data_nascimento=data_nascimento,
                                        senha=senha,
                                        tipo_da_conta=tipo_da_conta,
                                        saldo=saldo)


    def depositar(self, valor_a_depositar):
        """
        Função para realizar depósitos

        :param valor_a_depositar:
        :return:
        """
        self.informacoes_cliente['saldo'] += valor_a_depositar
        self.historico.append(f'Você fez um depósito no valor de R${valor_a_depositar:.2f}')

    def sacar(self, valor_a_sacar):
        """
        Função para realizar saques

        :param valor_a_sacar:
        :return:
        """
        if self.informacoes_cliente['saldo'] > valor_a_sacar:
            self.informacoes_cliente['saldo'] -= valor_a_sacar
            self.historico.append(f'Você fez um saque no valor de R${valor_a_sacar:.2f}')
        else:
            print('\033[;31mVocê não tem saldo suficiente!\033[m')
            sleep(2)

    def consultarSaldo(self):
        """
        Simplesmente mostrará quanto há depósitado na conta do cliente
        :return:
        """
        return f'Seu saldo é de R${self.informacoes_cliente["saldo"]}'


    def verHistorico(self):
        """
        Simplesmente mostrará o histórico de transações do cliente
        :return:
        """
        return self.historico


    def transferir(self, valor_a_transferir, lista_usuarios: list, nome: str):
        """
        Essa função irá transferir um valor para a conta de outro cliente.
        Para isso é necessário fornecer uma lista com todos os clientes que temos,
        cada elemento da lista será do tipo objeto e que instancia a classe Cliente.
        A função ainda realizará:
            - Armazenar as transações no histórico daquele que envia
            - Armazenar as transações no histórico daquele que recebe

        :param valor_a_transferir:
        :param lista_usuarios:
        :param nome:
        :return:
        """
        # Para quem se deve transferir
        usuario_a_transferir = None

        # A lista lista_usuarios será varrida do início ao fim e cada elemento se chamará usuario
        for usuario in lista_usuarios:

            # Verificando se o nome do usuario é igual ao nome fornecido no parâmetro "nome" da função
            if str(usuario.informacoes_cliente.get('nome')) == nome:
                are_you_sure = '0'
                # Se o saldo for menor do que o valor a ser transferido, será perguntado se a transação deve continuar
                if self.informacoes_cliente.get('saldo') < valor_a_transferir:
                    are_you_sure = input(f'Seu saldo é de R${self.informacoes_cliente.get("saldo")}, tem certeza de que'
                          f' quer transferir R${valor_a_transferir:.2f}? (Você ficará negativado após isso)'
                                         f'\n[0] Sim\n[1] Não\n>>> ')

                if are_you_sure == '0' and self.informacoes_cliente.get('nome') != nome:
                    # Se a transação continuar, vamos pegar o usuário a quem se deve transferir
                    usuario_a_transferir = usuario

                    # Este usuário terá o saldo incrementado pelo valor transferido
                    usuario_a_transferir.informacoes_cliente['saldo'] += valor_a_transferir

                    # O histórico desse mesmo usuário receberá as informações da transação
                    usuario_a_transferir.historico.append(f'Você recebeu um depósito no valor de '
                                                          f'R${valor_a_transferir:.2f}')

                    # O cliente que transferiu recebe em seu histórico as informações da sua transação
                    self.historico.append(f'Você transferiu R${valor_a_transferir:.2f} para {nome}')

                    # O cliente que transferiu o valor terá seu saldo decrementado
                    self.informacoes_cliente['saldo'] -= valor_a_transferir

                # Quando tudo for concluído, o break irá parar a iteração para que ele pare de iterar a lista
                # sendo que a transação já foi feita
                break


    def editarDadosDaConta(self):
        """
        Essa função realizará o papel de editar as informações do cliente.

        :return:
        """

        # Uma lista com os nomes de cada valor que o usuário pode alterar
        indexes = ['Nome', 'Endereço', 'Telefone', 'Nascimento', 'Senha', 'Tipo']
        while True:
            os.system('cls')

            # O dicionário com as informações do cliente é enumerada, cada valor(values) recebe um índice(index)
            for index, values in enumerate(self.informacoes_cliente.values()):
                try:
                    # Será mostrado na tela um index(valor númerico), um elemento da lista indexes e as informações do
                    # cliente
                    print(f'[{index}] {indexes[index]}: {values}')

                # Um erro sempre será retornado porque será apontado que a lista está fora de alcance, pois está sendo
                # ignorado o "saldo" do cliente visto que ele pode alterar seu saldo depositando ou sacando
                # esse erro será apenas ignorado para que o programa possa fluir
                except Exception:
                    pass
            print('[6] sair')
            dado_a_editar = verificarSeNumeroInteiro(input('Qual informação deseja editar: '))
            if dado_a_editar == 6:
                break

            # O dicionário com as informacoes do cliente será enumerada por índices(index) e chaves(keys)
            for index, keys in enumerate(self.informacoes_cliente.keys()):

                # O cliente insere a nova informação de acordo com a opção que ele escolher
                # Obs: a opção deve ser diferente de 3 e de 5, pois esses dois devem ser trabalhados de forma separada
                if dado_a_editar == index and dado_a_editar != 3 and dado_a_editar != 5:
                    self.informacoes_cliente[keys] = input('Digite a nova informação: ')

                # Verificando se o cliente escolheu 3 e a chave é igual a "data_nascimento"
                elif dado_a_editar == 3 and keys == 'data_nascimento':

                    # É inserido a nova data de nascimento
                    self.informacoes_cliente[keys] = verificarDataNascimento(input('Digite a nova data: '))

                # Verificando se o cliente escolheu 5 e a chave é igual a "tipo_da_conta"
                elif dado_a_editar == 5 and keys == 'tipo_da_conta':

                    # É inserido a novo tipo da conta
                    self.informacoes_cliente[keys] = verificarTipoDaConta(input('Digite a novo tipo: '))


    def excluirConta(self):
        """
        Essa função apenas apaga tudo do dicionário com as infomações do cliente

        :return:
        """
        self.informacoes_cliente.clear()
