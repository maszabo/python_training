# Hozz létre egy is_even nevű függvényt,
# amely True-t ad vissza, ha a paraméterként megadott
# érték páros, egyéb esetben False-t adjon vissza

def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False

print(is_even(1))
print(is_even(2))

####################################################
# Hozz létre egy sum_negatives függvényt, mely paraméterül kap egy listát,
# és összegzi a benne szereplő negatív számokat, és azzal tér vissza
def list_sum(list):
    sum = 0
    for i in list:
        if i < 0:
            sum += i
    return sum

list = [1,-1,2,-2,3,-10]
print(list_sum(list))

####################################################
# Hozz létre egy to_minutes függvényt, mely paraméterül megkapja
# az órák számát, és visszatér a percek számával
def to_minutes(hours):
    return hours*60

print(to_minutes(2))

####################################################
# Hozz létre egy input_number függvényt, melynek legyen egy
# paramétere. A függvény bekér a felhasználótól egy szöveget
# a paraméterrel megadott szöveggel, számmá konvertálja és azt adja vissza
def input_numer(param):
    number_text = input("Adj meg egy számot: ")
    return int(number_text)

####################################################
# Írjatok egy annotate_every_even_number függvényt, mely kap egy
# számok listáját, és kiírja őket egymás alá, de minden másodikat
# egy karakterrel beljebb ír ki

def annotate_every_even_number(list):
    j = 1
    for i in list:
        if j % 2 == 0:
            print("  " + str(i))
        else:
            print(str(i))
        j += 1

annotate_every_even_number([1,3,2,4,10,50,20])

####################################################

def conca_shorts(list):
    full_list = ""
    for i in list:
        if len(i) <= 3:
            full_list += i
    return full_list

print(conca_shorts(["Kék", "Zöld", "Red","Kutya","Három","Kár"]))