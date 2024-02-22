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

#look up value
multiply = my_dict[to_do] #check for double or half

#calculations
answer = your_num * multiply #input x dictionary value
print(f"{your_num} * {multiply} = {answer}")