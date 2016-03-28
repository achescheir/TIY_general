from statistics import mean, median, mode, stdev, StatisticsError

def prompt(value_type):
    return input("Please input a {}. Blank line to end: ".format(value_type))

def string_length_stats(strings):
    lengths =[]
    for string in strings:
        lengths.append(len(string))
    return {'min':min(lengths),'max':max(lengths),'avg':(sum(lengths)/len(lengths))}

def character_counter(string):
    characters = {}
    for character in string:
        if character in characters:
            characters[character]+=1
        else:
            characters[character]=1
    return characters

def display_numbers(numbers):
    print(20*'=')
    print("You input {} numbers.".format(len(numbers)))
    print("The numbers sum to {:0.2f}.".format(sum(numbers)))
    if len(numbers)== 0:
        print("Average, mean, meadian, mode, and standard deviation are undefined for 0 numbers.")
    else:
        print("Their {} is {:0.2f}".format("average",sum(numbers)/len(numbers)))
        print("Their {} is {:0.2f}".format("mean",mean(numbers)))
        print("Their {} is {:0.2f}".format('median',median(numbers)))
        try:
            print("Their {} is {}".format('mode',mode(numbers)))
        except StatisticsError:
            print("This list has no mode.")
        print("Their {} is {:0.2f}".format('standard deviation',stdev(numbers)))

def display_strings(strings):
    print(20*'=')
    string_stats = string_length_stats(strings)
    all_together =''.join(strings)
    characters = character_counter(all_together)
    print(all_together)
    print("That was {} separate strings.".format(len(strings)))
    print("The shortest string was {} characters.".format(string_stats['min']))
    print("The longest string was {} characters.".format(string_stats['max']))
    print("The average string was {:0.2f} characters.".format(string_stats['avg']))
    if 'e' in characters:
        print("The letter 'e' was used {} times.".format(characters['e']))
    else:
        print("The letter 'e' was never used.")

def number_list(inputs):
    print("This will be a list of numbers.")
    while True:
        user_in = prompt("number")
        if user_in == "":
            break
        else:
            try:
                inputs.append(float(user_in))
            except ValueError:
                mixed = input("That was not a number. Do you want to change to a mixed list? [Y/n]")
                if mixed.lower().startswith('n'):
                    continue
                else:
                    inputs.append(user_in)
                    mixed_list(inputs)
                    return
    display_numbers(inputs)

def string_list(inputs):
    print("This will be a list of strings.")
    while(True):
        user_in = prompt("string")
        if user_in =="":
            break
        else:
            try:
                float(user_in)
            except ValueError:
                inputs.append(user_in)
            else:
                mixed = input("That was a number. Do you want to change to a mixed list? [Y/n]")
                if mixed.lower().startswith('n'):
                    continue
                else:
                    inputs.append(float(user_in))
                    mixed_list(inputs)
                    return
    display_strings(inputs)

def mixed_list(inputs):
    print("This is now a mixed list. Your previous entry in now in the list.")
    while(True):
        user_in = prompt("value")
        if user_in =="":
            break
        else:
            try:
                inputs.append(float(user_in))
            except ValueError:
                inputs.append(user_in)
    display_strings([x for x in inputs if type(x) is str])
    display_numbers([x for x in inputs if type(x) is not str])

inputs = []
first_in = prompt("value")
if first_in == "":
    pass
else:
    try:
        inputs.append(float(first_in))
    except ValueError:
        string_list([first_in])
    else:
        number_list(inputs)
print(20*'='+"\nGoodbye.")
