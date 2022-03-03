
### 10 es szorzó tábla
def table():
    for i in range(1,11):
        for j in range(1, 11):
            print(str(int(i*j)) + "\t", end ="")
            if j == 10:
                print("")
            j += 1
        i += 1

table()

# hozz létre egy digist függvény kiírja paraméterül adott szám számjegeit

# def digits(numbers):
#     for i in str(numbers):
#         print(i)
#
# digits(1683)

def szamjegyek(szam):
    while szam > 10:
        maradek = szam % 10
        print(maradek)
        szam = szam // 10
    print(szam)

szamjegyek(8673432)