from random import randint

MIN_SECRET = 1
MAX_SECRET = 100000

PRIME = 104729

class SecretPair():
    def __init__(self,number,e):
        self.x = int(number)
        self.y = int(e)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

def generate_random_number(min:int,max:int):
    return int(randint(min,max))

def generate_coefficients(k:int,secret:int):
    coefficients = []
    coefficients.append(secret)

    for i in range(1,k):
        coefficients.append(generate_random_number(MIN_SECRET,MAX_SECRET))
    
    return coefficients

def calculate_secret_pairs(n:int,coefficients:[]):
    shareSecretPoints = []

    k = len(coefficients)

    for number in range(1,n+1):
        accumulator = int(coefficients[0])

        for exp in range(1,k):
            current = 1
            for i in range(1,exp+1):
                current = (current * number) % PRIME

            current = (current * int(coefficients[exp])) % PRIME

            accumulator = (accumulator + current) % PRIME

        shareSecretPoints.append(SecretPair(number,accumulator))

    return shareSecretPoints

def gcdExtended(a:int,b:int,x,y):
    if (b==0):
        x = 1
        y = 0
        return (int(x),int(y))
    else:
        n = a / b
        c = a % b

        x1 = y1 = 0
        x1,y1 = gcdExtended(b,c,x1,y1)

        x = y1
        y = x1 - y1 * n
        return (int(x),int(y))


def reconstructSecret(secretPairs:[]):
    secret = 0

    k = len(secretPairs)

    for i in range(0,k):
        upper = 1
        lower = 1

        for j in range(0,k):
            if (i == j):
                continue

            xi = secretPairs[i].getX()
            xj = secretPairs[j].getX()

            upper = (upper * xj * -1) % PRIME
            lower = (lower * (xi - xj)) % PRIME

        yi = secretPairs[i].getY()

        x = y = 0
        prime = PRIME

        ok = 0
        if (lower < 0):
            ok = 1
            lower *= -1

        x,y = gcdExtended(prime, lower, x, y)

        if (ok == 1):
            y *= -1

        lower = (y + PRIME) % PRIME

        current = (upper * lower) % PRIME
        current = (current * yi) % PRIME

        secret = (PRIME + secret + current) % PRIME

    return secret


def ekseptejszyn():
    print("Niepoprawna wartość!!!")
    from os import system
    system("start nope.gif")
    exit()




def split():
    print("Wybierz sekret między: ",MIN_SECRET," , ",MAX_SECRET)
    try:
        secret = int(input())
    except:
        ekseptejszyn()

    print("")
    try:
        n = int(input("n = "))
    except:
        ekseptejszyn()
    try:
        k = int(input("k = "))
    except:
        ekseptejszyn()

    if (n < k):
        ekseptejszyn()

    print("P(x) = (",end="")

    coefficients = generate_coefficients(k,secret)
    for i in range(0,k):
        if (i == k - 1):
            print(coefficients[i],"* x^",k-1,") % ",end="")
        else:
            print(coefficients[i],"* x^",i," + ",end="")
    print(PRIME)

    print("Wygenerowane pary (x , f(x)) to :")
    shareSecretPoints = calculate_secret_pairs(n,coefficients)
    for i in range(0,n):
        print("(",shareSecretPoints[i].getX()," , ",shareSecretPoints[i].getY(),")")


def restore():
    try:
        k = int(input("Wprowadź k = "))
    except:
        ekseptejszyn()

    print("Wprowadź pary: x,y  : ")

    secrets = []
    for i in range(0,k):
        xy = input("> ")
        try:
            xy_list = xy.split(",")
            x = int(xy_list[0])
            y = int(xy_list[1])
        except:
            ekseptejszyn()    

        secrets.append(SecretPair(x,y))

    print("Twój sekret = ",reconstructSecret(secrets))


if __name__ == "__main__":
    #zakres
    MIN_SECRET = 1
    MAX_SECRET = 1000000
    #modulo
    PRIME = 104729

    #wywołanie funkcji
    split()
    restore()