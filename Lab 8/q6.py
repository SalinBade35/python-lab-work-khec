#Write a Python program to access a function inside a function. 


def fun1():
    print("hi i am function 1")
    def fun2():
        print("hi i am function 2")
        def fun3():
            print("hi i am function 3")
        return fun3()
    return fun2()

fun1()
