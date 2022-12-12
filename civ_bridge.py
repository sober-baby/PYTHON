import matplotlib.pyplot as plt
import numpy as np
import math
# L = length, n = points that are analyzed on the bridge(L/1), P = weight of train
L = 1200
n = 1200
P = -400

x = []
for i in range (L + 1):
    x.append(i)

x_train_initial = [52, 228, 392, 568, 732, 908]
P_train = [P/6, P/6, P/6, P/6, P/6, P/6]
n_train = 241
sfd = []
bmd = []

for i in range(n_train):

    sfd.append([0]*1201)
    bmd.append([0]*1201)

# Calculate shear force and bending moment across the beam in 1200 points at all positions
for i in range(n_train):
    # Make list of position of point loads at n_train = i
    x_train = [0]*6
    for z in range(len(x_train_initial)):
        x_train[z] = x_train_initial[z] + i*240/(n_train - 1)

    # Calculate reactions
    end_y = 0
    for a in range (len(x_train)):
        end_y += x_train[a] * P_train[a]
    end_y = -end_y/L
    start_y = 400 - end_y

    # Store the point forces in a list of length of 1200
    w_x = [0]*(n + 1)
    w_x[0] = start_y
    w_x[n] = end_y
    for b in range (len(x_train)):
        w_x[int(x_train[b])] = P_train[b]

    # Construct list of SF for 0<= x <= 1200 for position = i
    SF = [0]*(n + 1)
    res = 0
    for c in range(n + 1):
        res += w_x[c]
        SF[c] = res
    # Construct list of BM for 0<= x <= 1200 for position = i
    BM = [0]*(n + 1)
    res = 0
    for d in range(n + 1):
        res += SF[d]
        BM[d] = res


    for e in range(1201):
           sfd[i][e] = SF[e]
           bmd[i][e] = BM[e]


def get_max_mag(L):
    L_transpose = np.array(L).transpose()
    L_min = []
    L_max = []
    L_max_mag = [0]*1201
    for i in range(1201):
        L_min.append(min(L_transpose[i]))
        L_max.append(max(L_transpose[i]))

    for i in range(1201):
        if L_min[i] < 0:
            if -1*L_min[i] > L_max[i]:
                L_max_mag[i] = L_min[i]
            else:
                L_max_mag[i] = L_max[i]

        else:
            L_max_mag[i] = L_max[i]

    return L_max_mag

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

def get_stress(s_max, b_max, y, I, q_c, q_g, height, glue_location):
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
    S_buck1 = (4 * pi**2 * E) / (12 * (1 - mu ** 2)) * (t / b1) ** 2
    S_buck2 = (0.425 * pi**2 * E) / (12 * (1 - mu ** 2)) * (t / b2) ** 2
    S_buck3 = (6 * pi**2 * E) / (12 * (1 - mu ** 2)) * (t / b3) ** 2
    return S_buck1, S_buck2, S_buck3

def sheer_buck(k, E, mu, t, a, n):
    pi = math.pi
    sheer_buck = (k * pi**2 * E) / (12 * (1 - mu ** 2)) * ((t / a) ** 2 + (t / n) ** 2);
    return sheer_buck

def get_fos(tension_max, compression_max, sheer_max, glue_max, buck_1_max, buck_2_max, buck_3_max, buck_V_max,
        s_top, s_bot, t_cent, t_glue):
    list = []
    FOS_tens = tension_max / s_bot;
    FOS_comp = compression_max / s_top;
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

#Q at glue location
#def get_Q()
SFD_env = get_max_mag(sfd)
SFD_env[0] = 0
BMD_env = get_max_mag(bmd)
S_max = max(SFD_env, key=abs)
B_max = max(BMD_env, key=abs)


''' enter lists of Ai, yi and Ii, return I_total'''

ybar = 0
# dimensions for design 0

