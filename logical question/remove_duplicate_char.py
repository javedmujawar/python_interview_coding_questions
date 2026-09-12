text ="programming"
def remove_duplicate_char(text):
    result = ""
    for char in text:
        if char not in result:
            result = result + char
    return result        

print(remove_duplicate_char(text))        