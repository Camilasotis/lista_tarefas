def saudacao(nome,hora):
   if hora>=0 and hora<=12:
      print("BOM DIA!")
   elif hora>12 and hora<=18:
      print("BOA TARDE!")
   else: 
      print("BOA NOITE")

usuario=str(input("Digite seu nome:"))
hora_relogio=int(input("Digite a hora (formato 24h):"))

saudacao(usuario,hora_relogio)