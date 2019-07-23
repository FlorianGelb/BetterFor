import time

a = [1,2,3,4,5,6,7,6]
t1= 0
t2 = 0
t = 0
x = []
def iterator(n, c, i = 0):
    global t1
    global t2
    
    t1 = time.clock()
    
    if i == n:
        t2 = time.clock()
        return
    c(i)
    iterator(n, c, i+1)

c = lambda i: print(a[i])


for i in range(1000):
    iterator(len(a), c)
    
    t += (t2 - t1)
    x.append(i)

print(t / len(x))
    

