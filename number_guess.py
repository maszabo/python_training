
print("Gondolj egy számra 1 és 100 között, én kitalálom.")
interval_start = 1
interval_end = 100
bigger_or_lower = "a"
guess = ""
while bigger_or_lower != "E":
    guess = int((interval_start+interval_end) / 2)
    bigger_or_lower = input("A szám amire gondoltál Nagyobb [N] / Kisebb [K] / Egyenlő [E] mint " + str(guess) + " ? - ")
    if bigger_or_lower == "K":
        interval_end = guess-1
    if bigger_or_lower == "N":
        interval_start = guess+1
print("A gondolt szám a " + str(guess))
