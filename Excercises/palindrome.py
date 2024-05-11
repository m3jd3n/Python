

def check_if_palindrome(word):
    for i in range(len(word)):
        if word[i].lower() != word[-i-1].lower():
            #print("The word is not a palindrome")
            return False
            break
        else:
            #print("The word is a palindrome")
            return True
            break

def check_if_palindrome_alt(word):
    return word.lower() == word[::-1].lower()


def main():
    word = input("Please enter a word: ")
    print("You entered: ", word)
    print("check_if_palindrome result: ", check_if_palindrome(word))
    print("check_if_palindrome_alt result: ", check_if_palindrome_alt(word))


main()

