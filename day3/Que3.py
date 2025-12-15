def count_vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for ch in text:
        if ch in vowels:
            count+=1
    return count

def count_consonants(text):
    count=0
    for ch in text:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count+=1
    return count

def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return "Undefined (no consonants)"
    return vowels / consonants

string = input("Enter a string: ")

vowels = count_vowels(string)
consonants = count_consonants(string)
ratio = vowel_consonant_ratio(vowels, consonants)


print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Ratio of vowels to consonants:", ratio)
