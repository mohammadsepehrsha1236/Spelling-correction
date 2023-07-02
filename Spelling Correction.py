from textblob import TextBlob
a = input("Please Enter Number :")
b = len(a)
for l in range(b):
    inputt = input("")
    words = []
    words.append(inputt)
    corrected_words = []
    for i in words:
        corrected_words.append(TextBlob(i))
    print("Wrong words :", words)
    print("Corrected Words are :")
    for i in corrected_words:
        print(i.correct(), end=" ")