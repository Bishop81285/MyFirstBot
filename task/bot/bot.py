def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("print(type(print)) <- What will be displayed after we run it?"
          "\n1. <class 'function'>, because it's a function, right?"
          "\n2. <class 'builtin_function_or_method'>, for it's a built-in function"
          "\n3. <class 'NoneType'>, because this function returns nothing"
          "\n4. I predict SyntaxError")
    while True:
        ans = int(input())
        if ans == 2:
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again.")
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Zoltan', '1386')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
