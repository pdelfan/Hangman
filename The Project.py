def read_string_list_from_file(the_file):    
    fileRef = open("list_of_formulas.txt","r") # opening file to be read
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)  # adds string to list
        
    fileRef.close()  
 
    return localList

#For the number of guesses. 

def max_number_guess(max_guess):
    while max_guess.isdigit() == False or max_guess == 0:
        print "Please type a number."
        max_guess = raw_input("Maximum wrong-guesses you want to have allowed?")
    
    return max_guess

def guess_validator():
    print "You can use digits 0 to 9 and symbols + *"
    symbol = raw_input("Please enter an operation symbol or digit:")
    while len(symbol) > 1 or symbol not in ["+", "*", "0", "1","2", "3", "4", "5", "6", "7", "8", "9"]:
        print "That is not a symbol, digit or too many characters."
        symbol = raw_input("Please enter an operation symbol or digit:")

    return symbol

def guess_update(random_fmla, partial_fmla, symbol):
    answer = ""
    if symbol not in random_fmla or symbol in partial_fmla:
        answer = partial_fmla
    else:
        if symbol in random_fmla and symbol not in partial_fmla:
            for i in range(len(random_fmla)):
                if symbol == random_fmla[i]:
                    answer += random_fmla[i]
                else:
                    answer += partial_fmla[i]

    print answer
    return answer, partial_fmla

def lucky_num1(random_fmla):
    lucky_number1 = ""
    for i in range(2, len(random_fmla)):
        if int(random_fmla[i]) % 2 == 0:
            lucky_number1 += "0"
        else:
            lucky_number1 += "1"

    print list(int(lucky_number1))

def convert_bin_list_to_dec(lucky_num1):
    newstring = ""
    answer = str(lucky_num1)[1:-1]
    for i in range(len(answer)):
        if answer[i].isdigit():
            newstring += answer[i]
        else:
            newstring += ""

    print int(newstring, 2)
            


        
listStrings= read_string_list_from_file("list_of_formulas.txt")

import random
random_fmla = (random.choice(listStrings)) #chooses a formula randomly
print random_fmla

attempts = 0

partial_fmla = len(random_fmla)*"-"
# to call the function use listStrings
max_guess = raw_input("Maximum wrong-guesses you want to have allowed?")
max_number_guess(max_guess)


'''
while attempts < max_guess or partial_fmla == random_fmla:
    symbol = guess_validator()
    guess_update(random_fmla, partial_fmla, symbol)
    attempts += 1
'''

lucky_num1(random_fmla)
convert_bin_list_to_dec(lucky_num1)
