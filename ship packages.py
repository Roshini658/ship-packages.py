def ship_capacity(weights,D):#find minimum ship capacity brute force
    start=max(weights)#minimum capacity must be largest package
    end=sum(weights)#maximum capacity if all shipped in one day
    for cap in range(start,end+1):#try every capacity
        days=1#start with day 1
        load=0#current load in ship
        for w in weights:#check each package
            if load+w>cap:#if capacity exceeded
                days+=1#move to next day
                load=w#start new load
            else:#if capacity not exceeded
                load+=w#add package to current load
        if days<=D:#if packages shipped within D days
            return cap#return this minimum capacity
    return -1#if no capacity works
weights=[1,2,3,4,5,6,7,8,9,10]
D=5
print(ship_capacity(weights,D))
