student_scores = [75, 84, 66, 99, 51, 65]


def get_grade_stats(scores):
    # Calculate the arithmetic mean
    a = sum(scores) / len(scores)

    # Calculate the standard deviation
    tmp = 0
    for score in scores:
        tmp += (score - a) ** 2
    b = (tmp / len(scores)) ** 0.5

    # Package and return average, standard deviation in a tuple
    return a, b


# Unpack tuple
c, d = get_grade_stats(student_scores)

print('Average score:', c)
print('Standard deviation:', d)