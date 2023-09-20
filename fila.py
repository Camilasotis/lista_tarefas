paciente1 = {
   "nome":"Camila","num":"0989"
}
paciente2 = {
   "nome":"Maria","num":"9909"
}
paciente3 = {
   "nome":"Pedro","num":"8878"
}
paciente4 = {
   "nome":"Filipe","num":"6677"
}
fila = []

fila.append(paciente1)
fila.append(paciente2)
fila.append(paciente3)
fila.append(paciente4)

print("1-Registrar um paciente;")
print("2-Chamar o próximo paciente;")
print("3-Mostrar os próximos pacientes;")
print("4-Mostrar o total de pacientes na fila;")
print("5-Buscar um paciente pelo nome.")


while(True):
     op=int(input("Digite o número da opção:"))
     match op:
        case 1:
         nome=input("Digite o nome do paciente: \n")
         num=input("Digite o número do paciente: \n")

         fila.append({nome,num}) #insere um elemento no final da lista
         print (fila)
        case 2:
           print(fila[0])
           fila.pop(0)
        case 3:
           print(fila)
        case 4:
           len(fila)
           print(len(fila))
        case 5:
           nome=input("Digite o nome do paciente: \n")
           for i in range(len(fila)):
              if(fila[i]["nome"]==nome):
                 print(i)
                
                
                 
           
               
           
           
