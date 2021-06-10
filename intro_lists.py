#list intro and repiting
a=['treck','chevrolet','cobalt','redline']
print(a)

#accessing elements in a list
b=['a','s','d','t','t']
print(b[3])

c=['w','f','h','y']
print(c[2].title())

#index positions start at 0,not 1
c=['ds','df','sdvfd','dfgsdfdgre','sdfweqwe']
print(c[3])
print(c[-1])

#using individual values from a list
e=['sd','ds','sd','ds','ds','ds','ds','dds','ds']
ex='my first work don by my own hand were did in school time where '+ e[3] +'!'
print(ex)

#changing adding removing elements
q=['ss','sx','sc','st','sd','rt','tre']
print(q)
q[2]='tgrfefrferfrefrf'
print(q)

e=[1,2,3,44,5,3,2,45,23,5,3]
print(e)
e.append('1234123332')
print(e)
r=[]
r.append('qertrew')
r.append('bvcdbgvfgb')
r.append('12345678')
print(r)
r.insert(4,'sdfwfdfsdf')
print(r)

del r[0]
print(r)

r=[1,2,3,4,5,6,7,8,9,12,134,343,2345,23423,3454,0.23,]
print(r)
f=r.pop()
print(r)
print(f)

#pooping items from any position
t=r.pop(4)
print(t)
print(r)
print('thise is fucking pop form list '+ t +'!')

a=[1,2,3,4,5,6,7,8,9,10]
for b in a:
    if (b % 2 == 0):
        print(b)