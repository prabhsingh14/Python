available_sizes = ["small", "medium", "large"]

if(requested_size := input("What size do you want? ")) in available_sizes:
    print(f"Here is your {requested_size} coffee")
else:
    print(f"Sorry, we don't have {requested_size} size")