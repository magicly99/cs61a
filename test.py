def t0():
    return 0

def t1():
    return 1

def t(who):
    if who==0:
        return t0
    else:
        return t1

print(t(0)())