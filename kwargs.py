def abc(**kwargs):
    print(kwargs)
    return kwargs


# a = abc(a=10, b=20)

def local():
    a = 10
    print("Fucntion: ", a)
    return a



a = local()
a += 1
print(a)