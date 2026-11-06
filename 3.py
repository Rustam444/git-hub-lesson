def funksiya(first:list, second:list)->list:
    st=set()
    for i in first:
        st.add(i)
    for k in second:
        st.add(k)
    return st
first = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
second = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
natija=funksiya(first, second)
print(sorted(list(natija), key=lambda x: x[1:]))
