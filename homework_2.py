# TODO: HW: Rewrite code, which will return only needed element of Fib sequence
def fibsequence(n):
    if n < 0:
        print("Incorrect input")
    # number is 0
    elif n == 0:
        return 0
    # number is 1
    elif n == 1:
        return 1
    else:
        return fibsequence(n - 1) + fibsequence(n - 2)


print(fibsequence(6))

# TODO Use datetime library to solve problem Seconds to Date
# Write a Python program to convert seconds to day, hour, minutes and seconds.
import datetime


def sec_to_hms(n):
    intermediate_value = datetime.timedelta(seconds=n)
    return str(intermediate_value)

print(sec_to_hms(10121))


# TODO: Zeros not for Heros

def remove_zeros(number):
    while number % 10 == 0:  # remainder of division = 0
        number //= 10  # number = number / 10
    return number


print(remove_zeros(96000))


# TODO: Find a Digital root

def sumdigits(num):
    result = 0

    while num > 0:
        rem = num % 10
        result = result + rem
        num = int(num / 10)
    return result


def digitalroot(n):
    r = sumdigits(n)
    # print("r =" + str(r))
    if r < 10:
        return r
    else:
        return digitalroot(r)


num = int(input("Enter a Number: "))
print("Digital root of {0} = {1}".format(num, digitalroot(num)))
