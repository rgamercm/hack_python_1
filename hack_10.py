"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    result = result.replace(result[6], "@")
    result = result.replace(result[1:2], "0")
    result = result.replace(result[4], "1")
    lista = []
    for i in range(8):
        lista.append(result[i]) 
    return lista 

r= fn_hack_10()
print(r)