def menu():
   print ("1-depositar")
   print ("2-Sacar")
   print ("3-Ver Saldo")
   print ("4-Pix")


def deposito(conta,valor):
    for cliente in clientes:
        if cliente['conta']==conta:
            cliente['saldo']=cliente['saldo']+valor

def saque(conta, valor):
    for cliente in clientes:
        if cliente['conta']==conta:
            if cliente['saldo'] >= valor:
               cliente['saldo']=cliente['saldo']-valor
            else: print("SALDO INSUFICIENTE")

def saldo(conta):
    for cliente in clientes:
        if cliente['conta']==conta:
            print(cliente['saldo'])

def pix(origem,destino,valor):
    saque(origem,valor)
    deposito(destino,valor)
   

clientes = [
    {"nome":"Camila","saldo":1000,"conta":1111},
    {"nome":"Marisa","saldo":8000,"conta":2222},
    {"nome":"Duda","saldo":4000,"conta":3333},
    {"nome":"Arthur","saldo":500,"conta":4444}
]


print(clientes)


  
