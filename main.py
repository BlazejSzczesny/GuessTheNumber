import random
def guess(rand):
    print("Podaj zgadywaną liczbę:")
    x=int(input())
    while(x!=rand):
        print("źle")
        if(x>rand):
            print("Twoja liczba jest za duża")
        if(x<rand):
            print("Twoja liczba jest za mała")
        x=int(input("Podaj liczbę:"))
    if (x == rand):
        print("Udało się!\nTwoja liczba to", x,"!")

def generateRandomNumberToGuess(a,b):
    rand=random.randint(a, b)
    guess(rand)

def main():
    print("Podaj zakres liczb")
    a=int(input("od:"))
    b=int(input("od:"))
    generateRandomNumberToGuess(a,b)

if __name__ == '__main__':
    main()