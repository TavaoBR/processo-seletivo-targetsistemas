import time

def ligar_interruptor(num):
    print(f"Interruptor {num} ligado")
    
def desligar_interruptor(num):
    print(f"Interruptor {num} desligado")
    
def verifica_lampada():
    return {
        'Lampada_1': 'aquecida',
        'Lampada_2': 'acesa',
        'Lampada_3': 'desligada'
    }

def descobrir_interruptores():
    ligar_interruptor(1)
    time.sleep(5)
    
    desligar_interruptor(1)
    ligar_interruptor(2)
    
    lampadas = verifica_lampada()
    
    for lampada, estado in lampadas.items():
        if estado == 'aquecida':
            print(f"{lampada} é controlada pelo interruptor 1")
        elif estado == 'acesa':
           print(f"{lampada} é controlada pelo interruptor 2")
        else:
          print(f"{lampada} é controlada pelo interruptor 3")   
          
          
descobrir_interruptores()                      