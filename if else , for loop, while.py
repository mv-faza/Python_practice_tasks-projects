#control flow
#operators
(1>2) or (2<3) # or
(1>2) and (2<3)# and
(1==2) or (2==3 or (4==4)) # multiple logic operators
(1!=1) # != is not iqual

# ex 1
if 1<2:
    print('yes!')
    if 2<3:
        print('true!')
# ex 2
if 1<2:
    print("blah blah")
    if 20<3:
        print("blah blah")

# if else nested
if 1>2:
    print("heloo")
elif 3==3:
    print("elif ran")
else:
    print ("last")

# if else nasted

if 1==1:
    if 5>2:
        print("heloo")
    elif 3==4: 
        print("elif ran")
    else:
        print ("last")

# for loop
a=[1,2,3,4,5,6]
for b in a:
    # code here
    print(b)
    print('hello')

# ex 1
a={"faza":1,"dana":2,"sam":3}
for e in a:
    print(e)
    
a={"faza":1,"dana":2,"sam":3}
for e in a:
    print(a[e])
        
#ex 2 (a)
a=[(1,2),(3,4),(5,6)]
for q in a:
    print(q)
#ex 2(b)
a=[(1,2),(3,4),(5,6)]
for (tup1,tup2) in a:
    print(tup1)
    print(tup2)


# while loop
i=1
while i<5:
    print("i is :{}".format(i))
    i=i+1

#example 1
for a in range(10):
    print(a)

# list comprohenshion
a=[1,2,3,4]
out = []
for s in a:
    out.append(s**2)

print(out)

# ex 1(b)

a=[1,2,3,4]
d=[s**2 for s in a]
print(d)
