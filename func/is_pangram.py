from string import ascii_lowercase


def is_pangram1(text):
    text = text.lower()
    is_letters = [False] * 26
    for ch in text:
        if 'a' <= ch <= 'z':
            is_letters[ord(ch) - ord('a')] = True
    for is_letter in is_letters:
        if not is_letter:
            return False
    return True


def is_pangram(text):
    text = text.lower()
    return len(set(ascii_lowercase) & set(text)) == 26


text = input()

print(is_pangram(text))