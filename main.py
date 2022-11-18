import traceback
import PySimpleGUI as sg
import datetime
from random import randint
import pandas as pd
from faker import Faker
import codecs


def read_table(filename):
    if filename is not None:
        fn = filename.split('/')[-1]
        try:
            df = pd.read_csv(filename, sep=',', engine='python')
            # Uses the first row (which should be column names) as columns names
            header_list = list(df.columns)
            # Drops the first row in the table (otherwise the header names and the first row will be the same)
            data = df[1:].values.tolist()

            return (df, data, header_list, fn)
        except:
            sg.popup_error('Error reading file')
            return


def show_table(data, header_list, fn):
    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  font='Helvetica',
                  pad=(25, 25),
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window(fn, layout, grab_anywhere=False)
    event, values = window.read()
    window.close()


def hideip(ip):
    return ip[:ip.index('.')] + ".***.***.***"


def dateToInt(date):
    return int(str(date[5:7]))


def daterand(date):
    return str(date[:8]) + str(randint(1, 30))


def advrand(adv):
    return adv + randint(-5, 5)


def advbool(adv):
    if adv >= 50:
        return ">=50"
    else:
        return "<50"


def count_dict(df):
    d = dict()
    for i in range(df.shape[0]):
        if ",".join(map(str, list(df.iloc[i]))) in d:
            d[",".join(map(str, list(df.iloc[i])))] += 1
        else:
            d[",".join(map(str, list(df.iloc[i])))] = 1
    return d


def timetothousand(time):
    if time >= 5000:
        return ">=5000"
    elif time >= 1000:
        return "1000<=>5000"
    else:
        return "<1000"


def domen(x):
    return x[x.index(".") + 1:]


def typeadv(adv):
    if " " in adv:
        return adv[:adv.index(" ")]
    else:
        return adv


def gen(path, num):
    f = codecs.open('ads.txt', encoding='utf-8')
    fakeRU = Faker(["ru_RU"])
    fake = Faker()
    s = f.readline()
    type_ads = []
    while s:
        if ":" not in s:
            type_ads.append(s[:-2])
        else:
            temp = [s[:s.index(":")]] + s[s.index(":") + 1:-1].split(";")
            for i in range(1, len(temp)):
                type_ads.append(temp[0] + temp[i])
        s = f.readline()
    f.close()
    columns = ["Пользователь", "IP адрес", "Платформы", "Дата просмотра", "Кол-во рекламы",
               "Время просмотра рекламы",
               "Вид рекламы"]
    sites = ['youtube.com', 'tiktok.com', 'instagram.com', 'dailymotion.com', 'vimeo.com', 'facebook.com',
             'twitter.com',
             'qzone.qq.com', 'weibo.com', 'linkedln.com', 'tumblr.com', 'change.org', 'renren.com', 'brainly.com',
             'pinterest.com', 'tagged.com', 'ask.fm', 'flickr.com', 'classmates.com', 'livejournal.com',
             'reddit.com',
             'deviantart.com', 'mixi.jp', 'myspace.com', 'toxicbun.com', 'vimple.com', 'wistia.com', 'cincopa.com',
             'vidyard.com', 'brightcove.com', 'twentythree.com', 'sproutvideo.com', 'dacast.com', 'onlyfans.com',
             'netflix.com', 'primevideo.com', 'tv.apple.com']
    sitesRU = ['dzen.ru', 'vk.com', 'ok.ru', 'rutube.ru', 'my.mail.ru', 'okko.tv', 'ivi.ru', 'kion.ru',
               'megogo.net',
               'start.ru', 'premier.one', 'tvigle.ru', 'wink.ru']
    df = []
    st = num
    stRu = randint(int(st / 10), int(st / 2))
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
    df.to_csv(path, mode='w', index=False)
    print("READY")
    return df

def depdf(path, flag1, flag2, flag3, flag4, flag5, flag6):
    df = pd.read_csv(path)
    if flag5 & flag2 & flag3 & flag4 & flag6 & flag1:
        df["Дата просмотра"] = df["Дата просмотра"].apply(dateToInt)
        df["Кол-во рекламы"] = df["Кол-во рекламы"].apply(advbool)
        df["Вид рекламы"] = df["Вид рекламы"].apply(typeadv)
        df["Платформы"] = df["Платформы"].apply(domen)
        df = df.drop(['Пользователь', "IP адрес", "Время просмотра рекламы"], axis=1)
        d = count_dict(df)
        dep_df = 'Платформы,Дата просмотра,Кол-во рекламы,Вид рекламы,Количество повторений\n'
        for key in d:
            if d[key] >= 5:
                dep_df += key + "," + str(d[key]) + "\n"
        f = codecs.open("depersonalize.csv", "w", encoding='utf-8')
        f.write(dep_df)
        f.close()
        print("READY")
        return
    df = df.drop(['Пользователь'], axis=1)
    if flag1:
        df = df.drop(["IP адрес"], axis=1)
    else:
        df["IP адрес"] = df["IP адрес"].apply(hideip)
    if flag2:
        df["Платформы"] = df["Платформы"].apply(domen)
    if flag3:
        df["Дата просмотра"] = df["Дата просмотра"].apply(dateToInt)
    if flag4:
        df["Кол-во рекламы"] = df["Кол-во рекламы"].apply(advbool)
    if flag5:
        df = df.drop(["Время просмотра рекламы"], axis=1)
    else:
        df["Время просмотра рекламы"] = df["Время просмотра рекламы"].apply(timetothousand)
    if flag6:
        df["Вид рекламы"] = df["Вид рекламы"].apply(typeadv)
    if not flag2:
        stats_prompt = sg.popup_yes_no('Delete "Платформы"?')
        if stats_prompt == 'Yes':
            df = df.drop(["Платформы"], axis=1)
    if not flag3:
        stats_prompt = sg.popup_yes_no("Apply date perturbation?")
        if stats_prompt == 'Yes':
            df["Дата просмотра"] = df["Дата просмотра"].apply(daterand)
    if not flag4:
        stats_prompt = sg.popup_yes_no("Apply number of advertisement perturbation?")
        if stats_prompt == 'Yes':
            df["Кол-во рекламы"] = df["Кол-во рекламы"].apply(advrand)
    d = count_dict(df)
    dep_df = ",".join(df.columns.to_list()) + ",Количество повторений\n"
    count_min_value = list(d.values()).count(1) + list(d.values()).count(2) + list(d.values()).count(3) + list(
        d.values()).count(4)
    if count_min_value / 250000 != 0:
        stats_prompt = sg.popup_yes_no("We can delete " + str(
            100 * round(count_min_value / 250000, 2)) + "% lines to establish k-anonymity = 5. Do you want to do it?")
        if stats_prompt == 'Yes':
            for key in d:
                if d[key] >= 5:
                    dep_df += key + "," + str(d[key]) + "\n"
        else:
            for key in d:
                dep_df += key + "," + str(d[key]) + "\n"
    else:
        for key in d:
            dep_df += key + "," + str(d[key]) + "\n"
    f = codecs.open("depersonalize.csv", "w", encoding='utf-8')
    f.write(dep_df)
    f.close()
    return


