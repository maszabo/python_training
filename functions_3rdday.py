#írjatok 1 get_max nevű FV, - param 2 foat, return nagyobbat

def get_max(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Egyenlőek"

print(str(get_max(3.14,6.666)))

def print_square(c,d):
    for i in range(1,d+1):
        for j in range(1,c+1):
            if i == 1 or i == d or j == 1 or j == c:
                print(end="* ")
            else:
                print(end=" ")
        print("\n")

print_square(7,5)


def concalist(list):
    newlist =""
    for i in list:
        newlist += "-" + i + "-"
    return newlist

clist = ["Alma", "Körte", "Róka", "Béka"]
print(concalist(clist))