def most_frequent_char(str):
    dict = {}

    max_repeat_count = 0

    for letter in str:

        if letter not in dict:

            dict[letter] = 1

        else:

            dict[letter] += 1

        if dict[letter] > max_repeat_count:
            max_repeat_count = dict[letter]

            most_repeated_char = letter

    return most_repeated_char


if __name__ == '__main__':
    strg = input("Enter the string : ")

    print("Most Frequent Character : " + most_frequent_char(strg))