def vowel(text):
    vowels = "aeiouAEIOU"
    res = [letter for letter in text.lower() if letter in vowels]
    print(", ".join(res))
    
vowel("BEautiFUL")
