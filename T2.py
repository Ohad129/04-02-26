rating: int = int(input('enter rating: '))
is_valid: bool = 1 <= rating <= 5
is_best: bool = rating == 5
is_medium: bool = 2 <= rating <= 4
is_positive: bool = rating > 0
is_even: bool = rating % 2 == 0
is_prime: bool = True
if is_valid:
    print('in range')
    if is_best:
        print('highest score')
    else:
        print('not highest score')
        if is_medium:
            print('medium score')
        else:
            print('score high or low')
else:
    print('not in range')
if is_positive:
    print('the number is positive')
if is_even:
    print('even')
if rating > 1:
    for i in range(2, rating):
        if rating % i == 0:
            is_prime = False
else:
    is_prime = False
if is_prime:
    print('number is prime')
else:
    print('number is not prime')
