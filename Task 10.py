def common(text):
    string1 = "natural"
    string2 = "neutral"

    s1 = set(string1)
    s2 = set(string2)

    common_letters = s1 & s2

    print(", ".join(s1 & s2))

common("common_letters")