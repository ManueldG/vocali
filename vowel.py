def isVowel(letter):
    if letter in "aeiou":
        return True
    else:
        return False


x = input("inserisci lettera: ")
print ("è una vocale" if isVowel(x) else "non è una vocale")