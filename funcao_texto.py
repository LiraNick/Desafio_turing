import time

def slowprint(texto, atraso=2):
  for c in texto:
    print(c,end='',flush=True)
    time.sleep(atraso)

#slowprint('E lá vamos nós')
var1 = 'e lá vamos nós'

slowprint(var1, 0.1)