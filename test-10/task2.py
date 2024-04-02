import numpy as np


def random_grades(s, g, m):
    grades_all = np.random.randint(30, 101, size=(s, g))
    mean_all = np.mean(grades_all)
    adjustment = m - mean_all
    grades_all += int(adjustment)

    return grades_all

def final_grades(g):
    final = np.mean(g, axis=1)

    return final

students = 15
grades = 20
desired_mean = 80

grades_matrix = random_grades(students, grades, desired_mean)
result = final_grades(grades_matrix)

print(np.clip(result, 0, 101))
