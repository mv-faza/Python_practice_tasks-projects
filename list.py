a ="i'm a dog"
print(a[::2]) # dve ::  oznachaech shto string budet udalyat kajdiy 2oy string 0
print(a[2:6]) # slising ot 2 go do 6 go
print(a.upper())
print(a.lower())
print(a.title())
print(a.split()) # daet tochniy raschet stringov

###

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

# list
b=[1,3,4,5,32,3,33,33,4,44,4,34,23,3,3,42,23,4,42,3,34]
c=['qwedwqedwq','true ',76.89,[1234,65445]]
print(b,c)
print(len(b))
print(len(c))

###

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

# slicing

d=['2','e','g','d','f',3]
print(d[0])
print(d[1:])
print(d[:3])
print(d[-1])
###

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#list reassigment
f=[2,1,3,4,4,55,55,3,3,1,'dsfdfd','drgrtg']
f[0]='shut your mouth'
print(f)

###

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#append
l=['a','s','d','f','a']
l.append('sdfdfgs')
print(l)
l.extend(['g','g','f','s'])
print(l)
###

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#poping list
e=['c','c','b','j','h','g']
s=e.pop()
print(e)
print(s)
s=e.pop(0)
print(e)
print(s)

###

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

# reverse and sorting list
e=['c','c','b','j','h','g']
e.reverse()
print(e)
e.sort()
print(e)

###
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

# nasted list
q=[1,3,4,['d','f','g']]
print(q[3])
q=[1,3,4,['d','f','g']]
print(q[3][2])
###

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#sample matrix example list comprhenshion

matrix=[[1,2,3],[4,5,6],[7,8,9]]
first_col=[row[0] for row in matrix]
secound_col=[row[1] for row in matrix]
therd_col=[row[2] for row in matrix]
print(first_col)
print(secound_col)
print(therd_col)