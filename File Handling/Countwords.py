f = open("abc.txt", "r")
data = f.read()
words = data.split()

print("Number of words in text file :", len(words))
