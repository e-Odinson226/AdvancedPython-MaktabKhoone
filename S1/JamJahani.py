teams = []
# t construction: { "country": "smt",
#                   "goal": "smt"}
def gameAnalyze(t1, t2):
    if t1["goal"] < t2["goal"]:
        teams[ t2["country"] ]["wins"]+=1
        teams[ t2["country"] ]["points"]+=3
    
    if t1["goal"] > t2["goal"]:
        teams[ t1["country"] ]["points"]+=3
        teams[ t1["country"] ]["wins"]+=1
    
    if t1["goal"] == t2["goal"]:
        teams[ t1["country"] ]["draws"]+=1
        teams[ t1["country"] ]["points"]+=1

        teams[ t2["country"] ]["draws"]+=1
        teams[ t2["country"] ]["points"]+=1

def getData(c1, c2, string):
    g1, g2 = string.split("-")
    cn1 = {"country": c1, "goal": g1}
    cn2 = {"country": c2, "goal": g2}
    return c1, c2



# Main ----------------------
iran =      {"wins":0,"loses":0, "draws":0, "gd":0, "points":0}
spain =     {"wins":0,"loses":0, "draws":0, "gd":0, "points":0}
portugal =  {"wins":0,"loses":0, "draws":0, "gd":0, "points":0}
morocco =   {"wins":0,"loses":0, "draws":0, "gd":0, "points":0}
teams.append({"iran" : iran})
teams.append({"portugal" : portugal})
teams.append({"spain" : spain})
teams.append({"morocco" : morocco})
print(teams)

s1 = input()
data1 = getData("iran", "spain", s1)
gameAnalyze(data1[0])
gameAnalyze(data1[1])
print(teams)
