def common():
    string1 = "I love python"
    string2 = "I think python is cool"
    s1 = set(string1)
    s2 = set(string2)
    common_letters = s1 & s2
    print(s1 & s2)

common()