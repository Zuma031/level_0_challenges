def print_Common(word_i, word_ii):
    common = "Common letters: "
    temp_string_i = word_i.lower()  
    temp_string_ii = word_ii.lower() 
    for i in temp_string_ii:  
        if(temp_string_i.count(i) > 0):
            if(i != " "):
                common+=i+", "
    common= common[:-2] 
    return common

print(print_Common("Ear","Dear"))