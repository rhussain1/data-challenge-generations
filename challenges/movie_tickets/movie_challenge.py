import math


def movie(card, ticket, perc):
    return 0


if __name__ == '__main__':
    result = movie(500, 15, 0.9)
    if result == 43:
        print('Correct')
    else:
        print('Incorrect, your answer for the first case was {}, the correct value is {} '.format(result, '43'))
    result = movie(100, 10, 0.95)
    if result == 24:
        print('Correct')
    else:
        print('Incorrect, your answer for the second case was {}, the correct value is {} '.format(result, '24'))