name = input('Zadejte svoje jméno: ')
correct=0
success_rate=0

print("Test na znalosti o České republice")
print("----------------------------------")
print("Nemusíte dodržovat diakritku. Rozlišujte ale prosím velká a malá písmena.")
q1= input('Jaký je nejvyšší bod v České republice?: ')
if q1 == "Sněžka" or q1 == "Snezka":
    success_rate+=20
    correct+=1

q2= input('Jaká je nejdelší řeka v České republice?: ')
if q2 == "Vltava":
    success_rate+=20
    correct+=1

q3= input('V jakém roce vznikla samostatná Česká republika?: ')
if q3 == "1993":
    success_rate+=20
    correct+=1

q4= input('Kdo napsal slova k české hymně?:')
if q4 == "Frantisek Skroup" or q4 == "František Škroup":
    success_rate+=20
    correct+=1

q5= input('Jak se nazývá město, ve kterém se nachází nejstarší český most?: ')
if q5 == "Písek" or q5 == "Pisek":
    success_rate+=20
    correct+=1

print("Uživatel",name,"vyplnil",correct,"/ 5 otázek spávné (",success_rate,"% úspěšnost)")
