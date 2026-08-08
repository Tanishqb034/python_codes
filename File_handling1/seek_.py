with open("data.txt", "r") as file:

    print(file.read(5))

    file.seek(0)

    print(file.read(5))