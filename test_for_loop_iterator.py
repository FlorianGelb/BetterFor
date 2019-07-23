import time

a = [1,2,3,4,5,6,7,6]
t1= 0
t2 = 0
t = 0
x = []


def iterator():
    global t2
    global t1
    
    t1 = time.clock()
    for i in range(len(a)):
        print(a[i])
    t2 = time.clock()
    
for i in range(1000):
    iterator()
    
    t += (t2 - t1)
    x.append(i)

print(t / len(x))
    

