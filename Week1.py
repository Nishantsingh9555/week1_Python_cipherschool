print("-----------WEEK-1------------")
                 #CHAPTER 1#
#-------------------------------------#
#exercise 1
#ques 1
print('this is \\\\ double blackslash')
#ques 2
print('these are /\\/\\/\\/\\ mountains')
#ques 3
print('he is \t awesome')
#ques 4
print("\\\" \\n \\t \\\' ")
#print emoji
print("\U0001F602")
#-----------------------------------#
#python as a calculator
print(2+3)
print(2-3)
print(2*3)
print(2//3)
print(2**3)
print(2/3)
print(2**0.5)
print(round(2**0.5,4))
#-------------------------------------#
#variable
a=2
b='hi'
print(a)
print(b)
#----------------------#
#STRING CONCATENATION
a='hello'
b='brother'
print(a+b)
print(a,b)
#--------------------------------#
#user input
a=input()
print('hello',a)
#-------------------------------#
#int function
a=int(input())
print(20-a)
#-------------------------------#
#split 
name, age=input().split()
print(name)
print(age)
#chapter2
#exercise 1
a=int(input())
b=int(input())
c=int(input())
print(a+b+c/3)
#-------------------------#
#index
a='hello'
print(a[0])#start
print(a[0:2])#start#stop
print(a[0:4:1])#step
#-------------------------------------#
#exercise 2
name=input()
reverse=name[-1: :-1]
print(reverse)
#-------------------------------------#
#string method 
a="hello"
print(len(a))
print(a.upper())
print(a.lower())
print(a.title())
print(a.count())
#-------------------------------------#
#exercise 3
a,b=input().split()
print(len(name))
print(name.count())
#-------------------------------------#
# replace method 
a='he is very good'
print(a.replace(' ','_'))
#-------------------------------------#
# find method
a='he is very good'
print(a.find('is'))
#-------------------------------------#
#center method
a='Harshit'
print(a.center(11,'*'))
#-------------------------------------#
#lstrip method
name='      Harshit      '
dots='..............'
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
#-------------------------------------#
#assignment operation
name="ravi"
name += "it"
print(name)
#-------------------------------------#
#if ,else condition
age =input()
age=int(age)
if age >=15:
	print(age)
else:
	print("you are above 15")
#-------------------------------------#	
#pass statement
x=18
if x>18:
	pass
#-------------------------------------#	
#chapter 3
#exercise 1
winning_number=27
user_input=input()
user_input=int(input())
if user_input==winning_number:
	print('you win')
else:
	print('you lose')
#-------------------------------------#
# and condition
a='abc'
age=19
if a=='abc' and age==19:
	print('true')
else:
	print('false')
#-------------------------------------#	
#or condition	
a='abc'
age=19
if a=='abc' or age==19:
	print('true')
else:
	print('false')
#-------------------------------------#	
#exercise 2
a=input()
age=input()
age=int((input))
if age==10 and (a[0]=='a' or a[0]=='A'):
	print('you can watch coco')
else:
	print('you cannot watch coco')
#-------------------------------------#	
#elif statement
age =input()
age=int(age)
if age >15:
	print('you are above 15')
elif age <15:
	print('you are less then 15')
else:
	print("you are 15")
#-------------------------------------#	
#in statement
name='nishant'
if 'a' in 'nishant':
	print("yes")
else:
	print('no')
#-------------------------------------#	
#check empty or not
a=""
if name:
	print("not empty")
else:
	print("empty")
#-------------------------------------#	
#loop
i=1
while i<=10:
	print('hey')
	i=i+1
#-------------------------------------#	
#exercise 3
n=input()
n=int(n)
total=0
i=1
while i <=n:
	total+=i
	i+= 1
print(total)
#-------------------------------------#
# exercise 4
num=input()
total=0
i=0
while i<len(num):
	total+=int(num[i])
	i+=1
print(total)
#-------------------------------------#
#exercise 5
name=input()
temp_var=""
i=0
while i<len(name):
	if name[i] not in temp_var:
		temp_var+=name[i]
		print(f'{name[i]}:{name.count(name[i])}')
		i+=1
#-------------------------------------#		
#infinite loop
i=0
while i<=10:
	print('hello')
#-------------------------------------#
#for loop
for i in range(10):
	print('hello world')
#------------------------------------------------------#