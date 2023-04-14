def GetReversedString(string):
    string = string[::-1].lower()
    return string.capitalize()

word = "Alucard"

print(GetReversedString(word))