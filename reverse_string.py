'''
#----reverse program-----
#1.
text = ["h","o","p"]
text=text[::-1] # slice operator[begin:end:step] -1 denote the reverse fn
print(text)

#2.
input_text= input("give input: ")
result =" ".join(reversed(input_text)) # join used to read and separate char by space reversed() used to read fron last
print (result)
'''
#3
class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        s=list(s)
        left=0
        right = len(s)-1
        s="iCEcrEam"
        
        while left < right:
            while left < right and s[left] not in vowels:
                left +=1
            while left < right and s[right] not in  vowels:
                right -=1

            s[left],s[right] =s[right],s[left]
            left +=1
            right -=1
            
        return " ".join(s)
    
    
                   

         
