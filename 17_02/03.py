def concat_strings(*args):
    str = []
    for i in args:
        if type(i) == int: 
           str.pop()
        
    return str

print(concat_strings("Hello", "world", "!"))
print(concat_strings("Python", 123, "is", "fun"))