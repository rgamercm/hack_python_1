"""
text: "fooziman" output => "FOOZIMAN"
"""

def fn_hack_1():
    result = "fooziman"
    result = result.upper()
    return result

r= fn_hack_1()
print(r)