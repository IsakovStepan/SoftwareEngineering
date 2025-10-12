grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
result1 = [4 if grade == 3 else grade for grade in grades1 if grade != 2]
print(result1)

grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
result2 = [4 if grade == 3 else grade for grade in grades2 if grade != 2]
print(result2)

grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
result3 = [4 if grade == 3 else grade for grade in grades3 if grade != 2]
print(result3)