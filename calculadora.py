     
n=0
while n==0:
    def soma(a,b):
        if (opcao==1):
          soma=a+b
          print(a,"+",b,"=",soma)
    def sub(a,b):
        if (opcao==2):
          sub=a-b
          print(a,"-",b,"=",sub)
    def mult(a,b):
        if (opcao==3):  
          mult=a*b
          print(a,"*",b,"=",mult)
    def div(a,b):
        if(opcao==4):
          div=a/b
          print(a,"/",b,"=",div)
    def pot(a,b):
        if(opcao==5):
           pot=a**b
           print(a,"**",b,"=",pot)
    print("1- Soma \n2- Subtração \n3- Multiplicação \n4- Divisão \n5- Potência")
    opcao=int(input("Digite o número da opção:"))
    a=float(input("Digite o valor do primeiro número:"))
    b=float(input("Digite o valor do segundo número:"))

    soma(a,b)
    sub(a,b)
    mult(a,b)
    div(a,b)
    pot(a,b)


    