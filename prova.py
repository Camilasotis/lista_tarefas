questao1 = {
    "Valor questão":"20",
    "Gabarito":"b",
    "enunciado":"Qual o nome do assento colocado no dorso do cavalo para os cavaleiros se sentarem?",
    "letra a)":"Estribo",
    "letra b)":"Sela",
    "letra c)":"Barrigueira",
    "letra d)":"Baixeiro",
}   
questao2 = {
    "Valor questão":"20",
    "Gabarito":"c",
    "enunciado":"Qual o nome do equipamento que serve de apoio para os pés dos cavaleiros?",
    "letra a)":"Cabresto",
    "letra b)":"Arreio",
    "letra c)":"Estribo",
    "letra d)":"Manto",
}
questao3 = {
    "Valor questão":"20",
    "Gabarito":"a",
    "enunciado":"Qual o nome do equipamento que é colocado na cabeça de um cavalo?",
    "letra a)":"Cabeçada",
    "letra b)":"Embocadura",
    "letra c)":"Rédea",
    "letra d)":"Peitoral",
}   
questao4 = {
    "Valor questão":"20",
    "Gabarito":"d",
    "enunciado":"Qual o nome do equipamento que vai na boca do cavalo?",
    "letra a)":"Gamarra",
    "letra b)":"Rédea",
    "letra c)":"Cabresto",
    "letra d)":"Embocadura",
} 
questao5 = {
    "Valor questão":"20",
    "Gabarito":"b",
    "enunciado":"Como seu corpo deve ficar posicionado para descer morro à cavalo?",
    "letra a)":"Para frente com os pés para trás",
    "letra b)":"Para trás com os pés pra frente",
    "letra c)":"Nem pra trás, nem pra frente",
    "letra d)":"Agarrado no pescoço do cavalo",
    
}

prova=[]
gabarito=['b','c','a','d','b']
marcacoes=[]

prova.append(questao1)
prova.append(questao2)
prova.append(questao3)
prova.append(questao4)
prova.append(questao5)

for num,questao in enumerate(prova):
    print(num+1,")",questao["enunciado"])
    print("a)",questao["letra a)"])
    print("b)",questao["letra b)"])
    print("c)",questao["letra c)"])
    print("d)",questao["letra d)"])
    marcacoes.append(input("Digite a letra da resposta escolhida: \n"))

print("O gabarito é:",gabarito)

nota=0

for i in range(0,5):
    if marcacoes[i] == gabarito[i]: nota=nota+20   

# if marcacoes[0] == gabarito[0]:
#     nota1=nota+20

# if marcacoes[1] == gabarito[1]:
#     nota2=nota1+20

# if marcacoes[2] == gabarito[2]:
#     nota3=nota2+20
   
# if marcacoes[3] == gabarito[3]:
#     nota4=nota3+20
   
# if marcacoes[4] == gabarito[4]:
#     nota5=nota4+20
   
print("Sua nota total é: ",nota," Pontos")

