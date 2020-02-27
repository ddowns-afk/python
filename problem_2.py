#number = int(input('Enter a number: '))

#if number % 4 == 0:
#     print('Your number is a multiple of 4!')
#elif number % 2 == 1:
#    print('You have entered an odd number!')
#elif number % 2 == 0:
#    print('You have entered an even number!')

num = int(input('Enter a number: '))
check = int(input('Enter another number: '))

if num % check == 0:
    print(str(check) + ' divides evenly into ' + str(num) + '!')
else:
    print(str(check) + ' does not divide evenly into ' + str(num) + '!')