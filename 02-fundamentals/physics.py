'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace

MOON_RADIUS = 1737100 #poloměr měsíce

SPEED_OF_LIGHT = 299792458 #? (m/s) rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? (m/s) rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def funkce1(e_grav):
    '''
    Tato funkce spočítá velikost dráhy, ze které těleso padalo. (volný pád)
    '''
    cab=input("Zadejte délku pádu (v sekundách): ")
    if int(cab) > 0:
        vys = (0.5*e_grav) * (int(cab)*int(cab))
        print("Těleso padalo z výšky {} m".format(vys))

def funkce2(m_grav, radius):
    '''
    Tato funkce spočítá hmotnost měsíce.
    '''
    res=((m_grav*(radius*radius))/0.0000000000667)
    print("Měsíc váži {}  kg".format(res))

def funkce3(spd_light):
    '''
    Tato funkce spočítá za jak dlouho světlo urazí danou vzdálenost.
    '''
    abb=input("Zadejte vzdálenost (v km): ")
    if int(abb) > 0:
        mmm=int(abb)*1000
        print("Světlo ve vakuu urazí vzdálenost {} km za {} sekund.".format(abb,round(mmm/spd_light,3)))

def funkce4(spd_sound,light):
    '''
    Tato funkce počítá kolikrát je rychlost zvuku pomalejší než rychlost světla.
    '''
    pok=light/spd_sound
    print("Rychlost zvuku je {}x pomalejší než rychlost světla.".format(round(pok,2)))

print(funkce1.__doc__)
funkce1(EARTH_GRAVITY)
print(funkce2.__doc__)
funkce2(MOON_GRAVITY, MOON_RADIUS)
print(funkce3.__doc__)
funkce3(SPEED_OF_LIGHT)
print(funkce4.__doc__)
funkce4(SPEED_OF_SOUND,SPEED_OF_LIGHT)
