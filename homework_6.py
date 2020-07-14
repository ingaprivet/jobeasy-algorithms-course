def get_sum(array, array_size):
    if array_size == 0:
        return 0
    else:
        # Find sum
        sum1 = int(array[array_size - 1]) + int(get_sum(array, array_size - 1))
        return sum1


def summ(array):
    if len(array) == 1:
        return array[0]
    else:
        value = array[0:1]
        array = array[1:]
        # Find sum
        sum = int(value[0]) + int(summ(array))
        return sum


def get_array(testString):
    number = ""
    array = []
    testString = testString + " "

    for i in range(0, len(testString)):
        if testString[i] != ' ':
            number = number + testString[i]

        else:
            array.append(number)
            number = ""
    print("List of numbers for this test is {0}".format(array))
    return array


def maximum_num(array, array_size):
    if array_size == 1:
        return array[0]
    # print("array size = " + str(array_size))
    # print("start point = " + str(array[array_size - 1]))
    # print("end point = " + str(maximum_num(array, array_size - 1)))

    return max(array[array_size - 1], maximum_num(array, array_size - 1))


while True:
    array_element = input(
        f'Please enter numbers to test '
        f'a "sum up all numbers" and '
        f'the "the biggest number in the list" functions: ')
    if array_element == "":
        print(
            f'Your input must be numberic and consist of a number of elements. Please check your input and try again.')
        break
    else:
        array_input = get_array(array_element)
        array_size = len(array_input)
        print("Test example from Ilya: Sum is {0}".format(summ(array_input)))
        print("One more Test variation of coding: Sum is {0}".format(get_sum(array_input, array_size)))
        print("Test example: The biggest number is {0}".format(maximum_num(array_input, array_size)))
        break
