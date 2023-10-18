line = "jedzenie kot monitor oko"

line = line.split()

longest_word = max(line, key=len)
print("najdłuższy wyraz to: '", longest_word, "' i ma: ", len(longest_word), " liter")
