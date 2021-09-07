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

