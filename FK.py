import math
import numpy as np

# a = np.mat(([1, 2, 3], [4, 5, 6]))
# b = np.mat(([1,2], [1,2],[1,2]))
# print(a)
# print(b)
# print(a.shape)
# print(b.shape)
# print(a*b)
# def cos(a):
#     return math.cos((a / 180 ) * math.pi)
# def sin(a):
#     return math.sin((a / 180) * math.pi)
def cos(a):
    return math.cos(a)
def sin(a):
    return math.sin(a)

def THT(Theta, A, D, Alpha):
    T = np.mat(([cos(Theta), -sin(Theta)*cos(Alpha), sin(Alpha)*sin(Theta), A*cos(Theta)],
                [sin(Theta), cos(Theta)*cos(Alpha), -cos(Theta)*sin(Alpha), A*sin(Theta)],
                [0, sin(Alpha), cos(Alpha), D],
                [0, 0, 0, 1]))
    return T


def FK(theta):
    # a =[0,-0.6127,-0.57155,0,0,0]
    # d = [0.1807,0,0,0.17415,0.11985,0.11655]
    # alpha = [math.pi/2,0,0,math.pi/2,-math.pi/2,0]

    # a =[0,-0.4250,-0.3922,0,0,0]
    # d = [0.1625,0,0,0.1333,0.0997,0.0996]
    # alpha = [1.57079633,0,0,1.57079633,-1.57079633,0]

    # 以下为UR5参数
    a =[0,-425,-392.25,0,0,0]
    d = [89.459,0,0,109.15,94.65,82.3]
    alpha = [math.pi/2,0,0,math.pi/2,-math.pi/2,0]


    T01 = THT(theta[0], a[0], d[0], alpha[0])
    T12 = THT(theta[1], a[1], d[1], alpha[1])
    T23 = THT(theta[2], a[2], d[2], alpha[2])
    T34 = THT(theta[3], a[3], d[3], alpha[3])
    T45 = THT(theta[4], a[4], d[4], alpha[4])
    T56 = THT(theta[5], a[5], d[5], alpha[5])




    T = np.matrix(T01 * T12 * T23 * T34 * T45 * T56)
    print(type(T))
    print("FK正向计算的结果是：")
    return T



theta = [0.09536376,  2.51144123, -1.73003667, -0.90712163, -1.89763719,  4.02417262]

a = FK(theta)
print(a)
print(a[0])
print(a.shape)
print(type(a))



