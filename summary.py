
number_repeat = int(input("Add meg hogy hány számot szeretnál megadni: "))
number_sum = 0
for i in range(0, number_repeat):
    number = int(input("Add meg a " + str(i+1) + ". számot: "))
    if number > 0 and number % 2 == 0:
        number_sum += number
print("Az eredmény a - " + str(number_sum))