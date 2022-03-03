# name = input("Add meg a neved: ")
# empty_string_len_null = ""
#
# if len(name) == 0: # vagy if n ame == ""
#     print("Nem jó, üres a név")

# name = input("Add meg a neved: ")
# age = input("Add meg a korod: ")
# if int(age) < 20:
#     print(name + " te túl foatal vagy.")

name = ""
while name == "":
    name = input("Add meg a neved: ")
    if name == "":
        print("Nem adhatsz meg üres értéket.")
print("Köszönöm!")