A = [101.6, 92.0242, 92.0242, 7.9629, 7.9629, 127]
y = [0.635, 37.5,  37.5, 74.365, 74.365, 75.635]
I = [13.656, 40264.05, 40264.05, 1.0703,1.0703,17.07]

# dimensions for design final
'''
A = [101.6, 98.3742, 98.3742, 8.89, 8.89, 127, 127, 127]
y = [0.635, 40, 40, 79.365, 79.365, 80.635, 81.905, 83.175]
I = [13.656, 49187.523, 49187.523, 1.194890083,1.194890083, 17.07, 17.07, 17.07]
'''

#dimentions of failed designs

'''
A = [127, 127, 127, 127, 14.3129, 14.3129,14.3129,14.3129,92.0242,92.0242,101.6]
y = [80.715, 79.445, 78.175, 76.905, 75.635, 75.635, 1.905, 1.905, 38.77, 38.77, 0.635]
I = [17.06986, 17.06986,17.06986, 17.06986, 23.0853, 23.0853, 23.0853, 23.0853, 40264.05, 40264.05, 13.656 ]


A = [127, 127, 127, 14.3129, 14.3129,14.3129,14.3129,92.0242,92.0242,101.6]
y = [79.445, 78.175, 76.905, 75.635, 75.635, 1.905, 1.905, 38.77, 38.77,0.635]
I = [17.06986, 17.06986, 17.06986, 23.0853, 23.0853, 23.0853, 23.0853, 40264.05, 40264.05, 13.656 ]
'''

# Dimensions for finding Q_cent

#design 0
Aq = [50.9651, 50.9651, 101.6]
yq = [20.056, 20.056, 40.765]

'''
# final design
Aq = [50.9651, 50.9651, 101.6]
yq = [20.056, 20.056, 60.405]
'''

# Dimensions for finding Q_glue

#design 0
Ag = [127]
yg = [34.235]

# Useful constants
E = 4000
mu = 0.2
t = 1.27
total_a = 825804

# Material properties
tension_max = 30
compression_max = 6
sheer_max = 4
glue_max = 2

# I and y_bar calculation
I_tot = get_I(A,y,I)
q_cent = get_q(Aq, yq)
print("q_cent:", q_cent)
q_glue = get_q(Ag, yg)
print("y bar", get_ybar_(A, y))
applied_stress = get_stress(S_max, B_max, get_ybar_(A, y), I_tot, q_cent, q_glue, 76.27, 6.27*2)
s_top = applied_stress[0]
s_bot = applied_stress[1]
t_cent = applied_stress[2]
t_glue = applied_stress[3]


#thin plate buckling calculation: case 1, 2, 3
tpb = thin_plate_buck(E, mu, t, 78.73, 10.635, 32.965)
print(tpb[0])
print("case2:", tpb[1])
print("case3:", tpb[2])

#sheer stress, case 4
sheer_b = sheer_buck(5, E, mu, t, (75-t), 400)

#def get_fos(tension_max, compression_max, sheer_max, glue_max, buck_1_max, buck_2_max, buck_3_max, buck_V_max,
       # s_top, s_bot, t_cent, t_glue):

#fos calculation
list_fos = get_fos(tension_max, compression_max, sheer_max, glue_max, tpb[0], tpb[1], tpb[2], sheer_b,
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

'''
plt.subplot(3, 3, 1)
plt.plot(x, SFD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(capacities[2], color="pink")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(-700,700)

plt.subplot(3, 3, 2)
plt.plot(x, SFD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(capacities[3], color="pink")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(-2500,2500)

plt.subplot(3, 3, 3)
plt.plot(x, SFD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(capacities[7], color="pink")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(-800,1000)

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
plt.ylim(400000, 0)

plt.subplot(3, 3, 6)
plt.plot(x, BMD_env, color = "black", linestyle='dashed')
plt.xlabel('Distance along bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(capacities[6], color="pink")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0,1200)
plt.ylim(400000, 0)

'''
plt.show()