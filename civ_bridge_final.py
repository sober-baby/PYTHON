import matplotlib.pyplot as plt
import numpy as np
import math

L = 1200
n = 1200
P = -400

x_i = [52, 228, 392, 568, 732, 908]
P_train = [P/6, P/6, P/6, P/6, P/6, P/6]
n_train = 241
sfd = []
bmd = []


x = []
for i in range (L + 1):
    x.append(i)

for i in range(n_train):

    sfd.append([0]*1201)
    bmd.append([0]*1201)

for i in range(n_train):

    BMD = [0]*(n + 1)
    SFD = [0]*(n + 1)

    x_train = [0]*6
    for z in range(len(x_i)):
        x_train[z] = x_i[z] + i*240/(n_train - 1)

    b_y = 0
    for a in range (len(x_train)):
        b_y += x_train[a] * P_train[a]
    b_y = - b_y/L
    a_y = 400 - b_y

    point_f = [0]*(n + 1)
    point_f[0] = a_y
    point_f[n] = b_y
    for b in range (len(x_train)):
        point_f[int(x_train[b])] = P_train[b]

    temp = 0
    for c in range(n + 1):
        temp += point_f[c]
        SFD[c] = temp

    temp = 0
    for m in range(n + 1):
        temp += SFD[m]
        BMD[m] = temp


    for n in range(1201):
           sfd[i][n] = SFD[n]
           bmd[i][n] = BMD[n]


def get_abs(l):
    L_trans = np.array(l).transpose()
    L_min = []
    L_max = []
    L_abs_max = [0]*1201
    for i in range(1201):
        L_min.append(min(L_trans[i]))
        L_max.append(max(L_trans[i]))

    for i in range(1201):
        if L_min[i] < 0:
            if L_min[i] < L_max[i] * -1:
                L_abs_max[i] = L_min[i]
            else:
                L_abs_max[i] = L_max[i]
        else:
            L_abs_max[i] = L_max[i]

    return L_abs_max

# Function to get y_bar
def get_ybar_(A, y):
    global ybar
    for i in range(len(A)):
        ybar += A[i]*y[i]
    ybar = ybar/sum(A)
    return ybar

# Function to get I
def get_I(A, y, I):
    global ybar
    I_total = 0
    y_bar = get_ybar_(A,y)
    for i in range(len(A)):
        I_total += float(I[i])
        I_total += A[i] * (y_bar - y[i])**2
    return I_total

# Function to get remaining area
def get_remaining_area(a_total, A):
    total_area = a_total
    for i in A:
        total_area -= i/1.27*1260
    return total_area

# Q at centroidal axes
def get_q(Aq, yq):
    q = 0
    for i in range (len(Aq)):
        q += Aq[i] * yq[i]
    return q

def get_sttemps(s_max, b_max, y, I, q_c, q_g, height, glue_location):
    print(b_max)
    print(y)
    print(I)
    if(s_max < 0):
        s_max = -s_max
    s_top = b_max * (height-y) / I
    s_bot = b_max * y / I
    t_cent = s_max * q_c / (I * 2.54)
    t_glue = s_max * q_g / (I * glue_location)
    return s_top, s_bot, t_cent, t_glue

def thin_plate_buck(E, mu, t, b1, b2, b3):
    pi = math.pi
    S_buck1 = (4 * pi**2 * E) / (12 * (1 - mu ** 2)) * (3 * t / b1) ** 2
    S_buck2 = (0.425 * pi**2 * E) / (12 * (1 - mu ** 2)) * (3 * t / b2) ** 2
    S_buck3 = (6 * pi**2 * E) / (12 * (1 - mu ** 2)) * (3 * t / b3) ** 2
    return S_buck1, S_buck2, S_buck3

def sheer_buck(k, E, mu, t, a, n):
    pi = math.pi
    sheer_buck = (k * pi**2 * E) / (12 * (1 - mu ** 2)) * ((t / a) ** 2 + (t / n) ** 2);
    return sheer_buck

def get_fos(tension_max, comptempsion_max, sheer_max, glue_max, buck_1_max, buck_2_max, buck_3_max, buck_V_max,
        s_top, s_bot, t_cent, t_glue):
    list = []
    FOS_tens = tension_max / s_bot;
    FOS_comp = comptempsion_max / s_top;
    FOS_shear = sheer_max / t_cent;
    FOS_glue = glue_max / t_glue;
    FOS_buck1 = buck_1_max / s_top;
    FOS_buck2 = buck_2_max / s_top;
    FOS_buck3 = buck_3_max / s_top;
    FOS_buckV = buck_V_max / t_cent;
    list.append(FOS_tens)
    list.append(FOS_comp)
    list.append(FOS_shear)
    list.append(FOS_glue)
    list.append(FOS_buck1)
    list.append(FOS_buck2)
    list.append(FOS_buck3)
    list.append(FOS_buckV)
    return list

def force_capacites(fos, m, v):
    list = []
    m = abs(m)
    v = abs(v)
    tens_fail = fos[0] * m
    comp_fail = fos[1] * m;
    cent_fail = fos[2] * v;
    glue_fail = fos[3] * v;
    buck_1_fail = fos[4] * m;
    buck_2_fail = fos[5] * m;
    buck_3_fail = fos[6] * m;
    buck_fail = fos[7] * v;
    list.append(tens_fail)
    list.append(comp_fail)
    list.append(cent_fail)
    list.append(glue_fail)
    list.append(buck_1_fail)
    list.append(buck_2_fail)
    list.append(buck_3_fail)
    list.append(buck_fail)
    return list


SFD_env = get_abs(sfd)
BMD_env = get_abs(bmd)
S_max = max(SFD_env, key=abs)
B_max = max(BMD_env, key=abs)


