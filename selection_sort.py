from random import randint


def selection_sort_from_Ilya(array):
    # for i, _ in enumerate(array):
    # or
    for i in range(len(array)):
        min_index = i  # will be used to swipe
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        print(array)
    return array


n = 5
unsorted_list = []
for _ in range(n):
    unsorted_list.append(randint(1, 99))

print(f'input: {unsorted_list}')
print()
print(f'output of selection sort example from Ilya: {selection_sort_from_Ilya(unsorted_list)}')

# TODO selection sort using a given key

def selection_sort(array, key):
    # for i, _ in enumerate(array):
    # or
    for i in range(len(array)):
        min_index = i  # will be used to swipe
        for j in range(i + 1, len(array)):
            if array[min_index][key] > array[j][key]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
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
      + str(selection_sort(unsorted_list, key='age'))
      )
