import math
import numpy as np
import random


def sigmoid(x):
    return (1 / (1 + np.exp(-x)))


def dsigmoid(m):
    dz = 0.5 * (1 - sigmoid(m) * sigmoid(m))
    return dz


def randomGenerator(m, n):
    array = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(random.uniform(-1, 1))
        array.append(a)

    print(array)
    return array


def Maintfunction(input_z, m):

    netj = []
    for i in range(4):
        sum1 = 0
        for j in range(3):
            sum1 = input_z[j] * weights[j][i] + sum1
        netj.append(sum1)

    # print(netj)
    out_put_layer1 = []
    for i in range(len(netj)):
        out_put_layer1.append(sigmoid(netj[i]))
    # print("output layer1 is ", out_put_layer1)
    sum2 = 0
    for i in range(len(out_put_layer1)):
        sum2 = out_put_layer1[i] * weights_layer2[i][0] + sum2

    o = sigmoid(sum2)
    eta = 0.2

    error1 = d[m] - o
    delta = error1 * dsigmoid(sum2)
    holder = 0
    for i in range(len(weights_layer2)):
        weights_layer2[i][0] = out_put_layer1[i] * delta * eta + weights_layer2[i][0]
        holder = holder + (delta * weights_layer2[i][0])
    # print(holder)
    # print(out_put_layer1)
    delta2 = []
    for i in range(len(out_put_layer1)):
        delta2.append(holder * out_put_layer1[i])

    for i in range(3):
        for j in range(4):
            weights[i][j] = weights[i][j] + (delta2[j] * eta * input_z[i])
    print("weights:", weights)
    return 0.5 * (error1 * error1)


def Input():
    Er1 = Maintfunction(input1, 0)
    print("er1:", Er1)
    Er2 = Maintfunction(input2, 1)
    print("er2:", Er2)
    Er3 = Maintfunction(input3, 2)
    print("er3:", Er3)
    Er4 = Maintfunction(input4, 3)
    print("er4:", Er4)
    General_error = Er1 + Er2 + Er3 + Er4
    return General_error


input1= [0, 0, -1]
input2= [0, 1, -1]
input3= [1, 0, -1]
input4= [1, 1, -1]
d = [0, 1, 1, 0]
weights = randomGenerator(4, 4)
weights_layer2 = randomGenerator(4, 1)
General_error = 0

n = 0
while Input() > 0.1:
    General_error = 0
    # error1 = 0
    n = n + 1
    print("number of training is ", n)
    print("general error is", Input())

print("training finished ")

