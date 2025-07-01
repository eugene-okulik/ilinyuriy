PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

lst = PRICE_LIST.split('\n')

d = {key: int(value[:-1]) for key, value in [i.split() for i in lst]}
print(d)
