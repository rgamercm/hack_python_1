"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    result = "fooziman"
    result = result[0].upper() + result[1:]
    return result

r= fn_hack_3()
print(r)