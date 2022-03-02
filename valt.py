# Literál - érték
print(5) # egész szám
print(100_000) # kód olvasást segítő alulvonal
print(3.14) # pont kell. Lebegőpontos
print("Hello W") # szöveges literal
print('Hello W') # szöveges literal

# Valtozok
name = "akarmi"
print(name)
employee_name = "Szabó Márton"
print(employee_name)
employee_age = 25
print(employee_age)
print("Név: " + employee_name + "\nKor: " + str(employee_age))

print(type(3.14)) # tipus kiiratás
print(type(employee_age))

print(type(employee_name))

salary: int = 200 # lelked rajta ha előre beállítod
print(salary)
salary = "kétszáz"
print(salary)
