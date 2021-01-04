from test_framework import generic_test


from collections import Counter

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    char_freq_letter = Counter(letter_text)
    
    for c in magazine_text:
        if c in char_freq_letter:
            char_freq_letter[c] -= 1
            if char_freq_letter[c] == 0:
                del char_freq_letter[c]
                if not char_freq_letter:
                    return True
    return not char_freq_letter


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
