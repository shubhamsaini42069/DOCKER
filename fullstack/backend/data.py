def getdata():
    with open("name.txt", "r") as f:
        lines = f.read().splitlines()
    return lines
