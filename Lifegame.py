#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Craig
#
# Created:     07/10/2015
# Copyright:   (c) Craig 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass
if __name__ == '__main__':
    main()
import random

class Training():
    def __init__(self,variant,value,cost):
        self.variant = variant
        self.value = value
        self.cost = cost

gym = Training("str",1,5)

class Govt():
    def __init__(self,bracket1,bracket2,bracket3,rate1,rate2,rate3,rate4):
        self.bracket1 = bracket1
        self.bracket2 = bracket2
        self.bracket3 = bracket3
        self.rate1 = rate1
        self.rate2 = rate2
        self.rate3 = rate3
        self.rate4 = rate4
left1 = Govt(0,25000,100000,0.9,0.76,0.6,0.5)
centregovt = Govt(1500,24000,150000,0.9,0.78,0.6,0.5)
right1 = Govt(6000,30000,150000,1,0.8,0.6,0.5)
name = "Craig"


cash = [0,20,50,100,150,200,250,500,800,1000,1200,1500,2000,3000,4000,5000,10000,50000,100000,1000000]
class Entertainment():
    def __init__(self,cost,happy,food,drink,age,stre,inte,cha):
        self.cost = cost
        self.happy = happy
        self.food = food
        self.drink = drink
        self.age = age
        self.stre = stre
        self.inte = inte
        self.cha = cha

class Drink():
    def __init__(self,cost,happy,food,drink,age,stre,inte,cha):
        self.cost = cost
        self.happy = happy
        self.food= food
        self.drink = drink
        self.age = age
        self.stre = stre
        self.inte = inte
        self.cha = cha

class Food():
    def __init__(self,cost,happy,food,drink,age,stre,inte,cha):
        self.cost = cost
        self.happy = happy
        self.food= food
        self.drink = drink
        self.age = age
        self.stre = stre
        self.inte = inte
        self.cha = cha

class Job():
    def __init__(self,name,salary,happy,food,drink,degree):
        self.name = name
        self.salary = salary
        self.happy = happy
        self.degree = degree
        self.food = food
        self.drink = drink

class Player():
    def __init__(self):
        self.name = name
        self.age = 19
        self.cash = cash[random.randint(0,(len(cash)-1))]
        self.happy = 100
        self.hungry = 100
        self.thirsty = 100
        self.degree = 0
        self.int = random.randint(0,100)
        self.crtv = random.randint(0,100)
        self.str = random.randint(0,100)
        self.job = "unemployed"
    def thing(self,task):
            if self.age> task.age:
                self.cash -= task.cost
                self.happy += random.randint(1,3) * task.happy
                self.hungry += random.randint(1,3) * task.food
                self.thirsty += random.randint(1,3) * task.drink
            else:
                print "your " + str(task.rstr) + "  is too low"
            if self.happy > 100:
                self.happy = 100
            if self.thirsty > 100:
                self.thirsty = 100
            if self.hungry > 100:
                self.hungry = 100
            print "hunger = " + str(self.hungry)
            print "thirsty = " + str(self.thirsty)
            print "happy = " + str (self.happy)
            print "cash = " + str(self.cash)
    def work(self):
        tax(self.job,currentgovt)
        self.happy += random.randint(1,3) * self.job.happy
        self.hungry += random.randint(1,2) * self.job.food
        self.thirsty += random.randint(1,3) * self.job.drink


        print "hunger = " + str(self.hungry)
        print "thirst = " + str(self.thirsty)
        print "happy = " + str(self.happy)
        print "cash = " + str(self.cash)
    def train(self,task):
        if task.variant == "str":
            self.str += task.value
            self.cash -= task.cost
        print "hunger = " + str(self.hungry)
        print "thirst = " + str(self.thirsty)
        print "happy = " + str(self.happy)
        print "cash = " + str(self.cash)



playa = Player()
currentgovt = right1
def tax(job,govt):
    wage = 0
    if job.salary * 200 <= govt.bracket1:
         wage = job.salary *govt.rate1
    elif job.salary * 200 <= govt.bracket2:
        wage = job.salary
        wage -= govt.bracket1 /200
        wage *=govt.rate2
        wage += govt.bracket1 / 200 * govt.rate1
    elif job.salary * 200 <=govt.bracket3:
        wage = job.salary
        wage -= govt.bracket2 /200
        wage *= govt.rate3
        wage += (govt.bracket2 /200 - govt.bracket1 /200) * govt.rate2
        wage += govt.bracket1 /200 * govt.rate1
    else:
        wage = job.salary
        wage -= govt.bracket3 /200
        wage *= govt.rate4
        wage += (govt.bracket3 /200 -govt.bracket2 / 200) * govt.rate3
        wage += (govt.bracket2 / 200 -govt.bracket1 / 200) * govt.rate2
        wage += govt.bracket1 / 200 * govt.rate1

    playa.cash += wage


print playa.cash

PO = Job("Post Office",56,-7,-7,-7,0)
Retail = Job("Retail",50,-6,-7,-7,0)
Admin = Job("Admin",80,-4,-7,-7,0)
Programmer = Job("Programmer",150,-3,-7,-7,1)
jobs = [PO,Retail,Admin]
statement = []
for i in range (len(jobs)):
    statement += str(i+1) + " " + str(jobs[i].name),

playa.job = PO


#decision = raw_input("which job do you want?" + str(statement),)
#print jobs[(int(decision)-1)].name

Movies = Entertainment(10,10,-3,-3,16,0,0,0)
playa.thing(Movies)

Burger = Food(3,2,10,-7,5,0,0,0)
playa.thing(Burger)

Beer = Drink(4,6,-5,3,18,0,0,0)
Water = Drink(0,-3,-3,10,-1,0,0,0)
playa.thing(Beer)
print playa.cash
playa.work()
print playa.cash
print playa.str
playa.train(gym)
count = 0
options = ["Burger","Beer","Movies","work","water"]
while count < 30:

    choice = int(raw_input("what do you want to do? " + str(options)))

    if choice == 1:
        playa.thing(Burger)
    elif choice == 2:
        playa.thing(Beer)
    elif choice == 3:
        playa.thing(Movies)
    elif choice == 4:
        playa.work()
    elif choice == 5:
        playa.thing(Water)
    count +=1
    if playa.happy <1 or playa.hungry <1 or playa.thirsty <1:
        print "you have died"
        break

