def getter(str):
    lst = str.strip().split(".")
    lst[1] = lst[1].title()
    return lst
def calculate(mainList, data):
    if data[0] == "f":
        mainList["f"].append( { "name":data[1],
                                "lang":data[2]} )
    elif data[0] == "m":
        mainList["m"].append( { "name":data[1],
                                "lang":data[2]} )



persons = { "f":[],
            "m":[]}
# many = int(input())
# for i in range(many):
#     calculate(persons ,getter(input()) )
calculate(persons ,getter("m.zaKa.py") )
calculate(persons ,getter("m.JaDi.c+") )
calculate(persons ,getter("m.erFa.c#") )
calculate(persons ,getter("f.sArA.c+") )
calculate(persons ,getter("f.asEm.c+") )

for d in persons:
    persons[d].sort( key=lambda d: d["name"] )

for l in persons:
    for dic in persons[l]:
        print(f"{l} {dic['name']} {dic['lang']}") 
