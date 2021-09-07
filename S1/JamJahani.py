teams = {}
# t construction: { "country": "smt",
#                   "goal": "smt"}
def gameAnalyze(t1, t2):
    if t1["goal"] < t2["goal"]:
        teams[ t2["country"] ]["wins"]+=1
        teams[ t2["country"] ]["points"]+=3
        teams[ t2["country"] ]["gd"]+= t2["goal"]
        teams[ t2["country"] ]["gd"]-= t1["goal"]

        teams[ t1["country"] ]["loses"]+=1
        teams[ t1["country"] ]["gd"]+= t1["goal"]
        teams[ t1["country"] ]["gd"]-= t2["goal"]

    
    if t1["goal"] > t2["goal"]:
        teams[ t1["country"] ]["points"]+=3
        teams[ t1["country"] ]["wins"]+=1
        teams[ t1["country"] ]["gd"]+= t1["goal"]
        teams[ t1["country"] ]["gd"]-= t2["goal"]

        teams[ t2["country"] ]["loses"]+=1
        teams[ t2["country"] ]["gd"]+= t2["goal"]
        teams[ t2["country"] ]["gd"]-= t1["goal"]
    
    if t1["goal"] == t2["goal"]:
        teams[ t1["country"] ]["draws"]+=1
        teams[ t1["country"] ]["points"]+=1
        teams[ t1["country"] ]["gd"]+= t1["goal"]
        teams[ t1["country"] ]["gd"]-= t2["goal"]

        teams[ t2["country"] ]["draws"]+=1
        teams[ t2["country"] ]["points"]+=1
        teams[ t2["country"] ]["gd"]+= t2["goal"]
        teams[ t2["country"] ]["gd"]-= t1["goal"]

def getData(c1, c2, string):
    g1, g2 = string.split("-")
    cn1 = {"country": c1, "goal": int(g1)}
    cn2 = {"country": c2, "goal": int(g2)}
    return cn1, cn2



# Main ----------------------
iran =      {"wins":0,"loses":0, "draws":0, "gd":0, "points":0}
spain =     {"wins":0,"loses":0, "draws":0, "gd":0, "points":0}
portugal =  {"wins":0,"loses":0, "draws":0, "gd":0, "points":0}
morocco =   {"wins":0,"loses":0, "draws":0, "gd":0, "points":0}
teams.update({"spain" : spain})
teams.update({"iran" : iran})
teams.update({"portugal" : portugal})
teams.update({"morocco" : morocco})

s1 = input()
data1 = getData("iran", "spain", s1)
gameAnalyze(data1[0], data1[1])

s1 = input()
data1 = getData("iran", "portugal", s1)
gameAnalyze(data1[0], data1[1])

s1 = input()
data1 = getData("iran", "morocco", s1)
gameAnalyze(data1[0], data1[1])

s1 = input()
data1 = getData("spain", "portugal", s1)
gameAnalyze(data1[0], data1[1])

s1 = input()
data1 = getData("spain", "morocco", s1)
gameAnalyze(data1[0], data1[1])

s1 = input()
data1 = getData("portugal", "morocco", s1)
gameAnalyze(data1[0], data1[1])

for con in teams:
    print(f"{con} : {teams[con]}")