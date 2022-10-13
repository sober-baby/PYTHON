#L = [5, 6, 7, 8, 9]
#L[1: 5: 2]

# incorrect L = L.appened(99) the effect is for L to become None, doesn't return anything

L = [5, 6, 7, 8]
#L.insert(1, "new")
#L.insert(len(L), "end")
#10 not in L
#L.sort()
#L = [5,4,3]
L[1:2] = [34]
print(L)
#sorted_L = sorted(L)


#myrandom.seed(0)
#login(username, password)
#Want:
# * return Ture if the username/password match
# * False if they dont, or if, the system is locked out
# * The system locks out after three consecutive incorrect login attempts

passwords[usernames.index(username)] = password
locked = False
attempted_logins = 0

def login(username, password):
    global attempted_logins, locked
    if locked:
        return False
    if username not in usernames: #global usernames?
        attempted_logins += 1
        if attempted logins == 3
            locked = True
        return False

    if passwords[usernames.index(username)] == password:
        attempted_logins = 0
        return True
    else:
        attempted_logins += 1
        if attempted_logins == 3:
            locked = True
        return False
