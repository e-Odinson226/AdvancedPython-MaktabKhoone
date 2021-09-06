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
many = 10
numbers = getNums(many)
res = []
for number in numbers:
    res.append( {"number": number ,
                "mEA": mEA(number) }    )

res.sort(key=lambda mEA:  mEA["mEA"], reverse=True)

try:
    if res[0]["mEA"] == res[1]["mEA"]:
        for i in range( len(res) ):
            if res[i]["mEA"] == res[i+1]["mEA"] and res[i]["number"] < res[i+1]["number"]:
                res[i], res[i+1] = res[i+1], res[i]
except:
    Exception
print(res[0]["number"], res[0]["mEA"])