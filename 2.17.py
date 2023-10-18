line = "kot jedzenie pralka lizak"

words = line.split()

len = sorted(words, key=len)
alfabetical = sorted(words)

print(len, alfabetical)