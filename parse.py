import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import config
import sqlite3
from itertools import chain, product



conn = sqlite3.connect('all_info.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS info(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   product_name TEXT,
   price TEXT,
   photo_url TEXT,
   product_url TEXT);
""")
conn.commit()

def soup():
    with open('data.txt', 'r', encoding='UTF-8') as f:
        a = f.readline()
        b = a.split(';')
        print(b)
        if b[0] == '1':
            url = f'https://www.kufar.by/l?ot=1&query={b[4]}&sort=lst.d'
        elif b[3] == '#':
            url = f'https://www.kufar.by/l/r~{b[1]}?ot=1&query={b[4]}&sort=lst.d'
        elif b[3] != '#':
            url = f'https://www.kufar.by/l/r~{b[3]}?ot=1&query={b[4]}&sort=lst.d'
        #url = f'https://www.kufar.by/l?ot=1&query=шапка&sort=lst.d'
        headers = {'accept': '*/*',
                   'user-agent': UserAgent().random}
        print(url)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

def names():
    names = soup().find_all('h3', class_="kf-Yovr-ffe0d")
    del names[:3]
    del names[-3:]
    for i in names:
        cur.execute("""INSERT INTO info(product_name) VALUES(?);""", (i.text,))
    conn.commit()

    prise = soup().find_all('p', class_='kf-YopJ-ded05')
    del prise[:3]
    del prise[-3:]
    cur.execute("SELECT id FROM info;")
    all_ids = cur.fetchall()
    zpr = []
    zid = []
    zz = []
    for i in all_ids:
        zid.append(i[0])
    for i in prise:
        zpr.append(i.text)
    for i in enumerate(zpr):
        zz.append((i[1], zid[i[0]]))
    price_apdate = """UPDATE info SET price=? WHERE id=?;"""
    cur.executemany(price_apdate, zz)
    conn.commit()


    photo = soup().find_all('img', class_='kf-MPpg-8a381 lazyload')
    del photo[:3]
    del photo[-3:]
    with open('photo.txt', 'w', encoding='UTF-8') as f:
        for i in photo:
            f.write(f'{i}\n')
    with open('photo.txt', 'r', encoding='UTF-8') as f:
        a = f.readlines()
        srcs = []
        for i in a:
            b = i.split()
            for k in enumerate(b):
                if k[1] == 'lazyload"':
                    x = k[0] + 1
            srcs.append(b[x])
    srcss = []
    with open('photo.txt', 'w', encoding='UTF-8') as f:
        for i in srcs:
            k = i.split('"')
            f.write(f'{k[1]}\n')
            srcss.append(k[1])

    zzz = []
    for i in enumerate(srcss):
        zzz.append((i[1], zid[i[0]]))
    photo_apdate = """UPDATE info SET photo_url=? WHERE id=?;"""
    cur.executemany(photo_apdate, zzz)
    conn.commit()

    product_url = soup().find_all('a', class_='kf-Yop-a43ab')
    del product_url[:3]
    del product_url[-3:]
    prod_urls = []
    for i in product_url:
        prod_urls.append(str(i))
    zzzz = []
    ur = []
    for k in prod_urls:
        t = k.split('"')
        ur.append(t[3])

    for i in enumerate(ur):
        zzzz.append((i[1], zid[i[0]]))
    product_url_apdate = """UPDATE info SET product_url=? WHERE id=?;"""
    cur.executemany(product_url_apdate, zzzz)
    conn.commit()


def run_parse():
    cur.execute("DELETE FROM info;")
    conn.commit()
    names()




