'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# -Kolekce, která je neuspořádaná, proměnlivá a indexovaná

# In Python dictionaries are written with curly brackets, and they have keys and values.
# -V pythonu jsou slovníky psány se složenými závorkami a mají klíče a hodnoty

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

films = {
  'first' : {
    'name' : 'Titanic',
    'year' : '1997',
    'czdabing' : True,
    'cinema' : ('2.1. 1998','3.1. 1998'),
    'hraje' : ['Leonardo DiCaprio', 'Kate Winslet'],
    'set' : {'James Cameron'}
  },
  'second': {
    'name': 'Hunger games',
    'year': '2012',
    'czdabing': True,
    'cinema': ('9.9. 2012', '3.9. 2012'),
    'hraje': ['Jennifer Lawrence', 'Josh Hutcherson'],
    'set': {'Gary Ross', 'Billy Ray'}
  },
  'third': {
    'name': 'Film bez cz dabingu',
    'year': '2020',
    'czdabing': False,
    'cinema': ('25.6. 2020', '27.6 2020'),
    'hraje': ['Bruce Willis','Tom Hanks'],
    'set': {'Suzanne Collins'}
  }
}

del films['third'] # odstranění filmu #3 z dict (protože nemá cz dabing)

films['fourth'] = {
  'name': 'Matrix',
  'year': '1999',
  'czdabing': True,
  'cinema': ('2.7. 1999', '5.7. 1999'),
  'hraje': ['Keanu Reeves','Hugo Weaving'],
  'set': {'Lana Wachowski', 'Lilly Wachowski'}
}

valuess= []
for key, value in films['first'].items():
    valuess.append(value)
for key, value in films['second'].items():
    valuess.append(value)
for key, value in films['fourth'].items():
    valuess.append(value)

names=valuess[::6]
years=valuess[1::6]
dabings=valuess[2::6]
cinemas=valuess[3::6]
hraje=valuess[4::6]
sett=valuess[5::6]
print(" Název filmu        Rok vydání        Cz Dabing          V kině                           Herci                                           Scénář")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("{}             {}              {}              {}        {}           {}\n{}        {}              {}              {}        {}        {}\n{}              {}              {}              {}        {}                {}".format(names[0],years[0],dabings[0],cinemas[0],hraje[0],sett[0],names[1],years[1],dabings[1],cinemas[1],hraje[1],sett[1],names[2],years[2],dabings[2],cinemas[2],hraje[2],sett[2]))
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
