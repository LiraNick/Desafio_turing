import os
import linecache
import time
poli = "="*15
correto = False
escolha = "Escolha a opção: "
os.system('cls' if os.name == 'nt' else 'clear')
telaInicial = open('tela01.txt')
content = telaInicial.readlines()

for i in range(14):
    print(content[i].strip("\n"))
    
print(f"\n {poli} 💍 Lord of the Rings 💍 {poli} \n")
vidas=3
def slowprint(texto, atraso=2):
  for c in texto:
    print(c,end='',flush=True)
    time.sleep(atraso)
pergunta = {"pergunta":"",
                "resposta1":"",
                "resposta2":"",
                "opcaoCorreta":""} 
    



c=2
usuario=str(input("Digite seu nome de usuario: "))
while(c!=0):
    while(correto!=True):#fase1
        if vidas==0:
            correto=True
        else:
            linha=1
            perguntaLinha = linecache.getline('perguntasRespostas.txt', linha)
            pergunta["pergunta"] = perguntaLinha.replace("P: ", "").strip("\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).replace("1: ", "").strip("\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).replace("2: ", "").strip("\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).replace("R: ", "").strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            print(1,pergunta["resposta1"])
            
            print(2,pergunta["resposta2"])
            print("\n")
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("\n")
                print("CORRETO")
                print("\n")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas} \n")
        
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
            pergunta["pergunta"] = perguntaLinha.replace("P: ", "").strip("\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).replace("1: ", "").strip("\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).replace("2: ", "").strip("\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).replace("R: ", "").strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            print(1,pergunta["resposta1"])
            print(2,pergunta["resposta2"])
            print("\n")
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("\n")
                print("CORRETO")
                print("\n")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas} \n")    
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
            pergunta["pergunta"] = perguntaLinha.replace("P: ", "").strip("\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).replace("1: ", "").strip("\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).replace("2: ", "").strip("\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).replace("R: ", "").strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("\n CORRETO \n")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas} \n")
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
            pergunta["pergunta"] = perguntaLinha.replace("P: ", "").strip("\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).replace("1: ", "").strip("\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).replace("2: ", "").strip("\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).replace("R: ", "").strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            print(1,pergunta["resposta1"])
            print(2,pergunta["resposta2"])
            print("\n")
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("correto")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas} \n")
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
            pergunta["pergunta"] = perguntaLinha.replace("P: ", "").strip("\n")
            pergunta["resposta1"] = linecache.getline('perguntasRespostas.txt', linha+1).replace("1: ", "").strip("\n")
            pergunta["resposta2"] = linecache.getline('perguntasRespostas.txt', linha+2).replace("2: ", "").strip("\n")
            pergunta["opcaoCorreta"] = linecache.getline('perguntasRespostas.txt', linha+3).replace("R: ", "").strip("\n")
            slowprint(pergunta["pergunta"],0.001)
            print("\n")
            if str(input(escolha))==pergunta["opcaoCorreta"]:
                print("correto")
                correto = True
            else:
                vidas = vidas -1
                print(f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas}\n")
    
    
print("fim de jogo")
