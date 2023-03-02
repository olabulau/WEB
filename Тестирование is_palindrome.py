from yandex_testing_lesson import is_palindrome


def test_is_palindrome():
    test_cases = (
        ('', True),
        ('a', True),
        ('aba', True),
        ('ab', False),
        ('abc', False),
    )
    for input_s, correct_output_s in test_cases:
        if is_palindrome(input_s) != correct_output_s:
            return False
    return True


print('YES' if test_is_palindrome() else 'NO')