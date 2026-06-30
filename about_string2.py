#find and replace

#find() -> find substring position if substring not present output:-1
#syntax:string_name.find("substring",start,end)
'''
text = "free fire"
size = len(text)
print(size)
print(text.find("e",5,9))
'''

#index similar to find() but it produce output : error
#syntax -> index("ss",start,end)
'''
text2= "the word is python"
print(len(text2))
print(text2.index("o",5,15))
'''
#count() ->count the letter how time comes if substring not found produce output:0
'''
Text3 = "banana is fruit"
print(len(Text3))
print(Text3.count("i",4,15))
'''
#replace() ->replace substring with new sub_string 
#syntax:("old","new",count)count->n how many times erukunu solu 2 nu thantha first 2 letter mathu
'''
text4 = "banana in fruit"
print(text4.replace("n","i",3))
'''
#startswith() -> check whether substring starts with string output:true/false
'''
text5 = "banana is a fruit"
print(text5.startswith("is",7,14))
'''
#endswith()->check sunstring end check true/false
text6 = "doc.pdf"
print(text6.endswith("pdf"))
