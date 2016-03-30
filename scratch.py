import csv

def my_sum(number_list):
    sub_sum = 0

    for number in number_list:
        sub_sum += number

    return sub_sum

def multiples_of_3_or_5(number_list):
    return my_sum([x for x in number_list if(x % 3 == 0 or x % 5 ==0)])

def mults_alt(num_list):
    mults_list = []

    for number in num_list:
        if number % 3 == 0 or number % 5 == 0:
            mults_list.append(number)

    return my_sum(mults_list)

def fizz_buzz(num_list):
    for num in num_list:
        need_space = False
        if num % 3 == 0 or num % 5 == 0 :
            if num % 3 == 0:
                print("Fizz", end = '')
                need_space = True
            if num % 5 == 0:
                if need_space:
                    print(" ", end = '')
                print("Buzz", end = '')
            print("")
        else:
            print(num)

for max_len in [4,6]:
    with open('data.csv', 'r') as csv_in:
        header = ['Strategy','Secret','MaxLength','Rep','Win?','Length']
        reader = csv.reader(csv_in)
        next(reader)
        data_list_list = []
        data = {}
        print(max_len)
        for eachline in reader:
            if int(eachline[2]) != max_len:
                continue
            data_list_list.append([eachline[0],int(eachline[1]),int(eachline[4])])
        strats = ["SecretNumber","bozo","random","binary","binary+"]
        for each_strat in strats:
            print(each_strat)
            stratrates = []
            for each_secret in range(1,101):
                wins = 0
                for eachline in data_list_list:
                    if eachline[0]== each_strat and eachline[1] == each_secret:
                        wins += eachline[2]
                stratrates.append(wins)
            data[each_strat]=stratrates
        data["SecretNumber"]=range(1,101)
        with open('shorter{}.csv'.format(max_len),'w') as csv_out:
            writer = csv.writer(csv_out)
            strats = ["SecretNumber","bozo","random","binary","binary+"]
            writer.writerow(strats)
            for secret in range(100):
                writer.writerow([data["SecretNumber"][secret],data["bozo"][secret],data["random"][secret],data["binary"][secret],data["binary+"][secret]])
