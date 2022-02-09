def duplicate_count(text):
    return result


if __name__ == '__main__':
    result = duplicate_count('d')
    if result == 0:
        print('Correct')
    else:
        print('Incorrect, your answer for the first case was {}, the correct value is {} '.format(result, '0'))
    result = duplicate_count('aapoimmhww')
    if result == 3:
        print('Correct')
    else:
        print('Incorrect, your answer for the second case was {}, the correct value is {} '.format(result, '3'))
    result = duplicate_count('Indivisibilities')
    if result == 2:
        print('Correct')
    else:
        print('Incorrect, your answer for the second case was {}, the correct value is {} '.format(result, '2'))