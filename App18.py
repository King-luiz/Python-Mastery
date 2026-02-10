# keyword arguments


def increment(number, by):
    return number + by

# result = increment(2,1)
# print(result)

# or we can write

print(increment(2,by= 1))

print("               ")
# default argument

def increment(number, by=1):
    return number + by
print(increment(2,5))


# args, wait, what?

print("             ")
# this creates a tuple
def multiply(*numbers):
    print(numbers)
    
# def multiply(x,y):
multiply(2,3,4,5)
print ("             ")


# also iterating inside of the tuple

def multiply(*numbers):
    total =1
    for number in numbers:
        total *= number
    return total

print(multiply(2,3,4,5))    