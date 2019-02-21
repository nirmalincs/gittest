def myrange(x,y):
    while x<y:
        x=x+1
        yield x
a=iter(myrange(10,25))
for m in a:
    print(m)
