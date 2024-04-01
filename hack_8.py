"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    result.remove(result[0])
    result.remove(result[3])
    
    return result  

r= fn_hack_8()
print(r)