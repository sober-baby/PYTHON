word_list_1 = open("text.txt", encoding="latin-1").read().split()
word_list = ["I", "am", "a", "sick", "man.", "I", "am", "a", "spiteful", "man.", "I", "am",
"an", "unattractive", "man.", "I", "believe", "my", "liver", "is", "diseased.",
"However,", "I", "know", "nothing", "at", "all", "about", "my", "disease,", "and",
"do", "not", "know", "for", "certain", "what", "ails", "me."]

#a
word_frequency = {}
for word in word_list:
    if word in word_frequency:
        word_frequency[word] += 1 #adding a new key and its value to dict
    else:
        word_frequency[word] = 1
print(word_frequency)

#b
def top10(L):
    L.sort()
    new_l = (L[-10:])
    return new_l

L = []
for i in range (1, 101):
    L.append(i)
print(top10(L))


#c
word_list_1 = open("prejudice.txt", encoding="latin-1").read().split()
word_frequency_1 = {}
#print(word_list_1)
for word in word_list_1:
    if word in word_frequency_1:
        word_frequency_1[word] += 1 #adding a new key and its value to dict
    else:
        word_frequency_1[word] = 1
word_frequency_r = {val: key for (key, val) in word_frequency_1.items()}
s = sorted(word_frequency_r.items())
length = len(word_frequency_r)
for i in range (10):
    print(s[length-1-i])
#for i in word_frequency.items():



import urllib.request
f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p=top%20ranked%20school%20uoft")
page = f.read().decode("utf-8")
f.close()
position1 = page.index('>About')
position2 = page.index(' search results<')
str = page[position1+7:position2]
substring = str.split(",")
int_final = ""
for i in range(len(substring)):
    int_final += substring[i]
int1 = int(int_final)
print(int1)


f1 = urllib.request.urlopen("https://ca.search.yahoo.com/search?p=top%20ranked%20school%20waterloo")
page1 = f1.read().decode("utf-8")
f1.close()
position3 = page1.index('>About')
position4 = page1.index(' search results<')
str2 = page1[position3+7:position4]
substring2 = str2.split(",")
int_final1 = ""
for j in range(len(substring2)):
    int_final1 += substring2[j]
int2 = int(int_final1)
print(int2)
if int1 > int2:
    print("uoft is better")
else:
    print("wloo is better")

#print(num1)
'''
varient = ["top ranked school uoft", "top ranked school waterloo"]
def choose_variant(varient):
   '''





















