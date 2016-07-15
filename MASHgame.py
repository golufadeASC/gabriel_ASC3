from random import *
mansion=1
apartment=2
shack=3
house=4
home=["dumpster","ur nan's house","shack",
"bottom of lake","ur boyfriend's car"]
user_input = []
get_input=raw_input("What would be your home?")
home.append(get_input)

#user_input.append(get_input)
#print(user_input)
get_rand=randint(0,4)
print ("You will live in a:", home[get_rand])
#print(random.choice(home))
Jacky_Jackof=1
Marvin_Keemstar=2
Booby_Smirnoff=3
no_one_loves_you=4
Cocky_CCadyballsman=5
name=["Jacky Jackof","Marvin Keemstar","Booby Smirnoff",
"no one loves you","Cocky CCadyballsman"]
user_input = []
get_input=raw_input("What is your name stupid?")
name.append(get_input)

#user_input.append(get_input)
#print(user_input)
get_rand=randint(0,5)
print ("Your stupid name would be:", name[get_rand])

you_are_so_trash_man=1
suck_ya_momma=2
y_are_u_still_living=3
get_a_job_you_fake_allstar=4
insult=["you are so trash man","suck ya momma",
"y are u still living",
"get a job you fake allstar"]
user_input = []
get_input=raw_input("Say something nice")
insult.append(get_input)

#user_input.append(get_input)
#print(user_input)
get_rand=randint(0,4)
print ("Awww thanks but:", insult[get_rand])