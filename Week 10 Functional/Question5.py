# TANISHA BISHT
# RA1911003010259

# Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in
# Python.

def make_bold(func):
    def wrapped():
        return '<b>'+ func() +'<b>'
    return wrapped

def make_italic(func):
    def wrapped():
        return '<i>'+ func() +'<i>'
    return wrapped
    
def make_underline(func):
    def wrapped():
        return '<u>'+ func() +'<u>'
    return wrapped

@make_bold
@make_italic
@make_underline
def decorators():
    return 'This content is inside decorators'
print(decorators())