line = """Stoi na stacji lokomotywa,
Ciezka, ogromna i pot z niej splywa:
Tlusta oliwa.
Stoi i sapie, dyszy i dmucha,
Zar z rozgrzanego jej brzucha bucha:
Buch - jak goraco!
Uch - jak goraco!
Puff - jak goraco!
Uff - jak goraco!
Już ledwo sapie, już ledwo zipie,
A jeszcze palacz wegiel w nią sypie."""

words = line.split()

start = words[:5]
end = words[-5:]


print("start: ", " ".join(start))
print("end: ", " ".join(end))