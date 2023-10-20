import pandas as pd

data = pd.read_csv("CompressionTable.csv", dtype=str, keep_default_na=False)
Characters = data["Characters"]
CB = data["Compressed Binary"]
TextToBin = dict(zip(Characters, CB))


def get_binary(p1: str):
    # print(TextToBin)
    p2 = ""
    for character in p1:
        if "\n" == character:
            p2 += "0110100"
        else:
            try:
                p2 += TextToBin[character]
            except KeyError as error:
                p2 += "0110101"
    with open("BinOutput.txt", "w") as bin:
        bin.write(str(len(p2)) + "." + p2)
    pass


with open("text.txt", "r") as file:
    text = file.read()

get_binary(text)
