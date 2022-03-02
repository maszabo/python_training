name = input("Add meg a neved: ")
repeat = input("Hányszor ismétlődjön? - ")

for i in range(1, int(repeat)+1):
    print(str(i) + " " + name)