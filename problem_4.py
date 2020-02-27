number = int(input('Enter a number: '))

divisors = range(1,number+1)

for term in divisors:
    if number % term == 0:
        print(term)
