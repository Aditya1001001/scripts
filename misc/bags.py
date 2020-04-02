def candy_bags(l):
    if sum(l) % 3 == 0:
        print("Yes")
    else:
        print("No")

candy_bags([2,3,1,3])
candy_bags([3,1,4,3])
candy_bags([3,1,1,4,3])
