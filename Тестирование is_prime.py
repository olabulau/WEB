from yandex_testing_lesson import is_prime


def test_is_prime():
    test_cases = (
        ('not a numder', None),
        (-1, None),
        (0, None),
        (1, None),
        (3, True),
        (120, False),
    )
    for input_s, correct_output_s in test_cases:
        try:
            answer = is_prime(input_s)
        except TypeError:
            if type(input_s) == int:
                return False
        except ValueError:
            if input_s > 1:
                return False
        else:
            if correct_output_s != answer:
                return False
    return True


print('YES') if test_is_prime() else print('NO')