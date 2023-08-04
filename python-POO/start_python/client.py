from forca import main as f_main
from jogo_advinha import main as adv_main

def main():
    print("==="*10)
    print("(1) Forca (2) Jogo adivinhacao")
    print("==="*10)
    jogo = int(input("Selecione um Jogo:"))

    if jogo == 1:
        f_main()
    if jogo == 2:
        adv_main()
    return

if __name__ == "__main__":
    main()