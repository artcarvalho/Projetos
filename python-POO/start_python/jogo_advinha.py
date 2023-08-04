#jogo malandro advinhação
from random import randint as rd

def query(n, nivel):
    chances = 20-(nivel*5)

    for rodadas in range(1, chances+1):
        print("Tentativa %s de %s" % (rodadas, chances))
        q = int(input("Chute um numero de 1 a 100: "))
        while q < 1 or q > 100:
            print("Você digitou um valor invalido")
            q = int(input("Chute um numero de 1 a 100: "))
        if q == n:
            print("Parabéns, você acertou o número %s em %s Rodadas" % (n, rodadas))
            return
        elif rodadas != chances:
            if q < n:
                print("\nDica: Chute mais alto")
            elif q > n:
                print("\nDica: Chute mais baixo")

    print("Que pena, não foi dessa vez!, o número era %s" % n) 
    return 
        

def main():
    n = rd(1, 101)
    print("="*5,"JOGO DA ADVINHACAO","="*5)

    print("\nEscolha um nivel: ")
    nivel = int(input("(1) Facil (2) Médio (3) Difícil: "))

    query(n, nivel)

    return 

if __name__ == "__main__":
    main()