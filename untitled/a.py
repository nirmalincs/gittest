def read(name):
    f=open(name,'r',encoding='utf-8')
    return f.readlines()
def process(lines):
    output=[]
    for x in lines:
        data=x.split(",")
        sum=int(data[2])+int(data[3])+int(data[4])
        output.append((data[0],data[1],sum))
    return output
def write(data):
    f=open("abc.txt",'r+')
    for x in data:
        str1=x[0]+","+x[1]+str(x[2])
        f.write(str1)
        f.write("\n")
def main():
    name="student.csv"
    l=read(name)
    y=process(l)
    y.sort(key=lambda x:x[2],reverse=True)
    print(y)
    write(y)
main()
