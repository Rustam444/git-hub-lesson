def products(iteams: list)->list:
    t=sorted(iteams, key=lambda x: -int(x[1]))
    print(t)
iteams = [
    ('Olma', '12000', '50'),
    ('Banan', '8000', '100'),
    ('Gilos', '15000', '70'),
    ('Apelsin', '9000', '80'),
    ('Anor', '30000', '20'),
    ('Uzum', '20000', '40'),
    ('Tarvuz', '25000', '15'),
    ('Shaftoli', '18000', '60'),
    ('Qovun', '40000', '25'),
    ('Qulupnay', '35000', '10')
]
natija=(products(iteams))