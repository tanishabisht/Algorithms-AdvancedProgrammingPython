# TANISHA BISHT
# RA1911003010259

# Write a Python program to access a function inside a function : USING DECORATORS

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner


@smart_div
def div(a,b):
    print(a/b)
div(2,4)