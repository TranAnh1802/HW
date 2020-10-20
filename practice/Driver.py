CORRECT = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', \
            'A', 'D', 'C', 'B', 'B', 'D', 'A']

# Open the file containing the student's answers
stud_ans_file = open('student answers.txt', 'r')


# Fill a list with the student's answers
stud_ans = []
for line in stud_ans_file:
    stud_ans.append(line.rstrip('\n'))

# Check each student answer against the correct answers in CORRECT. Use the
# variable correct_solutions as an accumulator which will give the number of
# correct answers on the student's work.
correct_solutions = 0
for i in range(len(stud_ans)):
    if stud_ans[i] == CORRECT[i]:
        correct_solutions += 1

# Check if the student passed or not and display his/her score.
if correct_solutions >= 15:
    print('The student passed with a score of', correct_solutions, 'out of 20.')
else:
    print('The student failed with a score of', correct_solutions, 'out of 20.')

# Remember to close the file
stud_ans_file.close()
