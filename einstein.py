# 300000000
def main():
    mass = int(input("Please enter the value of mass: "))
    print(energy(mass))


def energy(n):
    e = None
    c = 300000000
    e = n * (square(c))
    return e


def square(n):
    return n * n


main()
