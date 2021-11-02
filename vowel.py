def isVowel(letter):
    if letter in "aeiou":
        return False
    else:
        return True



x = input("inserisci lettera")
print (isVowel(x))