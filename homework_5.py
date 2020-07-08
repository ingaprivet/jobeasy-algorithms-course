# TODO: When given a list, the program should return
# a list of all the elements that are below the
# arithmetical mean of the original list.
# The arithmetical mean is the sum of all elements divided by the number of elements

def return_num_below_mean(n_num):
    print(f'Data entered for testing:' + str(n_num))
    mean = sum(n_num) / len(n_num)
    print(f'The arithmetical mean of the data: ' + str(mean))
    array_of_numbers = []
    j = 0
    while j < len(n_num):
        if n_num[j] < mean:
            array_of_numbers.append(n_num[j])
        j += 1
    return array_of_numbers


print(f'******** Test One ***********')
print(f'List of the items below the arithmetical mean: ' + (str(return_num_below_mean([1, 2, 3, 4, 5]))))
print(f'******** Test Two ***********')
print(f'List of the items below the arithmetical mean: ' + (str(return_num_below_mean([0, 9, 3, 1, 5]))))


# TODO: When given a list of elements find the two lowest elements. They can be equal to each other or different.
def two_lowest_elements(array):
    print(f'Data entered for testing:' + str(array))
    lowest = array[0]
    lowest2 = None  # the beginning
    for item in array[1:]:
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 is None or lowest2 > item or lowest2 == item:  # the first and > and the same
            lowest2 = item

    print("The smallest element among the entered data is:", lowest)
    print("The second smallest element among the entered data is:", lowest2)


print(f'*****************************')
print(f'*****************************')
print(f'*****************************')
array = [2, 12, 1, 2, 41, 1.8, 2, 10, 8, 6, 4, 2]
two_lowest_elements(array)
print(f'********* Test Two **********')
array = [99, 12, 1, 2, 1, 0.98, 2, 10, 8, 0, 4, 2]
two_lowest_elements(array)


# TODO: Mathematically, the sum of the nth line of odd numbers is n3, so this gives the correct result:
def row_sum_odd_numbers(input):
    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    print(f'**************************')
    print(f'Triangle data: ' + str(array))
    print(f'Testign for line: ' + str(input))

    total = 0
    start_from = 0
    j = 1
    x = 0

    while j < input:
        start_from += j  # find out first Index
        j += 1

    j = start_from

    while j < (start_from + input):
        total += array[j]
        j += 1
    print(f'The sum of the odd numbers is : ' + str(total))


row_sum_odd_numbers(1)  # 1
row_sum_odd_numbers(2)  # 3 + 5 = 8
row_sum_odd_numbers(3)  # 7 + 9 + 11 = 27
row_sum_odd_numbers(5)  # 125
