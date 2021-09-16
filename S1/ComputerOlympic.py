class Person:
    def __init__(self, str):
        dude = [str.split(".")]
        self.sex = dude[0]
        self.name = dude[1]
        self.lang = dude[2]

many = int(input())
for i in range(many):
    print(i)