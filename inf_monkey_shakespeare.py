# Connor Wilson
# The infinite time monkey typing out shakespeare attempt
# - Using Newton-Raphson method, our program will try to converge on a single line of shakespeare
# newguess = 0.5 * (oldguess + (n/oldguess) where n is initial number
# initial guess is usually n/2 for a sqrt() approx

import random



def str_rand_generate(length):
    '''
    Purpose : creates a randomly generated str of len 'length'
    Input : int
    Output : str (lowercase ch + space)
    '''

    # create lowercase lst with space in it
    lowerc_lst = [" "]
    for ch in range(97,123):
        lowerc_lst.append(chr(ch))
    #print(lowerc_lst)
    #print(len(lowerc_lst))

    my_str = ''
    for index in range(length):
        my_str = my_str + lowerc_lst[random.randint(0, 26)]
    #print(my_str)
    return my_str

def str_percision(guess, target):
    '''
    Purpose : provides likeness score between guess and target str
    input : str str
    output : float
    '''

    correct_ch = 0

    if len(guess) == 0 or len(target) == 0:
        return 100

    for index in range(len(target)):
        if guess[index] == target[index]:
            correct_ch += 1

    percent = (correct_ch / len(target)) * 100
    #print(f'{percent:3.0f}')
    #percent = round(percent, 0)
    return percent

def str_rand_eval(target):
    '''
    Purpose : Call random gen for new string until it 100% matches the target string, outputting the # of tries
    Input : str
    Output : int
    '''
    attempts = 0
    percentage = 0
    while percentage < 100:
        guess_str = str_rand_generate(len(target))
        percentage = str_percision(guess_str, target)
        if percentage == 100:
            print(f'Rand sucessful after {attempts} attempts for {target}')
        elif attempts % 1000000 == 0 and attempts != 0:
            print(f'Rand number of tries = {attempts} at str : {guess_str}')

        attempts += 1

    return attempts




def str_singlechr_swap(input_str):
    '''
    Purpose : randomly change one chr in the str
    Input : str
    Output : str
    '''

    # create lowercase lst with space in it
    lowerc_lst = [" "]
    for ch in range(97,123):
        lowerc_lst.append(chr(ch))

    my_str = ''
    rand_chr = lowerc_lst[random.randint(0, 26)]
    rand_index = random.randint(0, len(input_str))
    if len(input_str) == 0:
        my_str = ''
    elif len(input_str) == 1:
        my_str = rand_chr
    else:
        my_str = input_str[0:rand_index] + rand_chr + input_str[rand_index+1:len(input_str)]

    #print(my_str)
    return my_str

def str_climbing_eval(target):
    '''
    Purpose : Start with new rand str, use 'hill climbing' algo to until it 100% matches the target string, outputting the # of tries
    Input : str
    Output : int
    '''
    attempts = 0
    percentage = 0
    guess_str = str_rand_generate(len(target)) # initial guess

    while percentage < 100:
        percentage = str_percision(guess_str, target) # calc percentage
        alt_str = str_singlechr_swap(guess_str) # generate new str option by changing one chr
        alt_percentage = str_percision(alt_str, target)# calc new option percentage
        if alt_percentage > percentage:
            guess_str = alt_str

        if percentage == 100:
            print(f'Climbing sucess after {attempts} attempts for {target}')
        elif attempts % 1000 == 0 and attempts != 0:
            print(f'Number of climbing tries = {attempts} at str : {guess_str}')

        attempts += 1

    return attempts


# Testing
str_rand_eval('e')
str_climbing_eval('e')
str_rand_eval('ag')
str_climbing_eval('ag')
str_rand_eval(' ')
str_climbing_eval(' ')
str_rand_eval('ve')
str_climbing_eval('ve')
str_rand_eval('eee')
str_climbing_eval('eee')
#str_rand_eval('methinks')
str_climbing_eval('methinks')
str_climbing_eval('methinks it is like a weasel')

input('hold up bro')







#target = 'methinks it is like a weasel'
