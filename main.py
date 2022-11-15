import datetime
from random import randint

import pandas as pd
from faker import Faker

fakeRU = Faker(["ru_RU"])
fake = Faker()
# Faker.seed(0)
f = open('ads.txt')
s = f.readline()
type_ads = []
while s:
    if ":" not in s:
        type_ads.append(s)
    else:
        temp = [s[:s.index(":")]] + s[s.index(":") + 1:-1].split(";")
        for i in range(1, len(temp)):
            type_ads.append(temp[0] + temp[i])
    s = f.readline()
f.close()
columns = ["Пользователь", "IP адрес", "Платформы", "Дата просмотра", "Кол-во рекламы", "Время просмотра рекламы",
           "Вид рекламы"]
sites = ['youtube.com', 'tiktok.com', 'instagram.com', 'dailymotion.com', 'vimeo.com', 'facebook.com', 'twitter.com',
         'qzone.qq.com', 'weibo.com', 'linkedln.com', 'tumblr.com', 'change.org', 'renren.com', 'brainly.com',
         'pinterest.com', 'tagged.com', 'ask.fm', 'flickr.com', 'classmates.com', 'livejournal.com', 'reddit.com',
         'deviantart.com', 'mixi.jp', 'myspace.com', 'toxicbun.com', 'vimple.com', 'wistia.com', 'cincopa.com',
         'vidyard.com', 'brightcove.com', 'twentythree.com', 'sproutvideo.com', 'dacast.com', 'onlyfans.com',
         'netflix.com', 'primevideo.com', 'tv.apple.com']
sitesRU = ['dzen.ru', 'vk.com', 'ok.ru', 'rutube.ru', 'my.mail.ru', 'okko.tv', 'ivi.ru', 'kion.ru', 'megogo.net',
           'start.ru', 'premier.one', 'tvigle.ru', 'wink.ru']
print(len(sites))
df = []
print("Сколько сгенерировать строк?\n")
st = int(input())
stRu = randint(int(st/10), int(st/2))
for i in range(stRu):
    n = randint(1, 100)
    sec = randint(30, 120)
    df.append([fakeRU.free_email(), fakeRU.ipv4(), sitesRU[randint(0, len(sitesRU) - 1)],
               fakeRU.date_between(datetime.date(2022, 6, 1), datetime.date(2022, 9, 1)), n, n * sec,
               type_ads[randint(0, len(type_ads) - 1)]])
for i in range(stRu, st):
    n = randint(1, 100)
    sec = randint(30, 120)
    df.append([fake.free_email(), fake.ipv4(), sites[randint(0, len(sites) - 1)],
               fake.date_between(datetime.date(2022, 6, 1), datetime.date(2022, 9, 1)), n, n * sec,
               type_ads[randint(0, len(type_ads) - 1)]])
df = pd.DataFrame(df, columns=columns)
df.to_csv(r'advertisement.csv', mode='a', index=False)
print("READY")
