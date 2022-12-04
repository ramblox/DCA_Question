


if __name__=="__main__":

## Prepare the dictionary for the sums   
    input1=[int(i) for i in input('Enter the values').split(',')]
    n=0
    row={}
    for i in range(0,len(input1)):
        l=[]
        n+=1
        for j in range(0,len(input1)):
            l.append(input1[i]+input1[j])
        row[n]=l
    print(row)

## Find the common sums among each dictionary values
    l1=[]
    for i in range(2,n+1):
        for j in range(0,n):
            if row[i][j] in row[1]:
                l1.append(row[i][j])
    print("The list is",l1)

## Find the most frequent member in list of sums
    for i in l1:
        count=0
        for j in l1:
            if i==j:
                count=count+1
        if count==n-1:
            print("the most frequent is ",i)
            print("breaking with n as",n)
            break


## Find all the combinations which satisfy the required sum

    req_sum=i
    print("req sum is ",req_sum)

    req_list=[]
    for i in range(0,len(input1)):
        for j in range(0,len(input1)):
            if input1[i]+input1[j]==req_sum:
                req_list.append((input1[i],input1[j]))
    print(req_list)

## Find efficiency from those combinations

    sum_of_eff=0
    for i in req_list:
        sum_of_eff=sum_of_eff+i[0]*i[1]

    print("sum of efficiency is", sum_of_eff/2)


    
        

