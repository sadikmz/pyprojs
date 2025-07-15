# Step 1 - Create a sentence maker function
# Step 2 - Create a loop which asks input from a user continously
# Step 3 - Combine everything together

def sentence_maker(text):
    quesetion_words = ['what','how','where']
    capitalized_text = text.capitalize()

    for word in quesetion_words:
        if text.startswith(word):
            return "{}?".format(capitalized_text)

    return "{}.".format(capitalized_text)

# print(sentence_maker("how hello word"))
# print(sentence_maker("hello word"))

result = []

while True:
    user_input = input("What is on your mind: ")
    if user_input == "\end":
        break
    else:
        complete_sentence = sentence_maker(user_input)
        result.append(complete_sentence)


story = " ".join(result)

print(story)
# print(result)

#  combi