def minind(a):
    min = 0
    for i in range(len(a)):
        if a[i] <= a[min]:
            min = i
    return min
def f(name):
    ind = minind(name)
    for i in range(len(name)):
        # if(ind )
        if(ind<i):
            ind = minind(name[i:]) + i
        # print(ind)
        if(name[i]>name[ind]):
            # print(name[i],name[ind])
            t = name[i]
            name = name[:i] + name[ind] + name[i + 1:]
            name = name[:ind] + t + name[ind + 1:]
            return name
    return name
name = input()
print(f(name))