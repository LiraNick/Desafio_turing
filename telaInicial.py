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
        pergunta["pergunta"] = perguntaLinha.strip("P:\n")
        pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).strip("1:\n")
        pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).strip("2:\n")
        pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).strip("\n")
        return pergunta
    else:
        print("Não é uma pergunta")
        return NULL
    

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


