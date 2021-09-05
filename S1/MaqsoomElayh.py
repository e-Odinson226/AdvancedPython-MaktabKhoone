def getNums(many):
    nums = []
    for i in range(0, many):
        adad = False
        while not adad:
            try:
                num = input(f"Enter v[{ i+1 }]: ")
                nums.append(int(num))
                adad = True
            except ValueError:
                adad = False
                print("Wrong value type")
        
    return nums

def isP(x):
    if x > 1:
        for i in range(2, (x//2)+1):
            if x%i == 0:
                return False        
        return True
    else:
        return False

def mEA(x):
    mElAvCounter = 0
    for i in range(1, x+1):
        if x % i == 0 and isP(i):
            #print( f"{x}%{i}={x%i}" ) 
            mElAvCounter += 1
    return mElAvCounter

# Main ---------------------------------------
many = 5
numbers = getNums(many)
res = []
for number in numbers:
    res.append( {number : mEA(number)} )
print(res)



#print(nums)