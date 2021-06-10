def a(s="sdadqd"):
    print("my first function is  {}".format(s))
a()

#########
def a(s="sdadqd"):
    print("my first function is  ")
a()


########
def a(s="sdadqd"):
    """
asdadsdfefrf rfeew 
    """
    print("my first function is  {}".format(s))
a()


########
def hello():
    print('hello')
hello()


########
def hello():
    return 'hello'
ressdsd = hello()
print(ressdsd)

############

def addNum(num1,num2):
    return num1+num2
rerwedfdf= addNum(2,3)
print(rerwedfdf)
print(type(rerwedfdf))

#############
def addNum(num1,num2):
    return num1+num2
rerwedfdf= addNum("2","3")
print(rerwedfdf)
print(type(rerwedfdf))


#ex 2(b)
def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "sorry , I need integers!"
rerwedfdf= addNum(2,3)
print(rerwedfdf)
print(type(rerwedfdf))

###########################
#ex 2(b)
def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "sorry , I need integers!"
rerwedfdf= addNum("2","3")
print(rerwedfdf)
print(type(rerwedfdf))


#lambda expression
# filter
a = [1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2 == 0
even = filter (even_bool,a)
print (list(even) )


#land expration
a = [1,2,3,4,5,6,7,8]
lambda num:num%2==0
even = filter (lambda num:num%2==0,a)
print (list(even) )


#####################
d
st='hello'
st.lower()
st.upper()
st.split()

#############
tweet ="go sports! # sports"
result=tweet.split('#')[1]
print(result)

#########