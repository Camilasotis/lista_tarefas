# criar um programa que permite a anotação de tarefas
# As funções são:
# 1-Incluir tarefa
# 2-Marcar como feita
# 3-Remover Tarefa
# 4-Esvaziar Lista
# Após a operação exibir a lista de tarefas!

#Váriavel global para armazenar tarefas
#tarefas = []

#Adicionando...
#tarefas.append("Lavar o banheiro")
#tarefas.append("Limpar cozinha")

#Montando uma lista..
import 
tarefas = []
def menu():
   print ("1-Incluir tarefa")
   print ("2-Marcar tarefa como feita")
   print ("3-Listar tarefas")
   print ("4-Excluir uma tarefa")
   print ("5-Limpar lista de tarefas")

def adicionar():tarefas.append(input("Digite a tarefa:"))

def marcar():
    print("Veja sua lista de tarefas...")
    listar()
    codigo=int(input("Digite o número da tarefa:"))
    if codigo>=0 and codigo<len(tarefas): tarefas[codigo] = tarefas[codigo] + "[ok]"

def excluir():
   print("Veja sua lista de tarefas...")
   listar()
   codigo=int(input("Digite o número da tarefa:"))
   if codigo>=0 and codigo<len(tarefas): tarefas.pop(codigo)

def listar():
   for i,item in enumerate(tarefas): print("(",i,")",item)

def limpar(): tarefas.clear()


while(True):
    os.system('cls')
    menu()
    op=input("Digite a opção desejada: \n")
    
    match op:
       case "1": adicionar()
       case "2":marcar()
       case "3":listar()
       case "4":excluir()

    input("Digite qualquer tecla para continuar...")
      
      

      

