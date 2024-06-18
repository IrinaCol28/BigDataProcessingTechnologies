def separate_vowels_and_consonants(line):
    vowels = ''
    consonants = ''
    for sym in line:
        if sym in 'аоуеэяиюыёАОУЕЭЯИЮЫЁ':
            vowels += sym
        else:
            consonants += sym
    return vowels + consonants


a = input("Введите строку: ")

print("Новая строка: ", separate_vowels_and_consonants(a))
