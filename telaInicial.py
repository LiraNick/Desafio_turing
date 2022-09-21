import os
from random import randrange
import linecache

os.system('cls' if os.name == 'nt' else 'clear')

def buscaPerguntaAleatoria():
    linha = randrange(21)
    
    pergunta = linecache.getline('perguntasRespostas.txt', linha)

    #print(pergunta)
    print(pergunta[0])
    aux = pergunta[0]    
    if aux == "P":
        print(pergunta)
    elif aux == "1":
        linha = linha-1
        pergunta = linecache.getline('perguntasRespostas.txt', linha)
        print(pergunta)
    elif aux == "2":
        linha = linha-2
        pergunta = linecache.getline('perguntasRespostas.txt', linha)
        print(pergunta)
    

telaInicial = open('tela01.txt')

content = telaInicial.readlines()

for i in range(14):
    print(content[i])
    

buscaPerguntaAleatoria()



