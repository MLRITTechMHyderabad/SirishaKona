'''def add_numbers(a,b):
    print(a+b)
add_numbers(3,7)
if int(j)>highest:
            highest=j
print(j)'''

#matrix transpose
#max and min in matrix
#merging two dictionaries
#count of words and store it in dictionary


'''l=[[1,3,100],[5,20,9],[10]]
highest=[]
for i in l:
    print(i)
    for j in i:
        j=int(j)
        highest.append(j)
print(max(highest))
print(min(highest))'''
        

'''dict1={1:"siri",2:"kona"}
dict2={1:"siri",4:"chokka"}
final_dict=[]
for i in dict1.items():
    if i in final_dict:
        pass
    final_dict.append(i)
for j in dict2.items():
    if j in final_dict:
        pass
    final_dict.append(j)
print(dict(final_dict))'''


'''a=[[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    for j in i:
        print(j)
print()'''


'''import random
a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
li=[]
for i in a:
    for j in b:
        li.append((i,j))
print(li)

di={}
for i in range(2,13):
    c=0
    for j in li:
        if i==j[0]+j[1]:
            c+=1
    di[str(i)]=c/len(li)
print(di)

players=int(input("Enter a number: "))
for k in range(1,players+1):
    player1=random.randint(1,6),random.randint(1,6)
    print(player1)
    player2=random.randint(1,6),random.randint(1,6)
    print(player2)
    player1_score=sum(player1)
    player2_score=sum(player2)
    if di[str(player1_score)] < di[str(player2_score)]:
        print("player1 wins")
    else:
        print("player2 wins")'''


#Student grades tracker
'''students=[("Alice",[85,90,78,92]),("Bob", [60, 65, 70, 75]),("Charlie", [40, 45, 50, 55]),("David", [95, 100, 98, 92])]
di=dict(students)
print(f"Dictionary of students and their grades: ",di)
for i in di.values():
    #Average grade for name
    name=input("Enter a name: ")
    val=sum(di[name])
    avg=val//4
    print(f"Average grade for {name}: ",avg)
    #Student with the highest average grade
    va=di.values()
    c=[]
    count=0
    for j in va:
        total=sum(j)//4
        c.append(total)
        highest=0
        highest=max(c)
        h=c.index(highest)
        #Number of students who passed
        for k in c:
            pass
        if k>50:
            count+=1
    print("Number of students who passed: ",count)
    print("Student with the highest average grade :",students[h][0])
    break'''

    
#Fantasy Battle Arena
'''class Character:
    def __init__(self,n,h,a,d,s):
        self.name=n
        self.health=h
        self.attack_power=a
        self.defence=d
        self.speed=s
    def attack(self,t):
        self.target=t
        target.take_damage(self.attack_power)
    def take_damage(amount):
        self.health-=amount
    def is_alive(self):
        if self.health<=0:
            return False
        return True

class Warrior(Character):
    def __init__(self,r,n,h,a,d,s):
        super().__init__(n,h,a,d,s)
        self.rage=r
    def BerserkMode(self):
        if rage==10:
            self.attack+=10
    def revert():
        #reset rage=0,attack=og
        pass
    def special(self):
        if self.health<30:
            self.attack_power*=2

class Mage(Character):
    def __init__(self,m,n,h,a,d,s):
        super().__init__(n,h,a,d,s)
        self.mana=m

class Archer(Character):
    def __init__(self,c_c,n,h,a,d,s):
        super().__init__(n,h,a,d,s)
        self.critical_chance=c_c

    def PrecisionShot(self):
        if (self.critical_chance>30):
            self.health
w=Warrior(20,"siri",50,30,20,50)
a=Archer(85,"nani",20,50,60,80)
m=Mage(10,"lucky",50,90,15,60)'''


#Employee Salary Adjustment System
employees = [{"name": "Alice", "salary": 50000, "rating": 5},{"name": "Bob", "salary": 40000, "rating": 3},{"name": "Charlie", "salary": 35000, "rating": 2}]
updated_employees = list(map(lambda emp: {"name": emp["name"],"salary": round(
emp["salary"] * (1.10 if emp["rating"] >= 4 else 1.05 if emp["rating"] == 3 else 0.97), 2
),"rating": emp["rating"]},employees))
print(updated_employees)



















































