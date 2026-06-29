#brute force check all the possibilities one by one until solution found.
def rotateString(s: str, goal: str) -> bool:
    if len(s)!=len(goal):
        return False
    combined = s + s#s=abcdef (s+s=abcdefabcdef  goal = defabc goal ah s+s la checjh panu erukanu)
    return goal in combined
    
s = input("enter:")
goal = input("enter:")
    
result = rotateString(s,goal)
print (f" '{s}' match '{goal}' ? {result}"  )  

      
    
