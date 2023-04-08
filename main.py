try:
    file = open("file1.txt")
    dict = {1: "Anshu"}
    print(dict[1])

except FileNotFoundError:
    file = open("file1.txt", mode="w")
    file.write("Something")

except KeyError as errorMessage:
    print(f"The key {errorMessage} doesn't exist")

else:
    contents = file.read()
    print(contents)

finally:
    file.close()
    print("file was closed")