import string
def print_menu():
    print(" 1) Check a palindrome")
    print(" 2) Check a word square")
    print(" 3) Quit")

def get_menu_choice():
    choice = -1
    while choice >3 or choice <1:
        choice = int(input("Choose a function:"))
    return choice

def get_phrase():
    phrase = str(input("Enter a phrase:"))
    while len(phrase) < 1:
        phrase = str(input("Enter a phrase:"))
    return phrase

def is_palindrome(phrase):
    remove_punctuation = "".join(i.lower() for i in phrase if i in string.ascii_letters)
    if remove_punctuation == remove_punctuation[::-1]:
        return True
    elif remove_punctuation != remove_punctuation[::-1]:
        return False


def menu_check_palindrome():
    phrase = get_phrase()
    is_it_palindrome = is_palindrome(phrase)
    if is_it_palindrome == True:
        print(phrase, "is a palindrome!")
    if is_it_palindrome == False:
        print(phrase, "is not a palindrome")

def get_word_square():
    word = str(input("Please enter the first word of the square: "))
    length = len(word)
    for i in range(length -1):
        word1 = str(input("Please enter the next word of the square: "))
        while len(word1) != length:
            word1 = str(input("Please try again: "))
        word = word + word1
        i += 1
    return word

def check_word_square(square):
    n = int((len(square)+1)**0.5)
    i = 1
    for i in range(0,n,1):
        if square[n+i] != square[n*2+i]:
            return False
    return True

def menu_check_word_square():
    phrase = get_word_square()
    is_square = check_word_square(phrase)
    if is_square == True:
        n = int((len(phrase)+1)**0.5)
        print (phrase[:n])
        for i in range(n):
            if i > 0:
                print(phrase[n*i:n*i+n])
            print("is a word square!")
                      
    elif is_square == False:
        n = int((len(phrase)+1)**0.5)
        print (phrase[:n])
        for i in range(n):
            if i > 0:
                print(phrase[n*i:n*i+n])
        print("is not a word square")
def main():
    while 1 == 1:
        print_menu()
        choice = get_menu_choice()
        if choice == 1:
            menu_check_palindrome()
        if choice == 2:
            menu_check_word_square()
        if choice == 3:
            break
        choice = 0
main()
