def sqrroot(x):
    s=0 #take start as 0
    e=x #take end as the number
    ans=0 #take ans as 0
    while(s<e):
        m=s+(e-s)//2 #find mid
        if(m*m==x):  #if the square of mid is equal to the number
            return m  #return mid
        elif(m*m<x): #if square of mid is less than number
            ans=m    #store mid as answer
            s=m+1    #update start to mid+1
        else:        #if square of mid is greater than number
            e=m-1    #update end to mid-1

    return ans       #return ans when loop breaks

num=int(input("Input the number: "))
print("The squareroot is: ",sqrroot(num))
        