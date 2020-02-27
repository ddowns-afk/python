name = input("whats your name? ")
age = input("whats your age? ")

years_to_100 = 100 - int(age)

message = str("you will be 100 in " + str(years_to_100) + " years! ")
print(message)

multiple = int(input("give me another number "))

print(multiple * message)
