vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
# print(list((row[0], row[1], row[2]) for row in vector))
print([i for row in vector for i in row])

