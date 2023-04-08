# try:
#     file = open("file1.txt")
#     dict = {1: "Anshu"}
#     print(dict[1])
#
# except FileNotFoundError:
#     file = open("file1.txt", mode="w")
#     file.write("Something")
#
# except KeyError as errorMessage:
#     print(f"The key {errorMessage} doesn't exist")
#
# else:
#     contents = file.read()
#     print(contents)
#
# finally:
#     file.close()
#     print("file was closed")

"""raising exceptions"""
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

if height > 3:
    raise ValueError("Human height shouldn't be more than 3 meters")

bmi = weight / height ** 2
print(bmi)
