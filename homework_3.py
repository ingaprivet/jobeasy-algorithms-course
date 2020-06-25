# 1. Python function, which will count how many times
# a character (substring) is included in a string


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


'''
# 2. Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings.

def substring_replacement(string, substring_01, substring_02):
    len_01 = len(string)
    len_02 = len(substring_01)

    print("len_01 = " + str(len_01))
    print("len_02 = " + str(len_02))
    can_be_replaced = False
    j = 0

    while j < len_01:
        if string[j] == substring_01[0]:
            print("string[j] = " + string[j])
            print("substring_01[0] = " + substring_01[0])
            print("found a matching letter")

            print("string[j:j + len_02] = " + string[j:j + len_02])
            print("substring_01 = " + substring_01)

            if (string[j:j + len_02] == substring_01):
                print("found a matching substring")
                print("string before replacement: " + string)
                placement_for_string_rest = int[j:j+]
                can_be_replaced = True

            #else:
            #    print("Invalid entry. No substring match has been found. Please try again!")

        j += 1
        if can_be_replaced:
            print("in flag = true")

            string = string[0:j] + substring_02[0:]
            print("string after replacement: " + string)
            break


while True:
    can_be_replace = False
    string = input("Please enter your String: ")
    substring_01 = input("Please enter the Substring to be replaced: ")
    substring_02 = input("Please enter the Substring to used for replacement: ")
    substring_new_01 = ""
    substring_new_02 = ""
    substring_new_03 = ""

    if (string == "" and substring_01 == "" and substring_02 == "") or (
            not string.isalpha() and not substring_01.isalpha()) and not substring_02.isalpha():
        print("Your input is not alphabatical. Please check your input and try again.")
        break
    else:
        print("going to execute a function")
        substring_replacement(string, substring_01, substring_02)
        break
'''
