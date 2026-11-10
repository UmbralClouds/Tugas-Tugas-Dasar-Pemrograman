Sentence = input("Input a sentence : ")

TotalCharacters = len(Sentence)
TotalCharactersMinus = sum(1 for char in Sentence if char.isalpha())

print(f"Total characters : {TotalCharacters}")
print(f"Total characters (without spaces) : {TotalCharactersMinus}")
