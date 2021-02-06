# import random guess file
import random

# generate a random no. between 1 to 100
randnum = random.randint(1, 101)


# print("random no . is " , randnum)


def printstar(ch, x):
    # s='#'
    print(ch * x)


def computerguess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        # guess is in the middle , it's found !
        if guess == randnum:
            return count
        # if "guess" is greater than the number ,
        # it must be found in the lower half of the set of the numbers
        # between the guess and the upper value
        elif guess > randnum:
            count = count + 1
            return computerguess(lowval, guess - 1, randnum, count)
        # the number must be in the upper set of the numbers
        # between the guess and the upper value
        else:
            count = count + 1
            return computerguess(guess + 1, highval, randnum, count)
    else:
        # number not found
        return -1


# end of function

# user guess
def user(randnum):
    count = 0  # to count the no. of guesses
    guess = -99  # declare intial guess

    while (guess != randnum):
        # get the user guess the number
        guess = (int)(input("enter your guess between 1 to 100:"))

        if guess < randnum:
            print("\nlower the guess than randnum\n ")
        elif guess > randnum:
            print("\nhigher the guess than randnum\n")
        else:
            printstar('*', 80)
            print("\n\tyou guess it !!! congro...Now do your work!!!\n ")
            break
        count = count + 1
    printstar('*', 80)
    print("\n\tyou took " + str(count) + " step to guess the numbers\n")
    printstar('*', 80)


def startup():
    printstar('_', 80)
    print('\n' + '*' * 7 + "\t\t  Welcome to Guess Game \t" + '*' * 7)
    printstar('_', 80)
    print('\n' + '*' * 7 + "\t\tpress 1 to continue the Game\t" + '*' * 7)
    printstar('_', 80)
    st = input("")
    print(st)
    if st == '1':
        printstar('_', 80)
        print('\n' + '\t' + '*' * 7 + "\t1.start game\t" + '*' * 7)
        print('\t' + '*' * 7 + "\t2.option \t" + '*' * 7)
        print('\t' + '*' * 7 + "\t3.about  \t" + '*' * 7)
        print('\t' + '*' * 7 + "\t4.exit   \t" + '*' * 7)
        i = input("")
        if i == '1':
            printstar('*', 80)
            user(randnum)
            print("\n\tcomputer took " + str(computerguess(0, 100, randnum)) + "\tsteps!!\n")
            printstar('*', 80)
        elif i == '2':
            printstar('*', 80)
            print("option not available")
        # continue
        elif i == '3':
            printstar('*', 80)
            print('-' * 7 + "Made by Mayur Pingale\ncopyright@2020" + '-' * 7)
        # continue
        else:
            printstar('*', 80)
    # exit


# print ("\nyou took " +str(count) +" step to guess the numbers")
# print("\n\ncomputer took " +str(computerguess(0,100,randnum))+"\tsteps!!")
#	printstar(10)
startup()
# user(randnum)
# print(str(computerguess(0,100,randnum)))


