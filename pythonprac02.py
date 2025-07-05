#set practice 10questions
#ans1
set1={1,2,3}
set2={4,5,6}
print(set2.union(set1))


#ans2
set3={1,2,3}
set4={3,5,6}
print(set4.intersection(set3))


#ans3
set5={1,2,3,4,5,6}
set6={2,3}
print(set6.issubset(set5))

#ans4
set7={1,2,3,4,5,6}
set8={5,6}
print(set7.difference(set8))


#ans5
set9={1,2,3,4,5,6}
set10={6,7,8}
print(set9.symmetric_difference(set10))

#ans6

set11={1,2,3,4,5,6}
set12={6}
print(set11.discard(set12))

#ans7
text = "dev is a good boy"
words = text.split()             
unique_words = set(words)        
print(unique_words)



#ans8
list1=[1,1,2,3,4]
set13=set(list1)
print(set13)


#ans9
set14={1,2,3,4,5}
set15={4,5,6}
set16=set14.intersection(set15)
print(set16)
if set16==set():
    print("no elment is common")
else:
    print("common elements are :=",set16)


#ans10
squares = {x**2 for x in range(1, 11)}
print(squares)



#dictionary practise 10 questions 
#ans 1
text = "hello world"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)


#ans2
dict1={
    "mayank":20000,
    "dev":18000,
    "sumit":22000
}
max_salary= max(dict1,key=dict1.get)
print("max salary is :",max_salary)

#ans3

dict2={
    "mayank":20000,
    "dev":18000,
    "sumit":22000
}
swap={value:key for key , value in dict2.items()}       
print(swap)       



#ans4
dict4={
    "car name":"brezza",
    "model":2017
}
dict5={
    "bike name":"bullet",
    "model":2020
}
dict4.update(dict5)
print(dict4)

#ans5
dict6={
    "car name":"brezza",
    "model":2017
}
find="model"
if find  in dict6:
   print(f'{find} yes its is exists {dict6[find]}')
else:
   print(f'{find}no it is not exists')


#ans6
score1={
    'physics':98,
    'maths':99,
    'chemistry':97
}
mark=dict(sorted(score1.items(),key=lambda item: item[1]))
print(score1)
#ans7
info1={
    'name':'mayank',
    'age':20,
    'mobile':9090999990
}
info1.pop('mobile')
print(info1)
#ans8
score1={
    'physics':98,
    'maths':99,
    'chemistry':97
}
total_marks=0
for i in  score1.values():
    total_marks+=i
print(total_marks)
#ans9
lst1=['a1','a2','a3']
lst2=[10,12,13]
dict3={}
for x,y in zip(lst1,lst2):
    dict3.update({x:y})
print(dict3)
#ans10
my_dict={'a':10,'b':12,'c':13,'d':10}
list11=list(my_dict.values())
count1={value for value in list11 if list11.count(value)>1}
print(count1)




#tuple practice 10 questions
#ans1
tup=(1,2,3,4,5)
total=0
for i in tup :
    total+=i
    print(total)


    #ans2
    list1=[1,2,3,4,5]
    tup1=tuple(list1)
    print(tup1)


    #ans3
    tup3=("d","e","v")
    str1=''.join (tup3)
    print(str1)


    #ans4
    tup = ("a", "b", "c", "d")
value = "c"

if value in tup:
    index = tup.index(value)
    print("Index is:", index)
else:
    print("Value not found")



#ans5
tup = ("a", "b", "a", "c", "a", "d")
value = "a"

count = tup.count(value)
print("Count is:", count)


#ans6
tup=("dev","mayank","sunny")
for i in tup:
    print(i)


#ans7
tup12=(10,20,30)
rev=tup12[::-1]
print(rev)    


#ANS8
TUP=(1,(2,3),4)
print(TUP[1][0])

#ans9
tup=(1,2,3,4,5)
find=5
if find  in tup:
   print(f'{find} yes its is exists ')
else:
   print(f'{find}no it is not exists')


#ans10
tup=(1,2,3,4,5)
list1=list(tup)
print(list1)
list1.remove(3)

tup11=tuple(list1)
print(tup11)
   


