#02/04/2025
'''def add_numbers(a,b):
    print(a+b)
add_numbers(3,7)
if int(j)>highest:
            highest=j
print(j)'''

#matrix transpose
'''li=[[1,2,3],[4,5,6],[7,8,9]]
res=[0,0,0],[0,0,0],[0,0,0]
for i in range(len(li)):
    for j in range(len(li[0])):
        res[j][i]=li[i][j]
for r in res:
    print(r)'''


#max and min in matrix
'''l=[[1,3,100],[5,20,9],[10]]
highest=[]
for i in l:
    print(i)
    for j in i:
        j=int(j)
        highest.append(j)
print(max(highest))
print(min(highest))'''
        

#Removing duplicates in a dictionary
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


#merging two dictionaries
'''a=[[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    for j in i:
        print(j)
print()'''


#Student Grades Tracker
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






