def nice(*args):
    return sum(args)
# receive any number of parameters with *
print(nice(1,2,3,4))

# Rule: params, *args, default parameters, **kw