from asyncio.windows_events import NULL
import os
from random import randrange
import linecache

os.system('cls' if os.name == 'nt' else 'clear')

def buscaPergunta(linha=1):
    pergunta = {"pergunta":"",
                "resposta1":"",
                "resposta2":"",
                "opcaoCorreta":""} 
    
    perguntaLinha = linecache.getline('perguntasRespostas.txt', linha)

    aux = perguntaLinha[0]    
    if aux == "P":
        pergunta["pergunta"] = perguntaLinha.replace("P: ", "").strip("\n")
        pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).replace("1: ", "").strip("\n")
        pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).replace("2: ", "").strip("\n")
        pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).replace("R: ", "").strip("\n")
        return pergunta
    else:
        print("Não é uma pergunta")
        return NULL
    

telaInicial = open('tela01.txt')
conteudoFase = open('perguntasRespostas.txt')

content = telaInicial.readlines()

for i in range(14):
    print(content[i])
    

endGeral = False
vidaUsuario = 2
#menu principal
while endGeral == False:

    aux = 1
    for i in range(5):
        perguntaLoop = buscaPergunta(aux)
        print(perguntaLoop["pergunta"], "\n\n")
        print("1:", perguntaLoop["resposta1"])
        print("2:", perguntaLoop["resposta2"], "\n\n")

        print("Colinha:", perguntaLoop["opcaoCorreta"], "\n")
        escolhaInput = str(input("Escola uma opcao: "))

        if perguntaLoop["opcaoCorreta"] == escolhaInput:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("WOHO! Você ainda possui", vidaUsuario, " Vidas.\n\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            vidaUsuario = vidaUsuario-1
            print("BOOO! Você possui", vidaUsuario, " Vidas.\n\n")
            if vidaUsuario == 0:
                print("Você Morreu!")
                endGeral = True
                break
        aux = aux+4
        