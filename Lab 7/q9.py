# wap to demonstrate positional arguments and functional arguments in function

def func(a,b,c):
# ''' arugments passed to functions are functional argument
# '''
    print(a,b,c)

func(1,2,3)

def positional(a,b,c):
# ''' arugments sent in specific order passed to functions are positional argument'''
    print(a,b,c)

positional(1,2,3)