# Create an @authenticated decorator that only 
# allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):

    def check_arg_valid(*args):
        print("arg")
        for arg in args:
            if isinstance(arg, dict):
                if arg.get('valid'):
                    return fn(*args)
                else:
                    return "invalid arg"
    
    def check_kw_valid(**kw):
        print("kw")
        for k, v in kw.items():
            if isinstance(v, dict):
                if k == 'user':
                    if v.get('valid'):
                        return fn(**kw)
                    else:
                        print("invalid dic")                    

    def wrap(*args, **kw):
        if args:
            check_arg_valid(*args)
        elif kw:
            check_kw_valid(**kw)
    return wrap

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user=user1)