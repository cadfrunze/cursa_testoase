

def adunare(n1, n2):
    """Calculator adunare"""
    return n1 + n2

def scadere(n1, n2):
    """Calculator scadere"""
    return n1 - n2

def inmultire(n1, n2):
    """Calculator inmultire"""
    return n1 * n2


def impartire(n1, n2):
    """Calculator impartire"""
    return n1 / n2

def calculator(n1, n2, funct):
    """Calculator"""
    return funct(n1, n2)



result = calculator(5, 4, impartire)
print(result)