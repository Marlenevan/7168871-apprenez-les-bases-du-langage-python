# Ecrivez votre code ici !
nombres=input("entrer une liste de nombres separée par des virgules: ")
liste=nombres.split(",")
for i in range(len(liste)):
	liste[i]=int(liste[i])
j=0
somme=0
while j<len(liste):
     somme=somme + liste[j]
     j+=1
moyenne=somme/len(liste)
print(f"la somme est: {somme}")
print(f"la moyenne est: {moyenne}")
nbre=0
for i in range(len(liste)):
    if liste[i]>moyenne:
        nbre+=1
print(f"{nbre} nombres sont superieurs à la moyenne")
