student_scores = [80, 60, 50, 65, 75, 55]

# total = 0
# counter = 0
# for score in student_scores:
#     counter +=1
#     total = total + score
#
# average = total/counter
#
# score_list_above_average = []
#
# for score in student_scores:
#     if score > average:
#         score_list_above_average.append(score)
#
# total = 0
# for score in student_scores:
#     counter +=1
#     total = total + score
# print(total)

def sum_score_above_average(p_student_scores):

    # def tot_score (p_student_scores):
    total = 0
    counter = 0

    for score in p_student_scores:
        counter += 1
        total = total + score

    average = total/counter

    # print(f"The average score is: {average}")
    #  pull out values higher than the average score
    score_list_above_average = []

    for score in p_student_scores:
        if score > average:
            score_list_above_average.append(score)

    total_above_average = 0
    for score in score_list_above_average:
        # counter += 1
        if score > average:
            total_above_average = total_above_average + score
    return total_above_average

print(sum_score_above_average(student_scores))

for i in range(1,3):
    print(i)


# print(10%3)