'''
# dimensions for design 0

A = [101.6, 92.0242, 92.0242, 7.9629, 7.9629, 127]
y = [0.635, 37.5,  37.5, 74.365, 74.365, 75.635]
I = [13.656, 40264.05, 40264.05, 1.0703,1.0703,17.07]

'''
# dimensions for design final

A = [101.6, 98.3742, 98.3742, 8.89, 8.89, 127, 127, 127]
y = [0.635, 40, 40, 79.365, 79.365, 80.635, 81.905, 83.175]
I = [13.656, 49187.523, 49187.523, 1.194890083,1.194890083, 17.07, 17.07, 17.07]


#dimentions of some failed designs

'''
A = [127, 127, 127, 127, 14.3129, 14.3129,14.3129,14.3129,92.0242,92.0242,101.6]
y = [80.715, 79.445, 78.175, 76.905, 75.635, 75.635, 1.905, 1.905, 38.77, 38.77, 0.635]
I = [17.06986, 17.06986,17.06986, 17.06986, 23.0853, 23.0853, 23.0853, 23.0853, 40264.05, 40264.05, 13.656 ]


A = [127, 127, 127, 14.3129, 14.3129,14.3129,14.3129,92.0242,92.0242,101.6]
y = [79.445, 78.175, 76.905, 75.635, 75.635, 1.905, 1.905, 38.77, 38.77,0.635]
I = [17.06986, 17.06986, 17.06986, 23.0853, 23.0853, 23.0853, 23.0853, 40264.05, 40264.05, 13.656 ]
'''

# Dimensions for finding Q_cent

'''
#design 0
Aq = [50.9651, 50.9651, 101.6]
yq = [20.056, 20.056, 40.765]
'''

# final design
Aq = [50.9651, 50.9651, 101.6]
yq = []
for i in range (3):
    yq.append(y[len(y) - 1 - i] - 58.25259141692056)

# Dimensions for finding Q_glue
Ag = [127,127,127]
yg = [22.3824,23.6524,24.9224 ]

# Useful constants
E = 4000
mu = 0.2
t = 1.27
total_a = 825804

# Material properties
tension_max = 30
comptempsion_max = 6
sheer_max = 4
glue_max = 2

# I and y_bar calculation
ybar = 0
ybar = get_ybar_(A, y)
I_tot = get_I(A,y,I)
q_cent = get_q(Aq, yq)
print("q_cent:", q_cent)
q_glue = get_q(Ag, yg)
print("y bar", get_ybar_(A, y))

# sttemps calc
applied_sttemps = get_sttemps(S_max, B_max, get_ybar_(A, y), I_tot, q_cent, q_glue, 76.27, 6.27*2)
s_top = applied_sttemps[0]
s_bot = applied_sttemps[1]
t_cent = applied_sttemps[2]
t_glue = applied_sttemps[3]


#thin plate buckling calculation: case 1, 2, 3
tpb = thin_plate_buck(E, mu, t, 78.73, 10.635, (80 - ybar - 0.635))
print(tpb[0])
print("case2:", tpb[1])
print("case3:", tpb[2])

#sheer sttemps, case 4
sheer_b = sheer_buck(5, E, mu, t, (85-t), 120)

#def get_fos(tension_max, comptempsion_max, sheer_max, glue_max, buck_1_max, buck_2_max, buck_3_max, buck_V_max,
       # s_top, s_bot, t_cent, t_glue):

#fos calculation
list_fos = get_fos(tension_max, comptempsion_max, sheer_max, glue_max, tpb[0], tpb[1], tpb[2], sheer_b,
                 s_top, s_bot, t_cent, t_glue)
list_fos_int = [round(item, 4) for item in list_fos]
print(list_fos_int)
fos_min = min(list_fos_int, key=abs)
print("Min fos: ", fos_min, "Max train weight:", fos_min * 400 )

#sheer force capacities
capacities = force_capacites(list_fos, B_max, S_max)
print(capacities)

#area usage
area = get_remaining_area(total_a, A)
print("Used area:", int(total_a-area), "Remaining area:", int(area), "Used percentage:", int((total_a-area)/total_a*100),"%")


 #All plots
plt.rcParams.update({'font.size': 8})

# SFD Envelope:
plt.subplot(2, 1, 1)
plt.plot(x, SFD_env, color="blue")
plt.title("SFD Envelope")
plt.xlabel('Position(mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(-25,1225)
plt.ylim(-300,300)

# BMD Envelope:
plt.subplot(2, 1, 2)
plt.plot(x, BMD_env, color="blue")
plt.title("BMD Envelope")
plt.xlabel('Position (mm)')
plt.ylabel('Bending Moment (Nmm)')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(-25, 1225)
plt.ylim(-1000,80000)

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)

plt.subplot(3, 3, 1)
plt.plot(x, SFD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(capacities[2], color="pink")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(-700,1700)

plt.subplot(3, 3, 2)
plt.plot(x, SFD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(capacities[3], color="pink")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(-2500,4500)

plt.subplot(3, 3, 3)
plt.plot(x, SFD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(capacities[7], color="pink")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(-800,3000)

plt.subplot(3, 3, 4)
plt.plot(x, BMD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(capacities[0], color="pink")
plt.axhline(capacities[1], color="green")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(400000, 0)

plt.subplot(3, 3, 5)
plt.plot(x, BMD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(capacities[4], color="green")
plt.axhline(capacities[5], color="pink")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(8000000, 0)

plt.subplot(3, 3, 6)
plt.plot(x, BMD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
print("cap:", capacities[6])
plt.axhline(capacities[6], color="pink")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(29862289, 0)

plt.show()