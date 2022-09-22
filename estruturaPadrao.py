import os
import linecache
import time
poli = "="*10
correto = False
escolha = "Escolhe a opção:"
print(f"{poli} JOGO {poli}")
vidas=5
os.system('cls' if os.name == 'nt' else 'clear')
def slowprint(texto, atraso=2):
  for c in texto:
    print(c,end='',flush=True)
    time.sleep(atraso)


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
errado=f"Você escolheu a opção errada, perdeu uma vida \n VIDA TOTAL:{vidas}"

usuario=str(input("Digite seu nome de usuario: "))
for c in range(0,7):
    while(correto!=True):#fase1
        questao = buscaPergunta(1)
        slowprint(questao["pergunta"],0.05)
        print("\n")
        print(1,questao["resposta1"])
        print(2,questao["resposta2"])
        if str(input(escolha))==questao['opcaoCorreta']:
            print("correto")
            correto = True
        else:
            vidas=vidas-1
            print(errado)
            print("errado")
    correto=False
    while(correto!=True):#fase2
        questao = buscaPergunta(5)
        slowprint(questao["pergunta"],0.05)
        print("\n")
        print(1,questao["resposta1"])
        print(2,questao["resposta2"])

        if str(input(escolha))==questao['opcaoCorreta']:
            print("correto")
            correto = True
        else:
            vidas=vidas-1
            print(errado)
            
    correto=False
    while(correto!=True):#fase3
        questao = buscaPergunta(9)
        slowprint(questao["pergunta"],0.05)
        
        if str(input("digite o nome:"))==questao['opcaoCorreta']:
            print("correto")
            correto = True
        else:
            vidas=vidas-1
            print(errado)
    correto=False
    while(correto!=True):#fase4
        questao = buscaPergunta(13)
        slowprint(questao["pergunta"],0.05)
        print("\n")
        print(1,questao["resposta1"])
        print(2,questao["resposta2"])

        if str(input(escolha))==questao['opcaoCorreta']:
            print("correto")
            correto = True
        else:
            vidas=vidas-1
            print(errado)
    correto=False
    while(correto!=True):#fase5
        questao = buscaPergunta(17)
        slowprint(questao["pergunta"],0.05)
        
        if str(input("digite o nome:"))==questao['opcaoCorreta']:
            print("correto")
            correto = True
        else:
            vidas=vidas-1
            print(errado)
    
    
