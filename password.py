from random import choice       # choice is a function. This function import random module.

user_password = input("Enter your password: ")    # Take your password.

password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6',
            '7','8','9','<','>','/','"',':',';','`','~','!','@','#','$','%','^','&','*','(',
            ')','-','_','=','+','.']

guess = ""      # initial empty string value.
while guess != user_password:        #  guess and user_password is not ture. This is false.
    guess = ""      # import this password
    for letter in range(len(user_password)):     # This loop indicate user_password length.
        guess_letter = choice(password)         # choise function store guess_letter variable.
        guess += guess_letter                # increment guess_letter. guess_letter store guess variable.
        print(guess)              # print guess variable.
print("Your password is:", guess)         # Show your output.