def myfunc01(name):
    print('My name is {}'.format(name))

#myfunc01('Iris')

def myfunc02(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'
    
#myfunc02(True)

def myfunc03(a, b, c):
    if c == True:
        return a 
    else: 
        return b
    
#myfunc03('Hello', 'Goodbye', True)

def myfunc04(n):
    if n%3 == 0:
        return True
    else:
        return False

#myfunc04(15)

def myfunc05(c, d):
    if c < d:
        return True
    else:
        return False
    
#myfunc05(2,4)

