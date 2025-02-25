class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._transacoes = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @property
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\n||| Você Não Possui Saldo insuficiente. |||')

        elif valor > 0:
            self._saldo -= valor
            print('\n||| Saque Realizado com Sucesso. |||')
            return True
        
        else:   
            print('\n||| Valor do Saque Inválido. |||')
        return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('||| Depósito Realizado com Sucesso. |||')
        
        else:
            print('\n||| Valor do Depósito Inválido. |||')
            return False
        
        return True
