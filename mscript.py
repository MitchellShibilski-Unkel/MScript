import numpy as np

def read(file: str):
    if file.endswith(".mscript"):
        pass
    else:
        raise "INCORRECT FILE TYPE ERROR :: Should be *.mscript"
        
    with open(file, "r") as f:
        data = f.read()

    return data

def mscrToPy(fileName: str):
    file = read(fileName)

    mprint = file.replace("println(", "print(")
    mprint2 = mprint.replace('")', '\\n")')

    python = mprint2.replace("func", "def").replace("&", "and").replace("|", "or").replace("switch", "match").replace("enum", "enumerate").replace("true", "True").replace("false", "False")

    with open("exe.py", "w") as i:
        i.write(str(python))
