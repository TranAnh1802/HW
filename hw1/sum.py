
print("enter a series of digit with nothing separate: ")
series = list(map(int, input()))
sum = 0
for i in series:
    sum += i
 print("the sum of the digits in: ", series, "is", sum)