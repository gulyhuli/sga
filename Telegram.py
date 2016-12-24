# TelegramBotHelper
# coding=utf-8
import telebot
import constant
import random
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

import requests
import urllib.request
import re
import random as random_number
bot = telebot.TeleBot(constant.token)
global h, kj, ml


def kino():
    URL = "https://afisha.yandex.ru/selections/all-events-cinema?city=saint-petersburg"
    H = urlopen(URL)
    list25 = H.read().decode('utf-8')
    list1 = str(BeautifulSoup(list25))
    result = (re.findall(r'<h2 class="event__name" itemprop="name">.*?</h2>', list1))
    result1 = re.sub(r'<h2 class="event__name" itemprop="name">', "", str(result))
    result2 = result1.split('</h2>\', \'')
    return result2


def kino1():
    URL = "https://afisha.yandex.ru/selections/all-events-cinema?city=saint-petersburg"
    H = urlopen(URL)
    list25 = H.read().decode('utf-8')
    result = (re.findall(r'class="event__formats".*?</div>', list25))
    result1 = re.sub(r'class="event__formats">', "", str(result))
    result2 = result1.split('</div>\', \'')
    return result2


def new(n):
    URL = "https://www.yandex.ru"
    H = urlopen(URL)
    list25 = H.read().decode('utf-8')
    list1 = str(BeautifulSoup(list25))
    result = (re.findall(r'<li class="list__item"><a aria-label=\".*?\" class', list1))
    result1 = re.sub(r'<li class="list__item"><a aria-label=',"", str(result))
    result2 = result1.split('class\', \'')
    return (result2)[n]


def irodov(nomber):
    p = str(nomber)
    p1 = p[:1]
    p2 = p[2:]
    k = 'http://exir.ru/{0}/resh/{1}_{2}.htm'.format(p1, p1, p2)
    return k


def money(n):
    URL = "http://www.cbr.ru"
    H = urlopen(URL)
    listm = H.read().decode('utf-8')
    listm1 = str(BeautifulSoup(listm))
    resultm = (re.findall(r'<ins class="rubl">.*</div>', listm1))
    resultm1 = re.sub(r'<ins class="rubl">руб.</ins>', "", str(resultm))
    resultm1 = re.sub(r'xa0<i class="up" title="', "", str(resultm1))
    resultm1 = re.sub(r'xa0<i class="down" title="', "", str(resultm1))
    resultm1 = re.sub(r'</div>', "", str(resultm1))
    resultm1 = re.sub(r'</i>', "", str(resultm1))
    resultm1 = re.sub(r'\+.*\?">↑', "", str(resultm1))
    resultm1 = re.sub(r'-.*?\">↓', "", str(resultm1))
    resultm1 = re.sub(r'\\', "", str(resultm1))
    resultm1 = resultm1.split()
    if n == 0:
        resultm2 = str(resultm1[n])[2:9]
        return resultm2
    else:
        resultm2 = str(resultm1[n])[1:8]
    return resultm2


def ber(msg):
        ss = requests.Session()
        r = ss.get('https://yandex.ua/images/search?text=' + msg)
        p = 'div.class\=\"serp-item.*?url\"\:\"(.*?)\"'
        response = r.text
        w = re.findall(p, response)
        w = w[0:29:1]
        choice_f = random_number.choice(w)
        return choice_f


def you(hy):
    link = urllib.parse.urlencode({"search_query": hy})
    content = urllib.request.urlopen("https://www.youtube.com/results?" + link)
    search_results = re.findall('href=\"/watch\?v=(.*?)\"', content.read().decode())
    search_results = search_results[0:9:1]
    choice_f = random_number.choice(search_results)
    yt_link = "https://www.youtube.com/watch?v=" + choice_f
    return yt_link


def you1(hy):
    link = urllib.parse.urlencode({"search_query": hy})
    content = urllib.request.urlopen("https://www.youtube.com/results?" + link)
    search_results = re.findall('href=\"/watch\?v=(.*?)\"', content.read().decode())
    search_results = search_results[0:1:1]
    choice_f = random_number.choice(search_results)
    yt_link = "https://www.youtube.com/watch?v=" + choice_f
    return yt_link


@bot.message_handler(commands=['start'])
def hanlde_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Повеселиться', 'Узнать новости', 'Курс валют')
    user_markup.row('Смотреть видео', 'Смотреть картинки', 'Закончить')
    user_markup.row('Узнать о кино', 'Помоги с физикой', 'Закончить')
    bot.send_message(str(message.from_user.id), "{0} \n"
                                                ' чем бы ты хотел заняться ?  '.format(constant.hi),
                     reply_markup=user_markup)


