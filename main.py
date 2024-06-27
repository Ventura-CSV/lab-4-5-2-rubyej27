import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while True:
        number = random.randint(0,100)
        if total + number > 100:
            break
        numbers.append(number)
        total += number
        
    numbers.append(number)

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
