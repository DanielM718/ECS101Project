from TextToBinary import get_binary
from BinaryToText import get_text

with open("text.txt", "r") as file:
    text = file.read()
get_binary(text)

with open("BinOutput.txt", "r") as bin:
    bintext = bin.read()
get_text(bintext)

with open("TextOutput.txt", "r") as unc:
    final = unc.read()

count = 0
if len(final) == len(text):
    for i in range(len(final)):
        if final[i] == text[i]:
            count += 1
    accuracy = (count / len(final)) * 100
    print("accuracy: ", accuracy, "%")
else:
    print("data loss, unable calculate accuracy")


ratio = 100-(len(bintext)/(len(text)*8))*100
print("compression ratio: ", ratio, "%")