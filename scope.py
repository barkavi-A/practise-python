#4 scope 1.local , 2.enclosed , 3.global , 4.
#local means variable call inside the function .
def example():
    var1 = 10# local var workk on function only
    var2 = 20
    print(var1)


#2.enclosed means one function create inside the another function parent fun var can used for child function.
'''
def example_1():
    x = 3 #enclosed var
    y = 5
    def example_using():
        z = 4;
        print(x+z)
    #example_using()
#example_1()
'''
#3.global means var declare outside the function any function can access the variable.
'''
item = "tall"
def example_1():
    x = 3 #enclosed var
    y = 5
    print(item , y)
    def example_using():
        z = 4;
        print(x+z)
        print(item)
    example_using()
example_1()
'''
#big scope means it use local,enclosed,global
college ="rr"

def dept():
    class_a= "it"
    def class1():#{var}= variable value pass into string
        print(f"call {college} the student from: {class_a}")#f is used to directly use the variable in the string ,f=format sting literal
    class1() 
dept()  

