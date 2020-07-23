from random import randint


def bubble_sort_from_Ilya(array):
    # for i, _ in enumerate(array):
    # or
    for item in range(len(array)):
        j = 0
        while j < len(array) - 1:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        # print(array)
    return array


n = 5
unsorted_list = []

for _ in range(n):
    unsorted_list.append(randint(1, 99))

print(f'input: {unsorted_list}')
print()
print(f'output of insertion sort example from Ilya: {bubble_sort_from_Ilya(unsorted_list)}')


# TODO bubble sort using a given key

def bubble_sort(array, key):
    # for i, _ in enumerate(array):
    # or
    for item in range(len(array)):
        j = 0
        while j < len(array) - 1:
            if array[j][key] > array[j + 1][key]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
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
    }
]
print(f'****************************')
print(f'input: {unsorted_list}')
print()
print(f'This one is our final array of the selection sort of the '
      f'list of dictionaries using a key: '
      + str(bubble_sort(unsorted_list, key='age'))
      )
