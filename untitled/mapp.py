list=[1,2,3,4,5,6,7,8,9]
x=map(lambda y:y+2,list)
m=filter(lambda n:n%2!=0,list)
c=map(lambda f:f*3,filter(lambda n:n%2!=0,list))
print(c)
#for i in x:
#    print(i)
   # print("\n")
#for j in m:
 #   print(j)
for k in c:
    print(k)