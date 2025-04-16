
def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(total)
    return total


soma(1,2,3)
