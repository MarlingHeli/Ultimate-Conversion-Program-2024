#key : value

my_dict = {
    "blue" : "sky",
    "green" : "grass",
    "yelloe" : "sun",
    "red" : "apple",
}

#user has to search for key and not value. dictionary only searches for key
to_find = input("What are you looking for? ")

    #check if input is in dictionary
if to_find in my_dict:
    print(f"{to_find} is in the dictionary!")

    #get value
    coloured_object = my_dict[to_find]
    print(f"The {coloured_object} is {to_find}")

#if we want to search for values
elif to_find in my_dict.values():
    print(f"{to_find} is a value in the dictionary")

else:
    print("Sorry - item not found")
