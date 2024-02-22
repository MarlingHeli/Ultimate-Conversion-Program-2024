my_dict = {
    "blue" : "sky",
    "double" : 2,
    "half" : 0.5,
    "green" : "grass",
    "yellow" : "sun",
    "red" : "apple"
}

#can use dictionary to do some math
your_num = int(input("Enter a number: "))
to_do = input("double or half? ").lower()

if to_do == "double":
    #look up value
    multiply = my_dict[to_do] #get value based on key

    #calculations
    answer = your_num * multiply #input x 2
    print(f"{your_num} * {multiply} = {answer}")

elif to_do == "half":
    divide = my_dict[to_do]
    answer = your_num * divide #input x 0.5
    print(f"{your_num} * {divide} = {answer}")

else:
    print("Please select double or half.")
