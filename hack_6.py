"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = []
    contador = 0
    for i in range(6):
        result.append(contador)
        contador += 1
        
    return result  

r= fn_hack_6()
print(r)