def test(a):
    '''
    Info: prints the parameter
    '''
    print(a)

a = 'aa'
test(a) 
# a docstring will give the info when you are calling a function

help(test) #opens the information

print(test.__doc__) #get the info aswell
