#  Write a program to fill in a letter template given below with name and date. 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace("<|Name|>", "anish"),letter.replace("<|Date|>", "06/05/2025")) 
# here is the simple we replace the str with using replace function