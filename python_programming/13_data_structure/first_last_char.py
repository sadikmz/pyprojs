def first_last_characters(word):
    if len(word) < 2:
        return ''
    first_two_chars = word[0:2]
    last_two_chars = word[-2:]
    # print(first_two_chars, first_last_characters())
    return first_two_chars + last_two_chars

print(first_last_characters("helloooooo"))