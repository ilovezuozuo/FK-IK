import math
import numpy as np
from FK import FK
# t= np.mat(([1, 1, 1], [4, 5, 6]))
# print(a)
# l= t[1,2]
# print(l)

# T = np.mat(([9.97464523e-01, 1.62352060e-04, 7.11652966e-02, -2.47094785e-01],
#         [-1.13842071e-03, 9.99905842e-01,  1.36751695e-02,  5.37871931e-01],
#         [-7.11563756e-02, -1.37215125e-02,  9.97370789e-01,  5.89721122e-01],
#         [0,  0,  0,  1]))
# print(T)

# 以下是UR5全部取1的反算
T = np.mat(([ 1.62263535e-01, -3.93830491e-01,  9.04747528e-01,  1.37650794e+02],
 [-5.88760502e-01,  6.97158764e-01,  4.09060789e-01, -6.99381263e+01],
 [-7.91853280e-01, -5.99055259e-01, -1.18748392e-01, -5.40908287e+02],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.00000000e+00]))

print("需要反算的矩阵是：")
print(T)

def cos(a):
    return math.cos(a)
def sin(a):
    return math.sin(a)

def IK(T):
    # a = [0, -0.6127, -0.57155, 0, 0, 0]
    # d = [0.1807, 0, 0, 0.17415, 0.11985, 0.11655]
    # alpha = [math.pi / 2, 0, 0, math.pi / 2, -math.pi / 2, 0]

    a =[0,-425,-392.25,0,0,0]
    d = [89.459,0,0,109.15,94.65,82.3]
    alpha = [math.pi/2,0,0,math.pi/2,-math.pi/2,0]

    nx = T[0, 0]
    ny = T[1, 0]
    nz = T[2, 0]
    ox = T[0, 1]
    oy = T[1, 1]
    oz = T[2, 1]
    ax = T[0, 2]
    ay = T[1, 2]
    az = T[2, 2]
    px = T[0, 3]
    py = T[1, 3]
    pz = T[2, 3]


    # 求角1
    m = d[5] * ay - py

    n = ax * d[5] - px

    theta11 = math.atan2(m, n) - math.atan2(d[3], np.sqrt((m ** 2 + n ** 2 - (d[3]) ** 2)))
    theta12 = math.atan2(m, n) - math.atan2(d[3], -np.sqrt((m ** 2 + n ** 2 - (d[3]) ** 2)))
    # print(math.atan2(m, n))
    # print(math.atan2(d[3], ((m ** 2 + n ** 2 - d[3] ** 2) ** 0.5)))
    t1=[theta11,theta11,theta11,theta11,theta12,theta12,theta12,theta12]
    # for i in range (8):
    #     t1[i] = t1[i]/math.pi*180



    # 求角5
    theta51 = math.acos(ax * sin(theta11) - ay * cos(theta11))
    theta52 = -math.acos(ax * sin(theta11) - ay * cos(theta11))
    theta53 = math.acos(ax * sin(theta12) - ay * cos(theta12))
    theta54 = -math.acos(ax * sin(theta12) - ay * cos(theta12))
    t5= [theta51,theta51,theta52,theta52,theta53,theta53,theta54,theta54]

    ppp= nx * sin(1) - ny * cos(1)
    qqq= ox * sin(1) - oy * cos(1)
    # print( "!!!!!!",math.atan2(ppp, qqq) - math.atan2(sin(-1), 0))



    # 求角6
    t6= [0,0,0,0,0,0,0,0]
    for i in range (8):

        mm = nx * sin(t1[i]) - ny * cos(t1[i])
        nn = ox * sin(t1[i]) - oy * cos(t1[i])

        # print(math.atan2(mm, nn))
        # print(mm ** 2 + nn ** 2 - sin(t5[i]) ** 2)

        t6[i] = math.atan2(mm, nn) - math.atan2(sin(t5[i]), 0)

    # print(mm ** 2 + nn ** 2 - sin(t5[1]) ** 2)

    # m= nx* sin(theta11)-ny*cos(theta11)
    # n= ox*sin(theta11)- oy*cos(theta11)
    # theta61 = math.atan2(m,n) - math.atan2(sin(theta51),0)
    #
    # m = nx * sin(theta11) - ny * cos(theta11)
    # n = ox * sin(theta11) - oy * cos(theta11)
    # theta62 = math.atan2(m, n) - math.atan2(sin(theta52), 0)
    #
    # m = nx * sin(theta12) - ny * cos(theta12)
    # n = ox * sin(theta12) - oy * cos(theta12)
    # theta63 = math.atan2(m, n) - math.atan2(sin(theta53), 0)
    #
    # m = nx * sin(theta12) - ny * cos(theta12)
    # n = ox * sin(theta12) - oy * cos(theta12)
    # theta64 = math.atan2(m, n) - math.atan2(sin(theta54), 0)
    #
    # t6= [theta61,theta61,theta62,theta62,theta63,theta63,theta64,theta64]

    # 求角3
    m=[0,0,0,0,0,0,0,0]
    n=[0,0,0,0,0,0,0,0]
    for i in range(8):
        m[i] = d[4]*(sin(t6[i])*(nx*cos(t1[i])+ny*sin(t1[i]))+cos(t6[i])*(ox*cos(t1[i])+oy* sin(t1[i])))-d[5]*(ax*cos(t1[i])+ay*sin(t1[i]))+px*cos(t1[i])+py*sin(t1[i])
        n[i] = pz-d[0]-az*d[5]+d[4]*(oz*cos(t6[i])+nz*sin(t6[i]))
    # print(m)
    # print(n)

    t3=[0,0,0,0,0,0,0,0]
    t31 = math.acos((m[0]**2+n[0]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    t32 = -math.acos((m[0]**2+n[0]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    t33 = math.acos((m[2]**2+n[2]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    t34 = -math.acos((m[2]**2+n[2]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    t35 = math.acos((m[4]**2+n[4]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    t36 = -math.acos((m[4]**2+n[4]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    t37 = math.acos((m[6]**2+n[6]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    t38 = -math.acos((m[6]**2+n[6]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    t3 = [t31,t32,t33,t34,t35,t36,t37,t38]

    # for i in range(4):
    #     t3[i] = math.acos((m[i]**2+n[i]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    # for i in range(4):
    #     t3[i+4] = -math.acos((m[i+4]**2+n[i+4]**2-a[1]**2-a[2]**2)/(2*a[1]*a[2]))
    # for i in range (8):
    #     t3[i] = t3[i]/math.pi*180


    # 求角2
    t2=[0,0,0,0,0,0,0,0]
    s2= [0,0,0,0,0,0,0,0]
    c2=[0,0,0,0,0,0,0,0]
    for i in range (8):
        s2[i]= ((a[2]*cos(t3[i])+a[1])* n[i]-a[2]*sin(t3[i])*m[i])/(a[1]**2+a[2]**2+2*a[1]*a[2]*cos(t3[i]))
        c2[i] =(m[i]+(a[2]*sin(t3[i])*s2[i]))/(a[2]*cos(t3[i])+a[1])
        t2[i] = math.atan2(s2[i],c2[i])


    # 求角4
    t4=[0,0,0,0,0,0,0,0]
    for i in range(8):
        t4[i] = math.atan2(-sin(t6[i])*(nx*cos(t1[i])+ny*sin(t1[i]))-cos(t6[i])*(ox*cos(t1[i])+oy*sin(t1[i])),oz*cos(t6[i])+nz*sin(t6[i]))-t2[i]-t3[i]

    # print("第1个关节角", t1)
    # print("第2个关节角", t2)
    # print("第3个关节角", t3)
    # print("第4个关节角", t4)
    # print("第5个关节角", t5)
    # print("第6个关节角", t6)

    a1 = [t1[0], t2[0], t3[0], t4[0], t5[0], t6[0]]
    a2 = [t1[1], t2[1], t3[1], t4[1], t5[1], t6[1]]
    a3 = [t1[2], t2[2], t3[2], t4[2], t5[2], t6[2]]
    a4 = [t1[3], t2[3], t3[3], t4[3], t5[3], t6[3]]
    a5 = [t1[4], t2[4], t3[4], t4[4], t5[4], t6[4]]
    a6 = [t1[5], t2[5], t3[5], t4[5], t5[5], t6[5]]
    a7 = [t1[6], t2[6], t3[6], t4[6], t5[6], t6[6]]
    a8 = [t1[7], t2[7], t3[7], t4[7], t5[7], t6[7]]

    solution = np.mat((a1,a2,a3,a4,a5,a6,a7,a8))
    print("IK得到的结果是：")
    print(solution)



IK(T)


FK( [1.00000001,  2.3169939,  -1.7374143,  -0.72117225, -0.99999999,  4.14159265]   )



