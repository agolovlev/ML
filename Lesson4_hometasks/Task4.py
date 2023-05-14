import numpy as np


def cal_euclidean(a, b):
    ## Your code here
    distance = 0.0
    for item in range(np.size(a)):
        distance += (a[item]-b[item]) ** 2
    return distance ** 0.5


def cal_manhattan(a, b):
    ## Your code here
    distance = 0.0
    for item in range(np.size(a)):
        distance += abs(a[item]-b[item])
    return distance


def cal_cosine(a, b):
    ## Your code here
    a_temp = b_temp = ab_temp = 0
    for item in range(np.size(a)):
        a_temp += a[item] ** 2
        b_temp += b[item] ** 2
        ab_temp += a[item] * b[item]
    return ab_temp / ((a_temp ** 0.5) * (b_temp ** 0.5))


a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(a, b)
print('Евклидово расстояние = ', cal_euclidean(a, b))
print('Расстояние Манхэттена  = ', cal_manhattan(a, b))
print('Расстояние Косинусное  = ', cal_cosine(a, b))
