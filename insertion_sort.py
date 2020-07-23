from random import randint


def insertion_sort_from_Ilya(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while array[j] > temp and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
        # print(array)
    return array


n = 5
unsorted_list = []

for _ in range(n):
    unsorted_list.append(randint(1, 99))

print(f'input: {unsorted_list}')
print()
print(f'output of insertion sort example from Ilya: {insertion_sort_from_Ilya(unsorted_list)}')


# TODO insertion sort using a given key

def insertion_sort(array, key):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i][key]
        while array[j][key] > temp and j >= 0:
            array[j + 1][key] = array[j][key]
            j -= 1
        array[j + 1][key] = temp
        # print(array)
    return array


unsorted_list = [
    {
        'name': 'Ilya',
        'age': 26
    },
    {
        'name': 'John',
        'age': 35
    },
    {
        'name': 'Patric',
        'age': 17
    },
]
print(f'****************************')
print(f'input: {unsorted_list}')
print()
print(f'This one is our final array of the insertion sort '
      f'of the list of dictionaries using a key: '
      + str(insertion_sort(unsorted_list, key='name'))
      )
