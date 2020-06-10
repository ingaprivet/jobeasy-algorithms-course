# number 1
sample_list = []
counter = 0

while True:
    sample_num = input("Please enter the number of items to sum up: ")
    if sample_num.isdigit():
        sample_num = int(sample_num)
        break
    else:
        print("Invalid entry.  Try again.")

length = sample_num

while counter < length:
    item = input("Please enter the item to build the list: ")
    if item.isdigit():
        item = int(item)
        sample_list.append(item)
        counter += 1
    else:
        print('Invalid entry.  Try again.')

print("Sum of the items in the entered list is :", sum(sample_list))

# number 2
sample_list = []
counter = 0
length = 3

while counter < length:
    item = input("Please enter up to 3 numbers to complete the task: ")
    if item.isdigit():
        item = int(item)
        sample_list.append(item)
        counter += 1
    else:
        print('Invalid entry.  Try again.')

print("The max number entered is:", max(sample_list))


# 3. Count odd and even numbers.

def sum_digits(string_num):
    counter_odd = 0
    counter_even = 0
    for char in string_num:
        if int(char) % 2 == 0:
            counter_even += 1
        else:
            counter_odd += 1
    print("Number of even digits = {}:".format(counter_even))
    print("Number of odd digits = {}:".format(counter_odd))


while True:
    string_num = input("Please enter a number : ")
    if string_num.isdigit():
        sum_digits(string_num)
        break
    else:
        print("Invalid entry. Try again.")


