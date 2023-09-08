def missingnum(arr):
    n=len(arr)  
    s1=0
    for i in arr:
        s1+=i    #find the sum of all elements of the array

    n=n+1        #the array has elements from 0 to (length of array +1)
    s2=(n*(n+1))//2 #sum of natural numbers from 0 to (length of array+1)

    ans=s2-s1   #missing number is the difference between the above 2 sums
    return ans

lst=[]
n=int(input("No of integers : "))

for i in range(n-1): 
    ele=int(input())
    lst.append(ele)

print("Missing Number is: ",missingnum(lst))


    
