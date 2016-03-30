import random

# I got the ordinal function from: http://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers
# I would probably not have thought to use the .get and would have filled in the SUFFIXES dictionary
# but otherwise the code seems straight forward
# comments were in the source
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme.
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        # the second parameter is a default.
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix

def guard_strategy(strategy):
    if not any([strategy.lower() == x for x in ["random","binary","binary+"]]):
        raise ValueError('{} is not a valid strategy.'.format(strategy))

def binary_guess(bounds):
    return(int((bounds['lower'] + bounds['upper'])/2))

def random_guess(bounds):
    return(random.randint(bounds['lower'], bounds['upper']))

def make_guess(strategy, guesses, game_length, bounds):
    if strategy.lower() == 'binary':
        return binary_guess(bounds)
    elif strategy.lower() == 'random':
        return random_guess(bounds)
    elif strategy.lower() == 'binary+':
        if len(guesses) < game_length-1:
            return binary_guess(bounds)
        else:
            return random_guess(bounds)

def get_approved_input(my_guess,ok_answers, number_of_guess):
    shorter_user_answer = 'not in '+ ok_answers
    while shorter_user_answer not in ok_answers:
        user_answer = input(ordinal(number_of_guess) + " guess: " + str(my_guess)+'? ')
        if user_answer:
            shorter_user_answer = user_answer.upper()[0]
    return shorter_user_answer

def handle_user_input(my_guess, bounds, number_of_guess):
    shorter_user_answer = get_approved_input(my_guess,"HLC", number_of_guess)
    if shorter_user_answer == "H":
        bounds['upper'] = my_guess - 1
    elif shorter_user_answer == "L":
        bounds['lower'] = my_guess + 1
    elif shorter_user_answer == "C":
        return 'win'
    else:
        raise ValueError("Something happened to shorter_user_answer." +
            "It should be H, L, or C. It is '{}' instead.".format(shorter_user_answer))
    if bounds['upper'] < bounds['lower']:
        print("You lied to me.")
        return 'lie'
    return 'continue'

def computer_guesses_game(game_length, lower_bound = 1, upper_bound = 100, strategy = 'random'):
    guard_strategy(strategy)
    bounds = {'lower':int(lower_bound), 'upper': int(upper_bound)}
    guesses = []

    print("I'll guess {} to {}. Respond if my guess is too (H)igh, too (L)ow, or (C)orrect.".format(lower_bound, upper_bound))
    while len(guesses) < game_length:
        my_guess = make_guess(strategy, guesses, game_length, bounds)
        guesses.append(my_guess)
        game_status = handle_user_input(my_guess, bounds, len(guesses))
        if game_status != "continue":
            break

    if game_status == 'win':
        print("I won.")
    elif game_status == 'lie':
        print("Liar.")
    else:
        print("I lost.")

def epic_game(game_length):
    computer_guesses_game(game_length)

def impossible_game(game_length):
    computer_guesses_game(game_length,strategy='binary+')

impossible_game(5)

# def get_guess(number_of_guess):
#     try:
#         return(int(input("What's your {} guess? ".format(ordinal(number_of_guess)))))
#     except ValueError:
#         print("That's not a whole number.")
#         return(get_guess(number_of_guess))
#
#
# def is_winner(guesses, my_number):
#     return guesses[-1] == my_number
#
#
# def display_end_game(guesses, my_number):
#     print("My number was {}.".format(my_number))
#     if is_winner(guesses,my_number):
#         print("You won ", end = '')
#     else:
#         print("You lost ", end = '')
#     print("after {} turns.".format(len(guesses),my_number))
#
#
# def is_close(this_guess,my_number,close):
#     return (abs(this_guess - my_number) < close)
#
#
# def eval_guess(this_guess,my_number):
#     if this_guess > my_number:
#         print("Sorry that was too high.")
#     elif this_guess < my_number:
#         print("Sorry that was too low.")
#     elif this_guess == my_number:
#         return True
#     else:
#         raise ValueError("{} not higher lower or equal to {}".format(this_guess,my_number))
#     return False
#
# def is_good_guess(this_guess, in_guesses, my_number):
#     guesses = in_guesses[:]
#     guesses.extend([0,101])
#     lower_bound = max([x for x in guesses if x < my_number])
#     upper_bound = min([x for x in guesses if x > my_number])
#     if this_guess > lower_bound and this_guess < upper_bound:
#         return True
#     else:
#         return False
#
# def handle_guess(guesses, my_number, close = 0, critique = False):
#     this_guess = get_guess(len(guesses)+1)
# # I could join get_guess() and this in a loop instead of using up a guess but I like it this way
#     if this_guess in guesses:
#         print("You already guessed that. Do try to keep up next time.")
#     guesses.append(this_guess)
#     if eval_guess(this_guess,my_number):
#         return True
#     if is_close(this_guess, my_number, close):
#         print("But it's close!")
#     if critique and not is_good_guess(this_guess, guesses[:-1], my_number):
#         print("You should have known better.")
#     return False
#
#
# def normal_game(game_length,lower_bound = 1, upper_bound = 100):
#     my_number = random.randint(lower_bound,upper_bound)
#     guesses = []
#     print("Welcome to number guesser!")
#     print("You will have {} chances to find my number {} to {}.".format(game_length, lower_bound, upper_bound))
#     print("Good luck!")
#     while len(guesses) < game_length:
#         if handle_guess(guesses,my_number):
#             break
#     display_end_game(guesses,my_number)
#
#
# def advanced_game(game_length,lower_bound = 1, upper_bound = 100):
#     my_number = random.choice(range(lower_bound,upper_bound+1))
#     guesses = []
#     print("Welcome to number guesser!")
#     print("You will have {} chances to find my number {} to {}.".format(game_length, lower_bound, upper_bound))
#     print("Good luck!")
#     while len(guesses) < game_length:
#         if handle_guess(guesses, my_number, 5, True):
#             break
#     display_end_game(guesses,my_number)
#
# advanced_game(5)
