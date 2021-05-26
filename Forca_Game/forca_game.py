"""
    Jogo da forca.
    Para modificar ou incluir novas palavras, modificar o arquivo lista_palavras.py
"""

# importando os módulos
## módulo para valores aleatórios
import random  
## "módulo" para as palavras da lista
from lista_palavras import lista_palavras_forca  

# função para escolher uma palavra da lista
def escolhe_palavra():  
  palavra = random.choice(lista_palavras_forca)
  return palavra.upper()

# função para jogar
def jogar(palavra):
    espacos = "-" * len(palavra)
    acertou = False
    guessed_letters = []
    guessed_words = []
    tentativas = 6
    print("Vamos começar!")
    print(desenha_forca(tentativas))
    print(espacos)
    print("\n")
    while not acertou and tentativas > 0:
        chute = input("Por favor, entre com uma letra ou palavra: ").upper()
        if len(chute) == 1 and chute.isalpha():
            if chute in guessed_letters:
                print("Essa letra já apareceu aqui :", chute)
            elif chute not in palavra:
                print(chute, " não está na palavra.")
                tentativas -= 1
                guessed_letters.append(chute)
            else:
                print("Isso aí,", chute, " pertence à palavra!")
                guessed_letters.append(chute)
                word_as_list = list(espacos)
                indices = [i for i, letra in enumerate(palavra) if letra == chute]
                for index in indices:
                    word_as_list[index] = chute
                espacos = "".join(word_as_list)
                if "-" not in espacos:
                    acertou = True
        elif len(chute) == len(palavra) and chute.isalpha():
            if chute in guessed_words:
                print("Você já chutou essa palavra: ", chute)
            elif chute != palavra:
                print(chute, ": não está na palavra.")
                tentativas -= 1
                guessed_words.append(chute)
            else:
                acertou = True
                espacos = palavra
        else:
            print("Chute errado.")
        print(desenha_forca(tentativas))
        print(espacos)
        print("\n")
    if acertou:
        print("Parabéns!! Você é fera!!")
    else:
        print("Nossa, que pena!! Você errou a palavra: " + palavra + ". Tente outra vez!")

# função para desenhar o usuario sendo "enforcado"
def desenha_forca(tentativa):
    progresso = [  
        # cabeça, pescoço, braços e 1 pernas
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # cabeça, pescoço, braços e 1 perna
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # cabeça, pescoço e braços
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # cabeça, pescoço e braços
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # cabeça e pescoço
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # cabeça
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # forca inicial
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return progresso[tentativa]

def main():
    palavra = escolhe_palavra()
    jogar(palavra)
    while input("Deseja Jogar Novamente? (S/N) ").upper() == "S":
        palavra = escolhe_palavra()
        jogar(palavra)


if __name__ == "__main__":
    main()