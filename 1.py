def majority(nums:list)->int:
    dct={}
    for i in nums:
        if i not in dct:
            dct[i]=1
        else: 
            dct[i]+=1
    print(max(dct, key=dct.get))
n=int(input("nechta son kiritasiz:"))
nums=[int(input("son kirit:")) for i in range(n)]
majority(nums)