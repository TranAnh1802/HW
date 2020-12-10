def main():
    string = input('Enter a string for the program to capitalize sentences: ')
    result = capitalize(string)

    print(result)

# The capitalize method return a opy of the string
# with the first character of each sentence capitalized.
def capitalize(string):
    result = ''
    new_sentence = True
    result_word = ''

    words = string.split()

    for item in words:
        if new_sentence:
            result_word = item[0].upper() + item[1:]
        else:
            result_word = item

        result += result_word + ' '

        if item[-1] == '.' or item[-1] == '?' or item[-1] == '!':
            new_sentence = True
        else:
            new_sentence = False

    return result

main()