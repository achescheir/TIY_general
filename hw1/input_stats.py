# ask for input until blank line
# store input numbers
# output count, sum, avg of numbers
# handle non numerics
numbers = []
while True:
    user_in = input("Please input a number. Blank line to end: ")
    if user_in == "":
        break
    else:
        try:
            numbers.append(float(user_in))
        except ValueError:
            print("That was not a number.")
            continue
print("You input {} numbers.".format(len(numbers)))
print("The numbers sum to{}.".format(sum(numbers)))
print("Ther average is {}".format(sum(numbers)/len(numbers)))
