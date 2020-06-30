# TODO: Python function, which will count how many times a character (substring) is included in a string.


def sum_letters(string_entered):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    count = 0

    for j in range(0, 26):
        if count != 0:
            print("The letter", alphabet[j - 1], "has occurred", count, "times")
        count = 0
        for i in range(len(string_entered)):
            if alphabet[j] == string_entered[i]:
                count = count + 1


while True:
    string_entered = input("Please enter an alphabatical test string: ")
    if string_entered == "" or not string_entered.isalpha():
        print("Your input is not alphabatical. Please check your input and try again.")
        break
    else:
        sum_letters(string_entered)
        break


# TODO: Find and replace a substring in a string for another substring.


def substring_replacement(string, substring_01, substring_02):
    len_01 = len(string)
    len_02 = len(substring_01)
    len_03 = len(substring_02)
    j = 0
    cannot_be_replaced = True

    while j < len_01:  # length of the string entered
        if string[j] == substring_01[0]:
            if string[j:j + len_02] == substring_01:
                print("found a matching substring")
                string = string[0:j] + substring_02 + string[j + len_02:]
                print(f'Result String : ' + string)
                cannot_be_replaced = False
                break
        j += 1
    if cannot_be_replaced:
        print("No match for replacement has been found! Please try again.")


while True:
    cannot_be_replaced = True
    string = input("Please enter your String to test a substring replacement: ")
    substring_01 = input("Please enter the Substring to be replaced: ")
    substring_02 = input("Please enter the Substring to used for replacement: ")

    if (string == "" and substring_01 == "" and substring_02 == "") or (
            not string.isalpha() and not substring_01.isalpha()) and not substring_02.isalpha():
        print("Your input is not alphabetical. Please check your input and try again.")
        break
    else:
        print("going to execute a function")
        substring_replacement(string, substring_01, substring_02)
        break


# TODO: Recursion for digital root.

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


num = int(input("Enter a Number to test a digital root recursion: "))
print("Digital root of {0} = {1}".format(num, digitalroot(num)))


# TODO: Recursion for Fib.

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


print("Fibsequence recursion result for {0} = {1}". format(6,fibsequence(6)))

# TODO: Recursion for factorial.

def factorial(x):
    if x == 1:
        return 1
    else:
        result = x * factorial(x - 1)
        print("intermediate result for ", x, " : ", result)
        return result

print("Factorial recursion result for {0} = {1}". format(5,factorial(5)))
