import time
while True:
    n=int(input())
    Start_time=time.time()
    for i in range(1,n):
        if (i**n-i)%n!=0:
            print("Not a prime","[Expected time: ",time.time()-Start_time,"]")
            break
    else:
        print("Prime","[Expected time: ",time.time()-Start_time,"]")