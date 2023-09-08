def arrayManipulation(n, queries):
    arr = [0]*(n+1) #create answer array of size n
    current = 0
    max1=0
    #The idea here is to mark lcoation in the array where there is overlap.
    for a,b,k in queries:
        arr[a-1] +=k #to mark the overlap which start at a-1 ans add the number to index a-1
        arr[b]-=k    #overlap ends after b-1 so we subtract the number from b
    for j in range(n):
        current+=arr[j]
        if(current>max1):
            max1=current #find the maximum element in the array after all the operations
    return max1



n = int(input())
m = int(input())

queries = []

for i in range(m):
   list=[]
   for j in range(3):
       ele=int(input())
       list.append(ele)
   queries.append(list)

result=arrayManipulation(n, queries)
print(result)