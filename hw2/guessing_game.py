import random

def get_guess():
    try:
        return(int(input("What's your guess? ")))
    except ValueError:
        print("That's not a whole number.")
        return(get_guess())


def is_winner(guesses, my_number):
    return guesses[-1] == my_number


def display_end_game(guesses, my_number):
    print("My number was {}.".format(my_number))
    if is_winner(guesses,my_number):
        print("You won ", end = '')
    else:
        print("You lost ", end = '')
    print("after {} turns.".format(len(guesses),my_number))


def is_close(this_guess,my_number,close):
    return (abs(this_guess - my_number) < close)


def eval_guess(this_guess,my_number):
    if this_guess > my_number:
        print("Sorry that was too high.")
    elif this_guess < my_number:
        print("Sorry that was too low.")
    elif this_guess == my_number:
        return True
    else:
        raise ValueError("{} not higher lower or equal to {}".format(this_guess,my_number))
    return False

def is_good_guess(this_guess, in_guesses, my_number):
    guesses = in_guesses[:]
    guesses.extend([0,101])
    lower_bound = max([x for x in guesses if x < my_number])
    upper_bound = min([x for x in guesses if x > my_number])
    if this_guess > lower_bound and this_guess < upper_bound:
        return True
    else:
        return False

def handle_guess(guesses, my_number, close = 0, critique = False):
    this_guess = get_guess()

    if this_guess in guesses:
        print("You already guessed that.")
    guesses.append(this_guess)
    should_break = eval_guess(this_guess,my_number)
    if is_close(this_guess, my_number, close):
        print("But it's close!")
    if critique and not is_good_guess(this_guess, guesses[:-1], my_number):
        print("You should have known better.")
    return(should_break)


def normal_game(game_length):
    my_number = random.randint(1,100)
    guesses = []

    while len(guesses) < game_length:
        if handle_guess(guesses,my_number):
            break
    display_end_game(guesses,my_number)


def advanced_game(game_length):
        my_number = random.choice(range(1,101))
        guesses = []

        while len(guesses) < game_length:
            if handle_guess(guesses, my_number, 5, True):
                break
        display_end_game(guesses,my_number)

def guard_strategy(strategy):
    if not any([strategy.lower() == x for x in ["random","binary","binary+"]]):
        raise ValueError('{} is not a valid strategy.'.format(strategy))

def binary_guess(lower_bound, upper_bound):
    return(int((lower_bound + upper_bound)/2))

def random_guess(lower_bound, upper_bound):
    return(random.randint(lower_bound, upper_bound))

def make_guess(strategy, guesses, game_length, lower_bound, upper_bound):
    if strategy.lower() == 'binary':
        return binary_guess(lower_bound, upper_bound)
    elif strategy.lower() == 'random':
        return random_guess(lower_bound, upper_bound)
    elif strategy.lower() == 'binary+':
        if len(guesses) < game_length-1:
            return binary_guess(lower_bound, upper_bound)
        else:
            return random_guess(lower_bound, upper_bound)

def get_approved_input(my_guess):
    shorter_user_answer = 'not in HLC'
    while shorter_user_answer not in 'HLC':
        user_answer = input(str(my_guess)+'? ')
        if user_answer:
            shorter_user_answer = user_answer.upper()[0]
    return shorter_user_answer

def handle_user_input(my_guess, lower_bound, upper_bound):
    shorter_user_answer = get_approved_input(my_guess)
    if shorter_user_answer == "H":
        upper_bound = my_guess - 1
    elif shorter_user_answer == "L":
        lower_bound = my_guess + 1
    elif shorter_user_answer == "C":
        i_won = True
    else:
        raise ValueError("Something happened to shorter_user_answer." +
            "It should be H, L, or C. It is {} instead.".format(shorter_user_answer))
    if upper_bound < lower_bound:
        print("You lied to me.")
        user_lied = True
    return(lower_bound, upper_bound)

def computer_guesses_game(game_length, lower_bound = 1, upper_bound = 100, strategy = 'random'):
    guard_strategy(strategy)
    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)
    i_won = False
    user_lied = False
    guesses = []

    print("I'll guess {} to {}. Respond if my guess is too (H)igh, too (L)ow, or (C)orrect.".format(lower_bound, upper_bound))
    while len(guesses) < game_length:
        my_guess = make_guess(strategy, guesses, game_length, lower_bound, upper_bound)
        guesses.append(my_guess)
        lower_bound, upper_bound = handle_user_input(my_guess, lower_bound, upper_bound)
        if i_won or user_lied:
            break

    if i_won:
        print("I won")
    elif user_lied:
        print("Liar.")
    else:
        print("I lost")

def epic_game(game_length):
    computer_guesses_game(game_length)

def impossible_game(game_length):
    computer_guesses_game(game_length,strategy='binary+')

impossible_game(5)
