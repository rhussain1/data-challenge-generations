def get_count(letters):
    return result


if __name__ == '__main__':
    result = get_count('aeiou')
    if result == 5:
        print('Correct')
    else:
        print('Incorrect, your answer for the first case was {}, the correct value is {} '.format(result, '5'))
    result = get_count('bcdfghjklmnpqrstvwxzy')
    if result == 0:
        print('Correct')
    else:
        print('Incorrect, your answer for the second case was {}, the correct value is {} '.format(result, '0'))