import os
from random import randrange
import linecache

os.system('cls' if os.name == 'nt' else 'clear')

def buscaPergunta(linha=1):
    #reservado para teste de perguntas aleatórias
    #linha = randrange(21)
    pergunta = {"pergunta":"",
                "resposta1":"",
                "resposta2":"",
                "opcaoCorreta":""} 
    
    perguntaLinha = linecache.getline('perguntasRespostas.txt', linha)

    #print(pergunta)
    #print(pergunta[0])
    aux = perguntaLinha[0]    
    if aux == "P":
        pergunta["pergunta"] = perguntaLinha.strip("P:\n")
        pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).strip("1:\n")
        pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).strip("2:\n")
        pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).strip("\n")
        return pergunta
    elif aux == "1":
        linha = linha-1
        pergunta = linecache.getline('perguntasRespostas.txt', linha)
        print(pergunta)
    elif aux == "2":
        linha = linha-2
        pergunta = linecache.getline('perguntasRespostas.txt', linha)
        print(pergunta)
    elif aux == "R":
        linha = linha-3
        pergunta = linecache.getline('perguntasRespostas.txt', linha)
        print(pergunta)
    

telaInicial = open('tela01.txt')

content = telaInicial.readlines()

for i in range(14):
    print(content[i])
    

teste1 = buscaPergunta()
print(teste1)

print(teste1["pergunta"])
asd = input("Escola uma opcao")
if teste1["opcaoCorreta"] == asd:
    print("WOHO!")

#buscaPerguntaAleatoria(5)


