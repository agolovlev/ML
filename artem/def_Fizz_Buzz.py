def generate_fizz_buzz_list(a):
    my_list = []
    for i in range(1,a+1):
        FuzzBuzz = ''
        if i%3==0:
            FuzzBuzz = 'Fizz'
        if i%5==0:
            FuzzBuzz = FuzzBuzz + 'Buzz'
        my_list.append(FuzzBuzz if FuzzBuzz != '' else i)
    return(my_list)

print(generate_fizz_buzz_list(4))