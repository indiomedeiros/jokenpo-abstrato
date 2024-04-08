from random import choice

def j():
    a = ["Jogador venceu","Computador venceu", "Empate!"]
    while True:
        try:
            o = ["Pedra", "Papel", "Tesoura"]
            print("Escolha uma opcao para jogar: ")
            for i, opcao in enumerate(o):
                print(f"[{i}] {opcao}")
            g = int(input("Digite sua escolha:"))
            p = choice(range(3))
            if g not in range(3):
                print(f"-={"=" * 35}\nEntrada inválida!\n-{"=" * 35}")
            else:
                print("JO\nKEN\nPOOH!!!")
                print("-"+"=" * 35)
                print(f"O computador escolheu: {o[p]}")
                print(f"O jogador escolheu: {o[g]}")
                print("-"+"=" * 35)
                r = (g - p) % 3
                if r == 0:
                    print(a[2])
                elif r == 1:
                    print(a[0])
                else:
                    print(a[1])
                d = input("Deseja continuar jogando? [s/n]")
                if d.lower() != "s":
                    print("Obrigado por jogar!")
                    break
                else:
                    print("-"+"=" * 35)
        except:
            print("Entrada inválida!")
    
j()