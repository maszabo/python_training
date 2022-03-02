
szam = 5
sztring = "cica"
sztring2 = "cica2"

# print(szam+sztring) # unsupported operand type(s) for +: 'int' and 'str'
# print(sztring+szam) # can only concatenate str (not "int") to str
# print(sztring-sztring2) # unsupported operand type(s) for -: 'str' and 'str'
# print(sztring*sztring2) # can't multiply sequence by non-int of type 'str'
# print(sztring*szam) # annyiszor írja ki

result = 6 * 5 * 4
print(result)

number_of_apples = 5
number_of_baskets = 3
number_of_all_apples = number_of_apples * number_of_baskets
print(number_of_all_apples)

message = "A valtozo tipusa: " + str(type(sztring))
print(message)