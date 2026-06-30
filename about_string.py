#repetation.
'''
repeated = "ha" * 10
print(repeated)
'''
#membership check the character in string
'''
value = "member"
new_word = input("enter value:")

if new_word in value:
   print (f"'{new_word}' in '{value}'")
   
else:
    print(f"'{new_word}' not in '{value}'")   
'''
#lower to upper mostly used for password
text1 ="secure123"
print(text1.upper())    

#upper to lower mostly used in email
text2 = "WELcome@GMAil.com"
print(text2.lower())

#captilize makes the only first letter has upper others are lower
text3 = "hello WOrld"
print(text3.capitalize())

#tittle makes ever first letter of the word is upper
text4 = "i hAVE a cAT"
print(text4.title())

#swapcase convert upper to lower and lower toupper
text5 = "HE is sO beatuIFUL"
print(text5.swapcase())
