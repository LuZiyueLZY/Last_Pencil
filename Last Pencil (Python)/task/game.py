import random as rand

def pencil_case():
    number_pencils = input('How many pencils would you like to use: ')  # number of pencils
    number_pencils = numerical_check(number_pencils)
    first, second = order()
    counter = 1  # turn counter

    pencils = number_pencils * '|'
    print(pencils)

    order_game(number_pencils, counter, first, second)

def numerical_check(number_pencils_1):
    while True:  # check if the input is numeric
        if number_pencils_1.isnumeric():
            number_pencils_1 = int(number_pencils_1)
            if number_pencils_1 > 0:
                return number_pencils_1
            else:
                number_pencils_1 = input('The number of pencils should be positive: ')
        if not number_pencils_1.isnumeric():
            number_pencils_1 = input('The number of pencils should be numeric: ')


def order():
    first = str(input('Who will be the first (John, Jack): '))  # who goes first
    while first != 'John' and first != 'Jack':
        first = str(input("Choose between 'John' and 'Jack': "))
    if first == 'John':
        second = 'Jack'
        return first, second
    elif first == 'Jack':
        second = 'John'
        return first, second


def order_game(number_pencils, counter, first, second):
    if first == 'John':
        game(number_pencils, first, second, counter)
    else:
        game(number_pencils, first, second, counter)


def game(number_pencils, order_1, order_2, count):
    if order_1 == 'Jack':
        count = 2
        order_1, order_2 = order_2, order_1
    while number_pencils > 0:
        if count % 2 == 0:
            n = number_pencils_check(number_pencils)
            print(f"{order_2}'s turn:\n{n}")
            number_pencils -= n
            if number_pencils == 0:
                print(f"{order_1} won!")
                break
            pencils = number_pencils * '|'
            print(pencils)
            count += 1
        else:
            n = input(f"{order_1}'s turn! \n")
            n = one_round_check(n, number_pencils)
            number_pencils -= n
            if number_pencils == 0:
                print(f"{order_2} won!")
                break

            pencils = number_pencils * '|'
            print(pencils)

            count += 1


def number_pencils_check(number_pencils):
    if number_pencils % 4 == 0 or (number_pencils + 1) % 4 == 0 or (number_pencils + 2) % 4 == 0:
        if number_pencils % 4 == 0:
            n = 3
            return n
        if (number_pencils + 1) % 4 == 0:
            n = 2
            return n
        if (number_pencils + 2) % 4 == 0:
            n = 1
            return n
    elif number_pencils == 1:
        n = 1
        return n
    else:
        n = rand.randint(1, 3)
        return n


def one_round_check(a, number_pencils_1):
    while True:  # check if the input is numeric
        if a.isnumeric():
            a = int(a)
            if 1 <= a <= 3:
                if number_pencils_1 - a < 0:
                    a = str(input('Too many pencils were taken: '))
                else:
                    return a
            else:
                a = str(input("Possible values: '1', '2' or '3': "))
        elif type(a) != int:
            a = str(input("Possible values: '1', '2' or '3': "))


pencil_case()
