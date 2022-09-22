poli = "="*10
correto = False
escolha = "Escolhe a opção:"
print(f"{poli} JOGO {poli}")
usuario=str(input("Digite seu nome de usuario: "))
for c in range(0,7):
    while(correto!=True):#fase1
        questao = buscaPergunta()
        print(questao["pergunta"])
        if int(input(escolha))==questao['opcaoCorreta']:
            print("correto")
        else:
            print("errado")

    #while(correto!=True):#fase2

    #while(correto!=True):#fase3

    #while(correto!=True):#fase4

    #while(correto!=True):#fase5

    #while(correto!=True):#fase6
