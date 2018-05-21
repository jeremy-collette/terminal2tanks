a = 1

def func1():
    print('func1: ' + str(a))

def func2():
    a = 5
    print('func2: ' + str(a))

def func3():
    global a
    a = 10
    print('func3: ' + str(a))

func1()
func2()
func1()
func3()
func1()