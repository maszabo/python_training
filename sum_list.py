
def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    print("Számok összege: " + str(sum))

numbers = [1,2,5,8]
sum_list(numbers)