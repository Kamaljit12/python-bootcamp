# create fuction
def greet():
    print("Hello kamal !")

# call the function
greet()


# add two number 

def sum(num1, num2):
    res = num1 + num2
    print(res)

sum(10, 20)

# even check function

def is_even(n):
    if n % 2 == 0:
         print(f'{n} is even !')
    else:
        print(f'{n} is odd !')


is_even(10)
is_even(7)

# string call
def full_name(fname, lname):
    print(fname, lname)


full_name('kamal', 'singh')

# square functions

def square(n):
    res = n**2
    print("square is :", res)

square(10)

# square root finder

def square_root(n):
    res = n**0.5
    
    print('square root of {} is '.format(n), res)

square_root(8)
square_root(9)


# get square of the list
ls = [1, 2, 3, 4, 5]

def get_square(n):
    for i in n:
        res = i**2
        print('square of the list is :', res)

get_square(ls)


# get the square of the list
def square_of_list(lst):
    for i in lst:
        ls = i**2

print("square_of_list is =", ls)
square_of_list(ls)


# squre fucntion with default value

def square_fun(n=1):
    res = n*n
    print("squre of {} is :".format(n), res)

square_fun(10)
square_fun(5)
# i will not pass any argumnet even though i will get result
square_fun()


# fuction argument with default value
def add_num(a = 5, b = 10):
    res = a+b
    print("sum of {} and {} is :".format(a, b), res)

add_num()