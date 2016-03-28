# ask for input until blank line
# store input numbers
# output count, sum, avg of numbers
# handle non numerics
def number_list(inputs):
    print("This will be a list of numbers.")
    while True:
        user_in = input("Please input a number. Blank line to end: ")
        if user_in == "":
            break
        else:
            try:
                inputs.append(float(user_in))
            except ValueError:
                print("That was not a number.")
                continue
    print("You input {} numbers.".format(len(inputs)))
    print("The numbers sum to{}.".format(sum(inputs)))
    if len(inputs)== 0:
        print("Average is undefined for 0 numbers.")
    else:
        print("Their average is {}.".format(sum(inputs)/len(inputs)))

def string_list(inputs):
    print("This will be a list of strings.")
    while(True):
        user_in = input("Please input a value. Blank line to end:")
        if user_in =="":
            break
        else:
            inputs.append(user_in)
    print(''.join(inputs))


inputs = []
first_in = input("Please input a value. Blank line to end:")
if first_in == "":
    pass
else:
    try:
        inputs.append(float(first_in))
    except ValueError:
        string_list([first_in])
    else:
        number_list(inputs)
print("Goodbye.")
