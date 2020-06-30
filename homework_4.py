# TODO: Enter a string of words separated by spaces. Find the longest word.

def find_longest_word(testString):
    sample_word = ""
    words_array = []
    testString = testString + " "

    for i in range(0, len(testString)):
        if testString[i] != ' ':
            sample_word = sample_word + testString[i]
        else:
            words_array.append(sample_word)
            sample_word = ""

    longest_word = words_array[0]
    print("all_words = {0}".format(words_array))

    # Find the longest word
    for el in range(0, len(words_array)):

        if len(longest_word) < len(words_array[el]):
            longest_word = words_array[el]
    print("The longest of all_words = {0}".format(longest_word))
    return longest_word


while True:
    string_entered = input(f"Please enter a test sentence to find the longest word: ")
    if string_entered == "" or not string_entered.isascii():
        print("Your input is not valid.Please check your input and try again.")
        break
    else:
        find_longest_word(string_entered)
        break

# TODO: Enter an irregular string and make the string regular.

def do_string_cleansing(string_sample):
    string_sample_after_split = string_sample.split()
    print(f'String after cleansing: ' + ' '.join(string_sample_after_split))


while True:
    string_sample = input("Please enter an irregular string to test the cleansing routine: ")
    if string_sample.isascii():
        do_string_cleansing(string_sample)
        break
    else:
        print("Invalid entry. Please try again.")