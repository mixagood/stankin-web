'''
LAB #2
Mishchenko Mikhail
IDB-20-07
2022

git: 
https://github.com/mixagood/stankin-web

ALL TASKS + TESTS + CACHE_DECORATOR WITH PARAM
'''
def cache_decorator(counter=3):
    def _cache_decorator(func):
        cache = dict()

        def wrapper(*args):
            
            print(cache)

            if ((args not in cache) or (args in cache and cache[args][1] <= 0)):
                cache[args] = [func(*args), counter]
            else:
                cache[args][1] -= 1

            return cache[args][0]

        return wrapper
    return _cache_decorator



# task1 (palindrome int)
@cache_decorator(3)
def int_palindrome(number):
    n = str(number)
    for i in range(len(n) // 2):
        if (n[i] != n[len(n) - 1 - i]):
            return False
    return True


# task 2 (form 3 lists)
def formlists(list1):

    listmod2 = []
    listmod3 = []
    listmod5 = []

    for i in list1:
        if (i % 2 == 0):
            listmod2.append(i)
        if (i % 3 == 0):
            listmod3.append(i)
        if (i % 5 == 0):
            listmod5.append(i)
    
    return listmod2, listmod3, listmod5


@cache_decorator(3)
def reverseint(number):

    # clear zeros on end 
    strnumber = str(number)
    strnumber = strnumber.rstrip('0')

    if (strnumber == ''):
        return 0

    # sign check
    signs = ['-', '+']
    sign = ''
    if (strnumber[0] in signs):
        sign = strnumber[0]
        strnumber = strnumber[1::]

    # reverse + add sign
    strnumber = sign + strnumber[::-1]

    # conversion
    retnumber = int(strnumber)

    return retnumber

@cache_decorator(3)
def root_newton(number, power, accuracy, start=1):
    n = power
    x_iter = start

    for i in range (accuracy):
        x_iter = (1 / n) * ((n - 1) * x_iter + number / x_iter ** (n - 1))
    
    return x_iter


@cache_decorator(3)
def isprime(number):
    number = int(number)
    if (number != 2 and number % 2 == 0):
        return False
    for i in range(3, int(number ** (0.5)) + 1, 2):
        if (number % i == 0):
            return False    
    return True


# testing functions: (list with tpls (input, expected) and function)
def tests(test_cases, test_func):
    total_tests = len(test_cases)
    success_ctr = 0

    for i in range(total_tests):
        expected = test_cases[i][1]
        inputvalue = test_cases[i][0]
        retvalue = test_func(inputvalue)

        passed = (retvalue == expected)
        if (passed):
            success_ctr += 1
        else:
            print(f"{test_func.__name__} test #{i} failed, for {inputvalue} expected {expected} got {retvalue}")

    print(f"Summary testing {test_func.__name__} : passed {success_ctr} of {total_tests} tests")


test_cases_for_reverseint = [(12, 21), (120000, 21), (-123, -321), (0, 0), (000, 0), (-0, 0), (1, 1), (-1, -1)]

test_cases_for_isprime = [(1000, False), (100000, False), (997, True), (1, True), (2, True), (3, True), (4, False), (25, False)]

test_cases_for_intpalindrome = [(123456, False), (123321, True), (0, True), (1, True), (-1, False)]

test_cases_for_formlists = [([0], ([0], [0], [0])), 
                            ([1], ([], [], [])),
                            ([30], ([30], [30], [30])),
                            ([], ([], [], [])),
                            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ([2, 4, 6, 8, 10], [3, 6, 9], [5, 10]))]


tests(test_cases_for_reverseint, reverseint)
tests(test_cases_for_formlists, formlists)
tests(test_cases_for_intpalindrome, int_palindrome)
tests(test_cases_for_isprime, isprime)