sg.theme('DarkAmber')
layout = [[sg.Text('Enter name of file, number of line and choose function', key="txt")],
          [sg.Text('Path to file'), sg.InputText("abc.csv", key="input"),
           sg.InputText("250000", key="inputNUM", size=(20, 20))],
          [sg.Button('Generate dataset'), sg.Button('Depersonalize dataset'), sg.Button('Calculate k-anonymity')],
          [sg.Checkbox('Удаление IP адреса', key='1'), sg.Checkbox('Маскеризация платформы', key='2'),
           sg.Checkbox('Маскеризация даты просмотра', key='3'),
           sg.Checkbox('Локальное обобщение кол-ва рекламы', key='4'),
           sg.Checkbox('Удаление времени просмотра рекламы', key='5'),
           sg.Checkbox('Микро-агрегация вида рекламы', key='6')]]

window = sg.Window('Depersonalize adv dataset', layout)
flag = [False] * 6

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break

    for i in range(6):
        if values[str(i + 1)]:
            flag[i] = True
        else:
            flag[i] = False

    if event == 'Generate dataset':
        path = values["input"]
        num = values["inputNUM"]
        try:
            df = gen(path, int(num))
            window['txt'].update("Dataset has been generated!")
            window['input'].update(value=path)
            show_prompt = sg.popup_yes_no('Show the dataset?')
            if show_prompt == 'Yes':
                show_table(df[1:].values.tolist(), list(df.columns), path.split('/')[-1])
        except:
            window['txt'].update("Error! Enter name of file, number of line and choose function again!")
            print('Ошибка:\n', traceback.format_exc())

    elif event == 'Depersonalize dataset':
        path = values["input"]
        try:
            d = depdf(path, flag[0], flag[1], flag[2], flag[3], flag[4], flag[5])
            window['txt'].update("Dataset has been depersonalized!")
            window['input'].update(value="depersonalize.csv")
            show_prompt = sg.popup_yes_no('Show the dataset?')
            if show_prompt == 'Yes':
                df, data, header_list, fn = read_table("depersonalize.csv")
                show_table(data, header_list, fn)
        except:
            window['txt'].update("Error! Enter name of file and choose function again!")
            print('Ошибка:\n', traceback.format_exc())
    elif event == 'Calculate k-anonymity':
        path = values["input"]
        try:
            df = pd.read_csv(path)
            k_an = df.min()[-1]
            layout1 = [[sg.Text("K-anonymity = " + str(k_an))]]
            if k_an < 5:
                k_iter = k_an
                x = list(range(1, 5))
                y = [list(df["Количество повторений"]).count(i) for i in x]

                if y[0] != 0:
                    layout1.append([sg.Text("K-anonimity = 1: " + str(round(y[0] / sum(y) * 100, 2)) + "%")])
                if y[1] != 1:
                    layout1.append([sg.Text("K-anonimity = 2: " + str(round(y[1] / sum(y) * 100, 2)) + "%")])
                if y[2] != 2:
                    layout1.append([sg.Text("K-anonimity = 3: " + str(round(y[2] / sum(y) * 100, 2)) + "%")])
                if y[3] != 3:
                    layout1.append([sg.Text("K-anonimity = 4: " + str(round(y[3] / sum(y) * 100, 2)) + "%")])
            window1 = sg.Window('K-anonymity', layout1)
            window1.read()
            layout2 = [[sg.Text("Number of unique lines: " + str(df.shape[0]))]]
            if k_an == 1:
                df_1 = df[df["Количество повторений"] == 1]
                show_table(df[1:].values.tolist(), list(df.columns), path.split('/')[-1])
            else:
                window2 = sg.Window('Unique lines', layout2)
                window2.read()

            window['txt'].update("Your K-anonymity = " + str(k_an))
        except:
            window['txt'].update("Error! Enter name of file and choose function again!")
            print('Ошибка:\n', traceback.format_exc())

    print('You entered ', values["input"])

window.close()
