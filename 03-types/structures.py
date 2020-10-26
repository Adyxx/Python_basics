
veta =list("Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech.")
vypis = []
numbers = []
chars = []

def charFrequency(retezec):
    for i in range(0,len(veta)):
      if (retezec[i] not in chars):
        numbers.append(retezec.count(retezec[i]))
        chars.append(retezec[i])

    vypis = list(zip(chars, numbers))
    print("Četnost výskytu písmen:\n--------------------------")
    for i in range(0,len(vypis)):
        print(vypis[i])

charFrequency(veta)
