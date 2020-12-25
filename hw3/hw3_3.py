a,b=input().split()
a,b=int(a),int(b)

if(a>b or b>100 or a>100):
    print("Invalid.")
else:
    print("fahr celsius")
    
    for i in range(a,b+1,2):
        print(i,"{:>5.1f}".format(5*(i-32)/9))