number = 112304095094095

word = str(number)

counter = 0
for digit in word:
    if digit == "0":
        counter += 1

print(counter)
