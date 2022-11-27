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
SFD_all = []
BMD_all = []

for i in range(n_train):

    SFD_all.append([0]*1201)
    BMD_all.append([0]*1201)

# Calculate the shear force and bending moment across the beam in 1200 points
# at 241 positions of the train from when the train is completely on the beam
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
           SFD_all[i][e] = SF[e]
           BMD_all[i][e] = BM[e]


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

'''
Calculate Applied Stress
S_top =
S_bot =
T_cent =
T_glue =
'''

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

'''
%% 5. Material and Thin Plate Buckling Capacities
E = 4000;
mu = 0.2;
S_tens =
S_comp =
T_max =
T_gmax =
S_buck1 =
S_buck2 =
S_buck3 =
T_buck =



'''
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
    FOS_buck1 = s_buck_1_max / s_top;
    FOS_buck2 = s_buck_2_max / s_top;
    FOS_buck3 = s_buck_3_max / s_top;
    FOS_buckV = buck_V_max / T_cent;
    list.append(FOS_tens)
    list.append(FOS_comp)
    list.append(FOS_shear)
    list.append(FOS_glue)
    list.append(FOS_buck1)
    list.append(FOS_buck2)
    list.append(FOS_buck3)
    list.append(FOS_buckV)
    return list


#Q at glue location
#def get_Q()
SFD_env = get_max_mag(SFD_all)
SFD_env[0] = 0
BMD_env = get_max_mag(BMD_all)
S_max = max(SFD_env, key=abs)
B_max = max(BMD_env, key=abs)
#print(S_max)
#print(B_max)
''' use SFD_env[i] or BMD_env[i] to retrive values at specific locations'''

'''
plt.subplot(2, 1, 1)
plt.plot(x, SFD_env)
plt.title("SFD Envelope")
plt.xlabel('Position(mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(-25,1225)
plt.ylim(-300,300)
'''

'''
# SFD:
plt.subplot(2, 1, 1)
plt.plot(x, SFD_env)
plt.title("SFD Envelope")
plt.xlabel('Position(mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(-25,1225)
plt.ylim(-300,300)
'''

# SFD Envelope:
plt.subplot(2, 1, 1)
plt.plot(x, SFD_env)
plt.title("SFD Envelope")
plt.xlabel('Position(mm)')
plt.ylabel('Shear Force (N)')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(-25,1225)
plt.ylim(-300,300)

# BMD Envelope:
plt.subplot(2, 1, 2)
plt.plot(x, BMD_env)
plt.title("BMD Envelope")
plt.xlabel('Position (mm)')
plt.ylabel('Bending Moment (Nmm)')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(-25, 1225)
plt.ylim(-1000,80000)

''' uncomment to get graph'''
#plt.show()


''' enter lists of Ai, yi and Ii, return I_total'''

ybar = 0
# dimensions for design 0
total_a = 825804
A = [101.6, 92.0242, 92.0242, 7.9629, 7.9629, 127]
y = [0.635, 37.5,  37.5, 74.365, 74.365, 75.635]
I = [13.656, 40264.05, 40264.05, 1.0703,1.0703,17.07]


#current design dimentions
'''
A = [127, 127, 14.3129, 14.3129,14.3129,14.3129,92.0242,92.0242,101.6]
y = [78.175, 76.905, 75.635, 75.635, 1.905, 1.905, 38.77, 38.77, 0.635]
I = [17.06986, 17.06986, 23.0853, 23.0853, 23.0853, 23.0853, 40264.05, 40264.05, 13.656 ]

total_a = 825804
A = [127, 127, 14.3129, 14.3129,14.3129,14.3129,92.0242,92.0242,101.6]
y = [78.175, 76.905, 75.635, 75.635, 1.905, 1.905, 38.77, 38.77,0.635]
I = [17.06986, 17.06986, 23.0853, 23.0853, 23.0853, 23.0853, 40264.05, 40264.05, 13.656 ]
'''

# Dimensions for finding Q_cent
Aq = [50.9651, 50.9651, 101.6]
yq = [20.056, 20.056, 40.765]

# Dimensions for finding Q_glue
Ag = [127]
yg = [34.235]

# Useful constants
E = 4000
mu = 0.2
t = 1.27

# Material properties
tension_max = 30
compression_max = 6
sheer_max = 4
glue_max = 2

I_tot = get_I(A,y,I)
area = get_remaining_area(total_a, A)
q_cent = get_q(Aq, yq)
q_glue = get_q(Ag, yg)
applied_stress = get_stress(S_max, B_max, get_ybar_(A, y), I_tot, q_cent, q_glue, 76.27, 6.27*2)
S_top = applied_stress[0]
S_bot = applied_stress[1]
T_cent = applied_stress[2]
T_glue = applied_stress[3]


#tau
sheer_b = sheer_buck(5, E, mu, t, (75-t), 400)


#def thin_plate_buck(E, mu, t, b1, b2, b3):
tpb = thin_plate_buck(E, mu, t, 78.73, 10.635, 32.965)
print(tpb[0])
print(tpb[1])
print(tpb[2])

#fos
#def get_fos(tension_max, compression_max, sheer_max, glue_max, buck_1_max, buck_2_max, buck_3_max, buck_V_max,
        #s_top, s_bot, t_cent, t_glue):
list_fos = get_fos(tension_max, compression_max, sheer_max, glue_max, tpb[0], tpb[1], tpb[2], sheer_b,
                 s_top, s_bot, t_cent, t_glue, S_buck1, S_buck2, S_buck3, sheer_buck)


'''
print("Used area:", int(total_a-area), "Remaining area:", int(area), "Used percentage:", int((total_a-area)/total_a*100),"%")
print(ybar)
print(q_glue)
'''























#all FOS calculations


