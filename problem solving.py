# first problem solving 
a='django'
print(a[0])
print(a[5])
print(a[:4])
print(a[1:4]) 
print(a[4:])
print(a[::-1])
# secound problem solving
a=[3,7,[1,4,'hello']]
a[2][2]='goodbye'
print(a)
#third problem solving
e={'simple_key':'hello'}
w={'k1':{'k2':'hello'}}
q={'k1':[{'nest_key':['this is deep',['hello']]}] }
print(e['simple_key'])
print(w['k1']['k2'])
print(q['k1'][0]['nest_key'][1])
#forth problem solving
s=[1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(s))
#fivth problem solving
age=4
name='sammy'
s=("hello my dog's name is {a} and he is {b}  years old".format(a=name,b=age))
print(s)