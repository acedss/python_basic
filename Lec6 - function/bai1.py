sentence = str(input("Enter a sentence: "))
saveTimesKey = {}
for frequency in sentence:
    if frequency != "":
        if frequency in saveTimesKey:
            saveTimesKey[frequency] += 1
        else:
            saveTimesKey[frequency] = 1
print(saveTimesKey)
