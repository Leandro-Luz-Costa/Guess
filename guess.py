import random

def main():

    resposta = random.randint(1,10)
    while True:
        try:
            numero = int(input("Tente adivinhar o número de 1 á 10: "))
            if guess(numero, resposta):
                 break
        except ValueError:
            print("Insira um número!")
            continue


def guess(numero, resposta):
        if numero != resposta:
            print("Número errado! Tente novamente")
            return False
        else:
            print(f"Parabéns você acertou, o número era {resposta}")
            return True
    



main()   