import string
def check_string(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False


def score_word(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            words = line.split(" ")
            for word in words:
                if word.upper().lower() == string_to_search:
                    list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results


def average_core(file_name):
    with open(file_name,'r') as read_obj:
        text = read_obj.read()
        words = text.split()
        #normalize all and strip all punctuation
        table = str.maketrans("","",string.punctuation)
        stripped = [w.translate(table) for w in words]
        assemble = " ".join(stripped)
        assemble = assemble.lower()
        print(assemble)

def main():
    print("What would you like to do ?")
    print("1: Get score of a word?")
    print("2: Get the average score of words in a file ")
    print("3: Find the highest / lowest scoring words in a file")
    print("4: Sort the words into positive.txt and negative.txt")
    print("5: Exit the program")
    word = input("enter a word to get score's word ?")
    if check_string('training.txt', word):
        print('Yes, word found in file')
    else:
        print('Word not found in file')
    matched_lines = score_word('training.txt', word)
    s =0
    score = 0
    for elem in matched_lines:
        s += int(elem[1][0])
    score = round(s/(len(matched_lines)), 2)
    print("score: ", score)
    if score > 2:
        print(word," is positive")
    else:
        print(word," is negative")
#function2:
#normalize and strip punctuation
    # normalize = average_core('training.txt')
    # print(normalize)


if __name__ == '__main__':
    main()