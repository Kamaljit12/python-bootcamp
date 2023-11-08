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