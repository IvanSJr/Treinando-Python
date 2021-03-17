from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, conta, agencia, saldo):
        self._conta = conta
        self._agencia = agencia
        self._saldo = saldo

    @property
    def conta(self):
        return self._conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numerico.")
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do deposito precisa ser numerico.")
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self._agencia} Conta: {self._conta} Saldo: R$ {self._saldo:.2f}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do deposito precisa ser numerico.")
        if valor > self._saldo:
            print(f'Saldo Insuficiente R${self._saldo:.2f}')
            return
        self._saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, conta, agencia, saldo, limite=500):
        super().__init__(conta, agencia, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do deposito precisa ser numerico.")
        if valor > (self._limite + self._saldo):
            print(f'Saldo Insuficiente R${self._saldo:.2f}.\nSeu limite é de -R${self._limite:.2f}\nVocê tentou sacar R${valor:.2f}')
            return
        self._saldo -= valor
        self.detalhes()


cp = ContaPoupanca(1235, 123, 0)
cp.sacar(50)
cp.depositar(100)
print('#################')

cc = ContaCorrente(1235, 124, 0, 400)
cc.depositar(400)
cc.sacar(550)
cc.sacar(50)
cc.sacar(199)
cc.sacar(5)
