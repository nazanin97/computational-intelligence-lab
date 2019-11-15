import random
import math

def avg(input):
    sum = 0
    for key, value in input.items():
        sum += key
    return sum/len(input)

def distocnt(input):
    sum2 = 0
    errors = {}
    for key1, value1 in centers.items():
        error = 0
        number = 0
        for key2, value2 in input.items():
            if value2 == key1:
                number = number + 1
                error += math.fabs(key2 - value1)
                sum2 += key2

        if number == 0:
            sum2 = value1
            continue
        else:
            sum2 += value1
            errors[key1] = (error / number)
            sum2 = sum2/(number + 1)
        centers[key1] = sum2
    return errors

def function1(k):
    c = {}
    for i in range(k):
        c[i] = random.randint(1, 100)
    return c

def function2(i):
    distance = {}
    for key, value in centers.items():
        distance[key] = ((i - value) ** 2)

    minD = min(distance.items(), key=lambda x: x[1])
    return minD[0]

input = {1:0, 2:0 , 5:0, 7:0, 65:0,76:0, 43:0, 23:0, 80:0, 50:0}
centers = function1(3)

for key, value in input.items():
    input[key] = function2(key)


# print("centers is : ", centers)
print("input is :", input)
print("average inputs is :", avg(input))

errors = distocnt(input)
print(errors)

sum1 = 0
for key, value in errors.items():
    sum1 += value
avg_error = sum1 / len(errors)
print("avg error is: ", avg_error)

new_error = 0
while():
    # print("centers is : ", centers)
    error2 = distocnt(input)

    for key, value in input.items():
        input[key] = function2(key)

    new_error = distocnt(input)
    flag = True

    for key, value in new_error.items():

        for key2, value2 in error2.items():
            if key == key2:
                if value2 != value:
                    flag = False

    if not flag:
        break
print("centers is : ", centers)
print(errors)

sum1 = 0
for key, value in errors.items():
    sum1 += value
avg_error = sum1 / len(errors)
print("avg error is: ", avg_error)