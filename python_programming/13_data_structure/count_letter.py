def count_letter(word, letter):
    counter = 0
    for char in word:
        if char == letter:
            counter +=1
    return counter
        # print(char)

print(count_letter("Learning Pythonnnnnn", "n"))