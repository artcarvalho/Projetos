class Conta:
    def __init__(self, numero, titular, saldo, limite = 300.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, saldo):
        self.__saldo += saldo
        print("Deposito Realizado com Sucesso")

    def __disponivel(self, quantia):
        disponivel = self.__limite + self.__saldo
        if disponivel:
            return True
        return False

    def sacar(self, quantia):
        if self.__disponivel(quantia):
            self.__saldo -= quantia
            print("Saque realizado com sucesso")
            return
        print("Saldo Inválido, Você possui R$ %s Disponivel e %s como limite" % self.__saldo. self.__limite)
        
    def extrato(self):
        print("Saldo: %s" % self.__saldo)

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
