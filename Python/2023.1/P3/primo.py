def fprimo(n):
    div = 2
    while n % div != 0:
        div += 1
    if n == div:
        msg = 'primo'
    else:
        msg = 'não primo'
    return msg

num = int(input())
msg =fprimo(num)
print(msg)