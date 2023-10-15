import pandas as pd

data = pd.read_csv("CompressionTable.csv", dtype=str, keep_default_na=False)
Characters = data["Characters"]
CB = data["Compressed Binary"]
BinToText = dict(zip(CB, Characters))

def get_text(p1: str):
    p2 = ""
    buffer = 0
    for item in range(len(p1)):
        if buffer != 0:
            buffer -= 1
            continue
        if p1[item] == "1":
            p2 += BinToText[p1[item:item+4]]
            buffer += 3
        elif p1[item] == "0":
            if "0110100" == p1[item:item+7]:
                p2 += "\n"
            else:
                p2 += BinToText[p1[item:item+7]]
            buffer += 6

    with open("uncompressed.txt", "w") as unc:
        unc.write(p2)
    pass


with open("binary.txt", "r") as file:
    text = file.read()

get_text(text)

