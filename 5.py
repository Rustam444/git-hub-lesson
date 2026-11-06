def acending(text:str)->bool:
    k=text.split(" ") # so'zni space dan split qildik
    lst=[]
    for i in k:
        if i.isdigit(): # if i son bo'lsa 
            lst.append(int(i))# lst ga qo'shgin
    if lst==sorted(lst):# lst tengmi sorted qilinganiga
        print(True)
    else:
        print(False)
x=input("so'z kiriting masalan(1 qutida 5 ta yashil, 9 ta qizil, 12 ta sariq to'p bor edi->)")
natija=acending(x)