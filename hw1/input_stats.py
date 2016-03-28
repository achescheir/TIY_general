# ask for input until blank line
# store input numbers
# output count, sum, avg of numbers
# handle non numerics
from statistics import mean, median, mode, stdev, StatisticsError

def min_max_avg_string(strings):
    lengths =[]
    for string in strings:
        lengths.append(len(string))
    return (min(lengths),max(lengths),(sum(lengths)/len(lengths)))

def character_counter(string):
    characters = {}
    for character in string:
        if character in characters:
            characters[character]+=1
        else:
            characters[character]=1
    return characters

def display_numbers(numbers):
    print("You input {} numbers.".format(len(numbers)))
    print("The numbers sum to {}.".format(sum(numbers)))
    if len(numbers)== 0:
        print("Average, mean, meadian, mode, and standard deviation are undefined for 0 numbers.")
    else:
        print("Their {} is {}.".format("average",sum(numbers)/len(numbers)))
        print("Their {} is {}.".format("mean",mean(numbers)))
        print("Their {} is {}.".format('median',median(numbers)))
        try:
            print("Their {} is {}.".format('mode',mode(numbers)))
        except StatisticsError:
            print("This list has no mode.")
        print("Their {} is {}.".format('standard deviation',stdev(numbers)))


def display_strings(strings):
    string_min,string_max,string_avg = min_max_avg_string(strings)
    all_together =''.join(strings)
    characters = character_counter(all_together)
    print(all_together)
    print("That was {} separate strings.".format(len(strings)))
    print("The shortest string was {} characters.".format(string_min))
    print("The longest string was {} characters.".format(string_max))
    print("The average string was {} character.".format(string_avg))
    if 'e' in characters:
        print("The letter 'e' was used {} times.".format(characters['e']))
    else:
        print("The letter 'e' was never used.")

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
    display_numbers(inputs)

def string_list(inputs):
    print("This will be a list of strings.")
    while(True):
        user_in = input("Please input a value. Blank line to end:")
        if user_in =="":
            break
        else:
            inputs.append(user_in)
    display_strings(inputs)


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
