import os
import linecache
import time
poli = "="*10
correto = False
escolha = "Escolhe a opção:"
os.system('cls' if os.name == 'nt' else 'clear')

print(f"\n {poli} JOGO {poli} \n")
vidas=3
def slowprint(texto, atraso=2):
  for c in texto:
    print(c,end='',flush=True)
    time.sleep(atraso)
pergunta = {"pergunta":"",
                "resposta1":"",
                "resposta2":"",
                "opcaoCorreta":""} 
    


def buscaPergunta(linha=1):
    #reservado para teste de perguntas aleatórias
    #linha = randrange(21)
    

    #print(pergunta)
    #print(pergunta[0])
    aux = perguntaLinha[0]    
    if aux == "P":
        
        return pergunta

c=2
usuario=str(input("Digite seu nome de usuario: "))
while(c!=0):
    while(correto!=True):#fase1
        if vidas==0:
            correto=True
        else:
            linha=1
            perguntaLinha = linecache.getline('perguntasRespostas.txt', linha)
            pergunta["pergunta"] = perguntaLinha.strip("P:\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).strip("1:\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).strip("2:\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            print(1,pergunta["resposta1"])
            print("\n")
            print(2,pergunta["resposta2"])
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("correto")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas}")
        
    if vidas==0:
        break    
    else:
        correto=False
    while(correto!=True):#fase2
        if vidas==0:
                correto= True
        else:
            linha=5
            perguntaLinha = linecache.getline('perguntasRespostas.txt', linha)
            pergunta["pergunta"] = perguntaLinha.strip("P:\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).strip("1:\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).strip("2:\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            print(1,pergunta["resposta1"])
            print("\n")
            print(2,pergunta["resposta2"])
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("correto")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas}")    
    if vidas==0:
        break    
    else:
        correto=False        
    while(correto!=True):#fase3
        if vidas==0:
                correto= True
        else:
            linha=9
            perguntaLinha = linecache.getline('perguntasRespostas.txt', linha)
            pergunta["pergunta"] = perguntaLinha.strip("P:\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).strip("1:\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).strip("2:\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("correto")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas}")
    if vidas==0:
        break    
    else:
        correto=False
    while(correto!=True):#fase4
        if vidas==0:
                correto= True
        else:
            linha=13
            perguntaLinha = linecache.getline('perguntasRespostas.txt', linha)
            pergunta["pergunta"] = perguntaLinha.strip("P:\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).strip("1:\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).strip("2:\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            print(1,pergunta["resposta1"])
            print("\n")
            print(2,pergunta["resposta2"])
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("correto")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas}")
    if vidas==0:
        break    
    else:
        correto=False
    while(correto!=True):#fase5
        if vidas==0:
                correto= True
        else:
            linha=17
            perguntaLinha = linecache.getline('perguntasRespostas.txt', linha)
            pergunta["pergunta"] = perguntaLinha.strip("P:\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).strip("1:\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).strip("2:\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("correto")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas}")
    
    
print("fim de jogo")
