
def print_employee_data(name, age):
    """ így megadjuk hogy miről szól ez a függvény"""

    print("Az alkalmazott neve: ", name)
    print("Az alkalmazott eletkora: ", age)

print_employee_data("Béla", 12)
print_employee_data("Gazsi", 20)
print_employee_data("Jóska", 30)

########################################

def osszeg(a, b):
    print("A számok összege: " + str(a+b))

a = int(input("Add meg az első számot: "))
b = int(input("Add meg az második számot: "))
osszeg(a,b)