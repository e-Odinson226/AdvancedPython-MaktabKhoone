try:
    pplCount = int(input())
    generes = { "Horror":0,
                "Romance":0,
                "Comedy":0,
                "History":0,
                "Adventure":0,
                "Action":0 }  
    for index in range( pplCount ):
        values = input().strip().split(" ")[1:]
        print(values)
        for value in values:
            print(value, list(generes.keys()))
            if value in list(generes.keys()):
                generes[value]+=1        

except ValueError:
    print("Invalid input!!!")

try:
    listed = [{key:val} for key, val in generes.items()]
    listed.sort(key=lambda pair: list(pair.values())[0] ,reverse=True )
    print(listed)
except:
    raise Exception
