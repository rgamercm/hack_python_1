"""
loop: while [] output => [5,4,3,2,1,0]
"""
def fn_hack_7():
    result = []
    contador = 5
    while(contador >= 0):
        result.append(contador)
        contador -= 1
        
    return result  

r= fn_hack_7()
print(r)