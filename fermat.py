#Fermat factoring
while(True):
    n=int(input())
    Y=1
    while int((n+Y**2)**0.5)!=(n+Y**2)**0.5:
        Y+=1
    X=(n+Y**2)**0.5
    print(X+Y,X-Y)
