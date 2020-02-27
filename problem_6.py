input_string = input('Enter any word: ')

if input_string == input_string[::-1]:
    print(input_string + ' is a palindrome!')
else:
    print(input_string + ' is not a palindrome!')

