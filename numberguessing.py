import random

def main():
    '''
    Input the bounds of the range of numbers and lets the user guess the omputer's number until the guess is correct
    '''
    smaller = int(input("Enter the lower Bound: "))
    larger = int(input("Enter the upper bound: "))
    compNumber = random.randint(smaller, larger)
    count = 0
    while True:
        count +=1
        userNumber = int(input("What's your guess? "))
        if userNumber < compNumber:
            print("Too small")
        elif userNumber>compNumber:
            print("Too large")
        else:
            print("You've got it in", count , "tries!")
            break


if __name__ == '__main__':
    main()