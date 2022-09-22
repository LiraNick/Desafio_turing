from calendar import c
import time

pergunta = "Nossa aventura se passa na idade média e se inicia em um condado muito tranquilo e distante, no qual você mora com seu tio Bilbo. Porém em um dia inusitado, você descobre que a paz do condado pode ser comprometida caso você não assuma a responsabilidade de levar um determinado anel de poder para uma determinada cidade élfica. Qual será sua decisão? "


def lin():

    
    for c in range(1000):
      lin()
      print(pergunta[c], end='', flush=True)
      time.sleep(0.02)
      print(' Pronto!')

    
    for c in range(1000):
      lin()
      print(pergunta[c], end='', flush=True)
      time.sleep(0.02)
      print(' Pronto!')

    for c in range(1000):
      lin()
      print(pergunta[c], end='', flush=True)
      time.sleep(0.02)
      print(' Pronto!')
