def is_prime(n):
    if type(n) != int:
        # type check was missed
        raise TypeError()
    elif n <= 1:
        # value range check was missed
        raise ValueError()

    # error was here: range(2, k) doesn't include k
    # hence, for example, for 9 only divisor 2 will be checked
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    try:
        answer = is_prime(n)
    except ValueError:
        print('NO')
    else:
        print('YES') if answer else print('NO')