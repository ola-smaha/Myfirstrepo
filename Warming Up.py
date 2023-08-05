# Problem 1
#(assuming n is non-negative, we include the case of n=0)

# first method: iteratively
def factorial_1(n):
    if n == 0:
        return 1
    result = n
    while n>1 :
        result *= (n-1) 
        n -= 1
    return result

# second method: recursively
def factorial_2(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n*factorial_2(n-1)
    

# Problem 2
def fizz_buzz(n):
    for i in range(1,n+1):
        if (i%3 == 0 and i%5 == 0):
            print('FizzBuzz')
        elif (i%3 == 0):
            print('Fizz')
        elif (i%5 == 0):
            print('Buzz')
        else:
            print(i)


# Problem 3
def char_frequency(text):
    char_dic = dict()
    txt = text.replace(' ','')
    for char in txt:
        char_dic[char] = text.count(char)
    return char_dic


