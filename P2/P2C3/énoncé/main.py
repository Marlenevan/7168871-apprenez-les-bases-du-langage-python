# Ecrivez votre code ici
def salaire_mensuel(salaire_annuel):
	resultat=salaire_annuel/12
	return resultat

def salaire_hebdomadaire(salaire_mensuel):
	resultat=salaire_mensuel/4
	return resultat

def salaire_horaire(salaire_mensuel,heures_travaillees):
	resultat=salaire_mensuel/heures_travaillees
	return resultat

sal_an=float(input("entrer votre salaire annuel: "))
heure=float(input("entrer votre cotats horaire mensuel: "))
mensuel=salaire_mensuel(sal_an)
hebdomadaire=salaire_hebdomadaire(mensuel)
horaire=salaire_horaire(mensuel,heure)
print(f"votre salaire horaire est de {horaire} euros")
