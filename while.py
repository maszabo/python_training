
# are_you_a_boy = True
# print(are_you_a_boy)
# print(type(are_you_a_boy))
#
# result = 10 < 20
# print(result)
#
# print("alma" == "alma")
# print("alma" == "körte")

# count = 0
# while count<10:
#     print("hello - " + str(count))
#     count = count +1
# print("End")


number = 1
while number!=0:
    number = input("Adj meg egy számot, én meg duplázom. Exit = 0. Számod: ")
    if(int(number)==0):
        break
    print("Duplája: " + str(int(number)*2))
print("End")
