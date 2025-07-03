# Ecrivez votre code ici !
nombre1=input("entrez un nombre: ")
nombre2=input("entrer un autre nombre: ")
if nombre1.isnumeric() and nombre2.isnumeric():
  nombre1=int(nombre1)
  nombre2=int(nombre2)
else:
  print("les deux nombres doivent être entier")
  raise SystemExit("fin du programme")
operation=input("entrez votre opération souhaitée")
match operation:
  case "+":
    resultat=nombre1+nombre2
  case "-":
    resultat=nombre1-nombre2
  case "*":
    resultat=nombre1*nombre2
  case "/":
    if nombre2==0:
      print("la division par 0 n'est pas posible")
      raise SystemExit("fin du programme")
    resultat=nombre1*nombre2
  case _:
    print("les operateurs possibles sont +,-,*,/")
    raise SystemExit("fin du programme")
print(f"le resultat du calcul {nombre1}{operation}{nombre2}={resultat}")

