def fprimo(n):

    if n // 1 == n or n // n == 1:
        primo = True
    else:
        primo = False
    return primo

n = int(input())

if fprimo(n):
    msg = 'primo'
else:
    msg = 'não primo'

print(msg)