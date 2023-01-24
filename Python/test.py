L = [1,2,3,4,5]
print(L[:2]+ L[-2:])


# Q5 (10 marks)
# 5 marks for computing candy counts
# -- at most 2 marks if some progress is made
# 2 marks for getting the luckiest kid from the counts
# -- no part marks
# 3 marks for putting everything together
# -- Only give 3 marks if everything works. Take marks off depending on the
#    severity of the problem
# -- No marks for silly syntax errors
# 5 min
def luckiest_kid(haul_dataset):
    candy_count = {}
    for house, house_dat in haul_dataset.items():
        for kid, haul in house_dat.items():
            if kid not in candy_count:
                candy_count[kid] = len(haul)
            else:
                candy_count[kid] += len(haul)

    max_count = -1
    for kid, count in candy_count.items():
        if count > max_count:
            max_kid = kid
            max_count = count
    return max_kid


halloween_haul = {"house1": {"Annie": ["snickers", "mars"],
"Johnny": ["snickers"] },
"house2": {"Annie": ["coffee break", "mars"],
"Jackie":["coffee break"]}
}

print(luckiest_kid(halloween_haul))
