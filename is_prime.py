def is_prime(u1):
    
    for term in range(2,u1 + 1):

        if term == u1:
            print(str(u1) + ' is a prime number!')

        elif u1 % term != 0:
            continue
        else:
            print(str(u1) + ' is not a prime number!')
            break
    
