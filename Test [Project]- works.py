"CMPT 120 | Group members: Pouria Delfanazari, Josh Vocal | Version 1.0 | Time spent (total): 20"

"-----------------------------------------------------------------------------------------------------------------------------------"


"Reads the file with the list of formulas from the string."

def read_string_list_from_file(the_file):    
    fileRef = open("fmla.txt","r") # opening file to be read
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line                                    
        localList.append(string)  # adds string to list
    fileRef.close()  
    return localList


"Returns the the maximun number of wrong guesses allowed."

def max_number_guess(max_guess):    
    while max_guess.isdigit()== False or max_guess == "0":
        print "Please type a number:"
        max_guess = raw_input("Maximum wrong-guesses you want to have allowed?")
        print
    return int(max_guess)


"Returns the guess the user makes. If it is anything other than digits and symbols, it asks again."

def guess_validator():
    print "\nYou can use digits 0 to 9 and symbols + *"
    print
    symbol = raw_input("Please enter an operation symbol or digit:")
    while len(symbol) > 1 or symbol not in ["+", "*", "0", "1","2", "3", "4", "5", "6", "7", "8", "9"]:
        print "That is not a symbol, digit or too many characters."
        symbol = raw_input("Please enter an operation symbol or digit:")
        print
    return symbol

global partial_fmla
answer= ""


"Puts the correctly guessed characters into the partial_fmla (The formula with the correctly guessed characters inside) and returns it."

def guess_update(random_fmla, partial_fmla, symbol):
    answer = ""
    #if symbol not in random_fmla or symbol in partial_fmla: #symbol is the guess |  partial_fmla is ----------
    if symbol in random_fmla:
        for i in range(len(random_fmla)):
            if symbol == random_fmla[i]:
                answer += random_fmla[i]
            else:
                answer += partial_fmla[i]
    else:
        answer = partial_fmla
    print "\nThe formula you have guessed so far is: ", answer
    return answer


"Calculates the first lucky number."

def lucky_num1(random_fmla):
    lucky_number1 = ""
    for i in range(2, len(random_fmla)):
        if int(random_fmla[i]) % 2 == 0:
            lucky_number1 += "0"
        else:
            lucky_number1 += "1"
    return int(lucky_number1, 2)


"Calculates the second lucky number."

def lucky_num2(random_fmla):
    newstring = ""
    newList = []
    for i in range(2, len(random_fmla)):
        newstring += random_fmla[i] + "+"
    newstring =  newstring[0:len(newstring)-1]
    "print newstring" # Creates a new string with + between the numbers
    i = 0
    while i < len(newstring):
        test =  newstring[i:len(newstring)]
        i += 2
        newList.append(test)
        "print  newList" #Slices the string and creates a new element for every digit.
    for i in range(len(newList)):
        newList[i] = eval(newList[i])
        "print newList" #Evaluates the expression for each element in the list
    i = 0
    add_list = 0
    for i in range(len(newList)):
        add_list += newList[i]
        "print add_list" #Adds the total sum of the list
    return add_list


"Asks the user whether he wants to play. If the user types anything other than y or n (both lowercase and uppercase), it will ask again."

def play_update(want_play):
    while len(want_play) > 1 or want_play not in ["Y", "y", "N", "n"]:
        print "Please answer correctly."
        want_play = raw_input("Do you want to play? Yes = y No = n: ")
    return want_play


"Expands (alternates) the formula."

def expanded_formula(random_fmla):
    n= 2
    expanded= ''
    for i in range(2, len(random_fmla)):
        if n%2==0:
            expanded= expanded + random_fmla[i] + random_fmla[0]
            n= n +1
        else:
            expanded= expanded + random_fmla[i] + random_fmla[1]
            n= n+1
    expand= (expanded[0:len(expanded)-1])
    return expand


"Evaluates the expanded formula so that the user can guess."

def eval_expanded_formula(random_fmla):
    tmp = list(random_fmla)
    calculated_num = int(tmp[2])
    for i in range(3, len(random_fmla)):
        operator = ''
        if i%2 == 1:
            operator = tmp[0]
        else:
            operator = tmp[1]

        if operator == '+':
            calculated_num += int(random_fmla[i])
        else:
            calculated_num *= int(random_fmla[i])

    return calculated_num

        
###########################################################

#Top level

        
listStrings= read_string_list_from_file("list_of_formulas.txt")
import random
random_fmla = (random.choice(listStrings)) #chooses a formula randomly
global points
points = random.randint(3,6)
wrong_guess = 0
history_of_guesses = []
partial_fmla = len(random_fmla)*"-"
print 

global want_play

want_play = raw_input("Do you want to play? Yes = y No = n: ")
want_play = play_update(want_play)
game_number = 1
print

while points > 2 and want_play in ["Y", "y"]:
    print "Playing game #: ", game_number
    print "\nYou points so far are: ", points
    print "\n-----------------------------------------------"
    print "\nrandom formula:%s\n\n" % random_fmla
    max_guess = raw_input("Maximum wrong-guesses you want to have allowed? ")
    max_guess = max_number_guess(max_guess)
    print
    print "The formula you will have to guess has", len(random_fmla) ,"symbols: ", partial_fmla
    print
    while wrong_guess < max_guess and partial_fmla != random_fmla and points > 2:
        symbol= guess_validator()
        if symbol in random_fmla:
            partial_fmla = guess_update(random_fmla, partial_fmla, symbol)
        else:
            wrong_guess += 1
            history_of_guesses.append(symbol)
        
        print '\nNumber of allowable attempts left:', max_guess-wrong_guess
        print 'Number of wrong guesses made:', wrong_guess

    if partial_fmla == random_fmla:
        print "\n##You have correctly guessed the formula!##", partial_fmla
        print "\nYou have won 2 points"
        points += 2
        print "Your total points is now: ", points
        print "\nExpanded formula:", expanded_formula(random_fmla)
        exp_calc= input("\nCalculate the expanded formula:")
        result = eval_expanded_formula(random_fmla)
        if int(exp_calc)== result:
            print "\nYou won!"
            points += 10
            print "\nYou points so far are: ", points
        else:
            print "\nWrong, game over"
            points -= 2
            print "\nPoints:", points
            print "\nYour first lucky number is: ", lucky_num1(random_fmla)
            print "\nYour second lucky number is: ", lucky_num2(random_fmla)
            history_of_guesses.append(exp_calc)
            print "\nThis is the history of your wrong guesses.", history_of_guesses
            
        print "\nThe result is:" , result ########## need to hide from the user
        print
        
    else:
        print "\nYou have lost 2 points!"
        points += -2
        print "\nYour total points is now: ", points
        print "\nThis is the history of your wrong guesses.", history_of_guesses
        print "\nYour first lucky number is: ", lucky_num1(random_fmla)
        print "\nYour second lucky number is: ", lucky_num2(random_fmla)
        print "\nGame over."
        
        
    want_play = raw_input("Do you want to play? Yes = y No = n: ")
    want_play = play_update(want_play)
    random_fmla = (random.choice(listStrings))
    partial_fmla = len(random_fmla)*"-"
    wrong_guess = 0
    i = 0
    game_number += 1
    print
