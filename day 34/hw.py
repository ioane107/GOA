def repeat(text, num):
    return text * num

def check(s):
    return s if len(s) > 10 else "Too short"

def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(repeat("hi", 3))
print(check("hello world"))
print(check("hi"))
print(even_or_odd(5))
print(even_or_odd(10))