@bot.message_handler(commands=['menu'])
def hanlde_menu(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Повеселиться', 'Узнать новости', 'Курс валют')
    user_markup.row('Смотреть видео', 'Смотреть картинки', 'Закончить')
    bot.send_message(str(message.from_user.id),
                     ' чем бы ты хотел заняться ?  ',
                     reply_markup=user_markup)


@bot.message_handler(commands=['startplay'])
def hanlde_menu(message):
    user_markup1 = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup1.row('/startplay', 'Начать', '/stopplay')
    user_markup1.row('Вытащить 1', 'Вытащить 2', 'Вытащить 3')
    bot.send_message(str(message.from_user.id),
                     ' Введите:"Начать"  ', reply_markup=user_markup1)


@bot.message_handler(commands=['stopplay'])
def hanlde_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(str(message.from_user.id), 'Игра закончена',
                     reply_markup=hide_markup)


@bot.message_handler(commands=['stop'])
def hanlde_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(str(message.from_user.id), 'Меню закрыто,для его возвращения введите коменду /menu',
                     reply_markup=hide_markup)


# noinspection PyGlobalUndefined
@bot.message_handler(content_types=['text'])
def hanlde_text(message):
    global kj, ml, nom
    if message.text == "Привет" or message.text == "привет" or message.text == "прив":
        bot.send_message(str(message.from_user.id), "{0} \n"
                                            'чем бы ты хотел заняться ?  '.format(random.choice(constant.hello)))
        kj = 0
        ml = 0
        nom = 0
    elif message.text == "/start":
        kj = 0
        ml = 0
        nom = 0
    elif message.text == "Узнать новости" or message.text == "узнать новости":
        kj = 0
        ml = 0
        nom = 0
        n = 0
        while n < 4:
            if n == 0:
                bot.send_message(str(message.from_user.id), str(n + 1) + ' ' + (re.sub(r'\[\'', "", str(new(n)))))
            else:
                bot.send_message(str(message.from_user.id), str(n + 1) + '. ' + (new(n)))
            n += 1
    elif message.text == "Узнать о кино" or message.text == "узнать о кино":
        bot.send_message(str(message.from_user.id), "Подождите несколько секунд, я попробую найти что-нибудь.....")
        kj = 0
        ml = 0
        nom = 0
        i = 0
        while i < len(kino()):
            if i == 0:
                bot.send_message(str(message.from_user.id), str(i + 1) + ' ' + (re.sub(r'\[\'', "", str(kino()[i]))) +
                                 str('(' + (re.sub(r'\[\'', "", str(kino1()[i]))) + ')'))
                bot.send_message(str(message.from_user.id), you1((re.sub(r'\[\'', "", str(kino()[i])))))
            elif i == len(kino()) - 1:
                bot.send_message(str(message.from_user.id), str(i + 1) + ' ' + re.sub(r'</h2>\'\]', "", str(kino()[i]))
                                 + ' ' + str('(' + (re.sub(r'</div>\'\]', "", str(kino1()[i]))) + ')'))
                bot.send_message(str(message.from_user.id), you1(re.sub(r'</h2>\'\]', "", str(kino()[i]))))
            else:
                bot.send_message(str(message.from_user.id), str(i + 1) + ' ' + (kino()[i]) + " " +
                                 '(' + (kino1()[i]) + ')')
                bot.send_message(str(message.from_user.id), you1((kino()[i])))
            i += 1

        bot.send_message(str(message.from_user.id), "Это все,что я смог найти")
    elif message.text == "Помоги с физикой" or message.text == "Физика":
        bot.send_message(str(message.from_user.id), "Введи номер задания,например,1.123")
        kj = 0
        ml = 0
        nom = 1
    elif message.text == "Закончить":
        kj = 0
        ml = 0
        nom = 0
    elif message.text == "Смотреть картинки":
        kj = 1
        ml = 0
        nom = 0
        bot.send_message(str(message.from_user.id), "Что ты хочешь посмотреть?")

    elif message.text == "Смотреть видео":
        ml = 1
        kj = 0
        nom = 0
        bot.send_message(str(message.from_user.id), "Что ты хочешь посмотреть?")
    elif message.text == "Курс валют" or message.text == "курс валют":
        kj = 0
        ml = 0
        nom = 0
        bot.send_message(str(message.from_user.id), "Информация от ЦБ РФ\n" +
                                                    "Доллар США" + ":" + money(0) + ' руб' + "\n" +
                                                    "Евро" + ":" + money(1) + ' руб')

    elif message.text == "Повеселиться" or message.text == "повеселиться":
        kj = 0
        ml = 0
        nom = 0
        bot.send_message(str(message.from_user.id), "Анекдот:\n" + random.choice(constant.hap))
    elif nom == 1:
        bot.send_message(str(message.from_user.id), "Это поможет тебе,а не я ")
        bot.send_message(str(message.from_user.id), irodov(message.text))
    elif kj == 1:
        bot.send_photo(str(message.from_user.id), ber(message.text))
    elif ml == 1:
        bot.send_message(str(message.from_user.id), text=you(message.text))
    else:
        bot.send_message(str(message.from_user.id), "К сожалению , я пока не могу понять все то , что ты мне говоришь")
    print("{0} от {1} ".format(message.text, message.from_user.first_name))


bot.polling(none_stop=True, interval=-4)
