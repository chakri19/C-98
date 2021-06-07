def swapFileData():
    fileName = input("Enter file name:")
    fileName2 = input("Enter second file name:")

    with open(fileName, "r") as a:
        data_a = a.read()
    with open(fileName2, "r") as b:
        data_b = b.read()

    with open(fileName, "w") as a:
        a.write(data_b)
    
    with open(fileName2, "w") as b:
        b.write(data_a)

swapFileData()