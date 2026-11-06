def janr(cinema: list, genr: str) -> list:
    t = [i for i in cinema if i["genre"].strip() == genr.strip()]
    return t
cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]
kiritilgan_janr = input("Film janrini kiriting (Masalan: Fantastika): ")
natija = janr(cinema, kiritilgan_janr)
print(natija)
