from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marcos", 100.0, 1000.0)
conta.transferir(10.0, conta2)
conta.extrato()
conta2.extrato()
