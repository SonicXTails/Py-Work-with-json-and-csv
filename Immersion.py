from colorama import *
import time
import pygame
import random
import json
import csv

cols = ['Имя', 'Возраст', 'Способность', 'Недостаток', 'Волосы', 'Торс', 'Пояс']
def save_to_CSV(data):
    with open('Table.csv', 'w', encoding='cp1251', newline='') as file:
        writer = csv.DictWriter(file, delimiter=";", fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)
        
def play_game():
    cups = set(range(1, 4))
    ball_cup = random.choice(list(cups))
    print("Игра началась! Угадайте, в каком стаканчике находится шарик.")
    guess = int(input("Выбери номер стаканчика (1-3): "))
    if guess == ball_cup:
        print("Поздравляю, ты угадал! Шарик находится в стаканчике", ball_cup, "(На этом всё, так как не укладывался в срок)")
    else:
        print("Ты не угадал. Шарик находится в другом стаканчике. (На этом всё, так как не укладывался в срок)")

""" Множество - def_game
    Список - Инвентарь
    Словарь - Man\Woman """

inventory = [] # Пустой список для данных инвентаря... Возможео стоит поменять на множитель

man = {'Имя': 'Нет',
       'Возраст': '34',
       'Способность': 'Повышенная харизма',
       'Недостаток': 'Не может общаться с богатыми',
       'Волосы': 'Чёрные',
       'Торс': 'Толстовка',
       'Пояс': 'Спортивные штаны',
       'Инвентарь': 'Что-то похожее на нож, но в бою бесполезное', }

woman = {"Имя": "Нет",
       "Возраст": "25",
       "Способность": "Может общаться со всеми",
       "Волосы": "Каштановые",
       "Торс": "Свитер",
       "Пояс": "Юбка",
       "Инвентарь": ""}

def thanks():
    time.sleep(3)
    print("Отдельные благодарности:")
    print("------------------------")
    time.sleep(3)
    print("Артём Асеев - Сценарист (Ну тупо основу дал)")
    time.sleep(3)
    print("Лев Мацас - лучший тестеровщик в 1:40 по мск ну, точнее по его времени в 5:40.")

"""Вводимый пользователем текст"""
def user_txt():
    try:
        txt = (str(input(Fore.LIGHTGREEN_EX + "\nВы: " + Style.RESET_ALL)))
        txt = txt.lower()
        txt = txt.capitalize()
        return txt
    except ValueError:
        print()
def nach_txt():
    print(Fore.LIGHTGREEN_EX + "\nВы *про себя*:")

def choose_your_name_man():
    man.clear()
    man['Имя'] = user_txt()
    man['Возраст'] = '34'
    man['Способность'] = 'Повышенная харизма'
    man['Недостаток'] = 'Не может общаться с богатыми'
    man['Волосы'] = 'Чёрные'
    man['Торс'] = 'Толстовка'
    man['Пояс'] = 'Спортивные штаны'
    man['Инвентарь'] = 'Что-то похожее на нож, но в бою бесполезное'
    return man
def choose_your_name_woman():
    woman.clear()
    woman["Имя"] = user_txt()
    woman["Возраст"] = "25"
    woman["Способность"] = "Может общаться со всеми"
    woman["Волосы"] = "Каштановые"
    woman["Торс"] = "Свитер"
    woman["Пояс"] = "Юбка"
    return woman

"""Всё это относиться к инвентарю"""
def first_open_inventory():
    print(Fore.CYAN + ("\n\t\t\t\t\t\t\t\tВоу, воу, вы открыли способность смотреть в инвентарь!\n\t\t\t\t\t\tВы в любой момент (когда вы можете вводить данные) можете написать \"Инвентарь\".\n\t\t\t\t\t\t\t\tи вы сможете насладиться своими находками, так держать!\n\t\t\t\t\t\t\t\t\t\t\tпопробуйте открыть его сейчас)" + Style.RESET_ALL))
    while True:
        try:
            txt = user_txt()
        except ValueError:
            continue
        if type(txt) == str and txt == "Инвентарь":
            print(inventory_return())
            break
        else:
            print(Fore.RED + "\nВы *про себя*:"), printd(Style.RESET_ALL + "\tПо-моему... Я что-то должен сделать перед этим... Но вот что?\n")
def inventory_add(item):
    inventory.append(item)
    save_in_JSON_inventory(inventory)

def inventory_return():
    return inventory

def save_in_JSON_inventory(inventory):
    inventory = json.dumps(inventory)
    inventory = json.loads(str(inventory))
    with open('Inventory.json', 'w', encoding='utf-8') as file:
        json.dump(inventory, file, indent=4, ensure_ascii=False)

def inventory_show(user_txt):
    if type(user_txt) == str and user_txt == "Инвентарь":
        if user_txt == "Инвентарь":
            if inventory_return() == []:
                print("Ваш инвентарь пуст!")
            else:
                print(inventory_return())

"""Пробелы"""
def cls(): print("\n" * 36)

"""Для музыки"""
def play_music(mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
"""Для звуков"""
def play_sound(mp3):
    pygame.init()
    sound2 = pygame.mixer.Sound(mp3)
    sound2.play()

"""Красивый вывод (побуквенный)"""
"""delay=0.07"""
def printd(text, delay=0):
    from time import sleep
    for char in text:
        print(char, end='')
        sleep(delay)

"""Начало (условное приветствие)"""
def start():
    print(
        "\t\t\t\t\t\t\t\t\t\t\tЗдравствуй игрок!\n\t\t\t\t\t\t\tК вашему вниманию представлен проект: \"Immersion\"!\nЗдесь вас ждёт увлекательное путешествие на Землю в виде инопришеленца, который должен изучить данный мир.\n\t\t\tДанный проект не пытаеться никого оскорбить и все совпадения исключительно случайны.\n"), print(
        Fore.CYAN + "\t\t\t\t\t\t\t\t\t\t  Приятного прохождения!" + Style.RESET_ALL), print(
        Fore.RED + "\t\t\t\t\t\t\t\t\t Для продолжения напишите: \"GO!\"" + Style.RESET_ALL)
    while True:
        try:
            GO = str(input())
            GO = GO.upper()
        except ValueError:
            continue
        if type(GO) == str and GO == "GO!":
            cls()
            break
        else:
            print("Вы не ввели \"GO!\"")
            cls()

"""Начало (Готов \ Я не готов)"""
def beginning():
    while True:
        try:
            txt = user_txt()
        except ValueError:
            continue
        if type(txt) == str and txt == "Готов":
            cls()
            fly()
            break

        elif type(txt) == str and txt == "Я не готов":
            cls()
            first_not_ready()
            break
        else:
            print(Fore.RED + "\nНеизвестный:"), printd(Style.RESET_ALL + "\t- Что ты сказал? Я тебя не расслышал...\n")

"""Первый (я не готов)"""
def first_not_ready():
    print(Fore.RED + "\nНеизвестный:"), printd(Style.RESET_ALL + "\t- Чтож... тогда полетит другой кандидат. Арестуйте его!\n")
    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Да всмы, дайте на дорожку осмотреться.\n")
    print(Fore.RED + "Неизвестный:"), printd(Style.RESET_ALL + "\t- Мггххх... Ладно, но только не долго\n")
    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Конечно, сер\n")
    time.sleep(2)
    cls()
    print(Fore.LIGHTBLACK_EX + " Перед вами представленна довольно большая комната, она довольно тёмная, но вы видете через огромное\nстекло на потолке луну, которая освещает данное помещение. В комнате стоят два охранника \nи учёный (вы делаете данный вывод из-за его белого халата и бейджека справа от груди). Вы знаете, что это место вы видите\nвозможно в последний раз, но не чуствуете страха или иного тревожного чувства.\n\n Вы же, в свою очередь, находитесь в небольшой технике, которая неподвластна Земному пониманию. \nЗемлянин бы сделал вывод, что это особый летательный аппарат. В нём вы можете увидеть MP3 - плеер\nУ вас промелькает мысль о том, что данный предмет может быть вам полезен.\n\nНапишите ваше действие: \"Взять\" или \"Оставить\"")
    while True:
        try:
            Take_MP3_player_or_not = str(input())
            Take_MP3_player_or_not = Take_MP3_player_or_not.lower()
            Take_MP3_player_or_not = Take_MP3_player_or_not.capitalize()
        except ValueError:
            continue
        if type(Take_MP3_player_or_not) == str and Take_MP3_player_or_not == "Взять":
            cls()
            inventory_add("MP3-player")
            print(Fore.RED + "\nВы *про себя*:"), printd(Style.RESET_ALL + "\tХмм... Довольная классная вещь. Правда старая как мой дедушка, ну и ладно)\n")
            first_open_inventory()
            # Цикл, пока не откроться инвентарь
            inventory_show(user_txt)
            second_not_ready()
            break

        elif type(Take_MP3_player_or_not) == str and Take_MP3_player_or_not == "Оставить":
            cls()
            print(Fore.RED + "\nВы *про себя*:"), printd(Style.RESET_ALL + "\tДа зачем мне он нужен? Мы давно уже опередили Землян и изоблели другой гаджет, который лучше в тысячу раз.\n")
            second_not_ready()
            break
        else:
            print(Fore.RED + "\nВы *про себя*:"), printd(Style.RESET_ALL + "\tПо-моему... Я не могу так сделать\n")

"""Второй (Я не готов)"""
def second_not_ready():
    print(Fore.RED + "\nНеизвестный:"), printd(Style.RESET_ALL + "\t- Ну что? Готов? Напиши: \"Готов\" если ты не против начать или \"Я не готов\" если ты ещё не готов преступить к путешествию.\n")
    while True:
        try:
            txt = user_txt()
        except ValueError:
            continue
        if type(txt) == str and txt == "Готов":
            cls()
            fly()
            break

        elif type(txt) == str and txt == "Я не готов":
            cls()
            first_end()
            break
        else:
            print(Fore.RED + "\nНеизвестный:"), printd(Style.RESET_ALL + "\t- Что ты сказал? Я тебя не расслышал...\n")
"""Первая концовка (Если два раза выбрать (Я не готов))"""
def first_end():
    print(Fore.RED + "\nВы не подчинились приказу, за что были арестованы за неповиновение в службе \"Immersion\"\n"
                     "Вы будете лишены всего вашего имущества и социального рейтинга, вы НИКОГДА не вернётесь в свой"
                     " дом.\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tСлава \"Immersion'у!\"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + Style.RESET_ALL)
    play_music("3. First_ending.mp3")
    thanks()
    time.sleep(15)
    pygame.mixer.music.set_volume(0.3)
def fly():
    print(Fore.RED + "Неизвестный:"), printd(Style.RESET_ALL + "\t- Что-ж... Удачи тебе, 业严丯中乫丯丯中业严\n")
    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Чего? \n")
    play_sound("1. Chego_Chego.mp3")
    time.sleep(1)
    cls(), print("\n")
    first_location()

def first_location():
    play_music("2. Choose_of_character.mp3")
    pygame.mixer.music.set_volume(0.3)
    str(input("Чтобы продолжить, нажмите Enter:"))
    pygame.mixer.music.pause()
    cls()

    print("\t\t\t...Прошло около 4 часов Земного времени...\n\n\n\n\n\n\n\n")
    print(Fore.GREEN + "Вы: ")
    printd(Style.RESET_ALL + ("\t- Уфф... Перелёт был довольно тяжёлый, но пора уже приступать к цели, но для начала... \nНужно выбрать менее приметную форму, чтобы живые организмы принимали меня за своего.\n\n"))
    choose_of_character()

def woman_game():
    def Go_dark():
        cls()
        print(Fore.CYAN + "Вы проходите через арку в здании и натыкаетесь на мужчину, который для вас кажетсья опасным")
        print(Fore.CYAN + "К сожалению вы были разрублены на несколько частей и проданы на органы")
        with open('Character.json', 'w', encoding='utf-8') as file:
            json.dump(woman, file, indent=4, ensure_ascii=False)
        with open('Character.json', 'r', encoding='utf-8') as file:
            Character_data = json.load(file)
        with open('Table.csv', 'w', encoding='cp1251', newline='') as file:
            writer = csv.DictWriter(file, delimiter=";", fieldnames=Character_data)
            writer.writeheader()
            writer.writerow(Character_data)

    def Go_man():
        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Подходите, не стесняйтесь...\n")
        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(
            Style.RESET_ALL + "\t- Добрый день!\n")
        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Не хотите поиграть в игру?\n")
        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(
            Style.RESET_ALL + "\t- Ну допустим\n")
        print(Fore.RED + "\nЧеловек:"), printd(
            Style.RESET_ALL + "\t- Вам необходимо угадать в каком из стаканчиков находиться шарик:\n")
        print(Fore.CYAN + "Перед вами три стаканчика:")

        with open('Character.json', 'w', encoding='utf-8') as file:
            json.dump(woman, file, indent=4, ensure_ascii=False)
        with open('Character.json', 'r', encoding='utf-8') as file:
            Character_data = json.load(file)
        with open('Table.csv', 'w', encoding='cp1251', newline='') as file:
            writer = csv.DictWriter(file, delimiter=";", fieldnames=Character_data)
            writer.writeheader()
            writer.writerow(Character_data)
        play_game()
        thanks()

    def repeat_woman_goman_godark():
        while True:
            match user_txt():
                case "Подойти к мужчине":
                    Go_man()
                    break
                case "Пойти в тёмный переулок":
                    Go_dark()
                    break
                case "Инвентарь":
                    inventory_show("Инвентарь")
                case _:
                    nach_txt(), printd(
                        Style.RESET_ALL + "\tНе... Чёт не то.\n")

    def Osmotr():
        cls()
        print(Fore.CYAN + "Вы решаете ещё осмотретья и замечаете человека, который сидит на лавочке рядом с дорогой.\nДля вас он выглядет очень старым и вам он особо не интересен.\n\nВыберете действие: \n\tПодойти к человеку\n\tПойти в лес\n\tПойти асфальтированной дороге")
        while True:
            match user_txt():
                case "Подойти к человеку":
                    print(Fore.CYAN + "Вы решаете подойти к человеку. Вы приблизились к нему" + Style.RESET_ALL)
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Добрый день!\n")
                    print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Здравствуй! (кринж но блин сорри)\n")
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- А чего вы у дороги тут стоите?\n")
                    print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Да вот... жду таких лошарок, как ты)\n")
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Не пон. Ты что во мне лошарку видишь?\n")
                    print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Пока да, вот сыграй в игру, может и не буду так считать))\n")
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\tНу го, что за игра?\n")
                    print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Ну смотри. У меня есть предмет, который выдаёт опредёленное число в диапазоне от 1 до 10, если угадаешь, то кое что получишь.\n")
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\tНу го (я не смогу сейчас открыть инвентарь)\n\n")
                    numbers = ["1","2","3","4","5","6","7","8","9","10"]
                    print(Fore.CYAN + "Вы думаете какое число выбрать" + Style.RESET_ALL)
                    if user_txt() == random.choice(numbers): # Открыть инвентарь нельзя
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Не ну ты кончено хороша, но у меня есть другой выход из данной ситуации\n")
                        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\tИ какой же?\n")
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Ну вот... такой)\n")
                        print(Fore.CYAN + "Данный человек направляет на вас странный предмет, который вы не не успеваете рассмотреть, так как в вашем черепе\nпоявилсась огромная дырка. Вы к сожалению умерли...\n\n\n" + Style.RESET_ALL)
                        thanks()
                    else:
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Нет, ты не угадал.\n")
                        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Да иди ты... я пошёл.\n")
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Стой! Мне нужно знать твоё имя\n")
                        choose_your_name_woman()
                        name = woman.get("Имя")
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + f"\t- Приятно было повидаться, {name}.\n")
                        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы *про себя*:"), printd(Style.RESET_ALL + "\t- Ну и нафига нужно было ему моё имя?\n")
                        print(Fore.CYAN + "Вы немного расстроились из-за данной ситуации, но вам это не помешает продолжить ваше путишествие, так что скорей выберайте действие!\n\tПойти в лес\n\tПойти по асфальтированной дороге")
                        while True:
                            match user_txt():
                                case "Пойти в лес":
                                    Go_forest()
                                    break
                                case "Пойти по асфальтированной дороге":
                                    Go_road()
                                    break
                                case "Инвентарь":
                                    inventory_show("Инвентарь")
                                case _:
                                    nach_txt(), printd(
                                        Style.RESET_ALL + "\tНе... Чёт не то.\n")

    print(Fore.CYAN + "Вы выбрали характеристики женщины: " + Style.RESET_ALL, woman)
    nach_txt(), print("\tТак, я готова начать.\n")
    print(
        Fore.CYAN + "\t\t\t\t\t\t\t\tВы осматриваете местность в которой очутились. Перед вами раскинуля большой лес и тропинка, которая ведёт в самую гущу данного леса\n\t\t\t\t\t\t\t\tСправа вы видите асфальтурованную дорогу.\n")
    print(Fore.CYAN + "Выберете действие:\n\tОсмотреться\n\tПойти в лес\n\tПойти по асфальтированной дороге")
    def Go_forest():
        print(Fore.CYAN + "Вы решаете пойти по лесной тропинке. На половине пути, вы замечаете, что тропинка заканчивается и начинается дорога, вы решаете продолжать идти до данной дороге" + Style.RESET_ALL)
        Go_road()
    def Go_road():
        print(Fore.CYAN + "Через некоторое время, вы видите большие здания, которые вас особо не впечатлили, ибо на своей планете вы видели вещи намного круче, чем то, что видите сейчас.")
        print(Fore.CYAN + "В городе вы замечаете прилавок, за которым стоит мужчина и кричит, что готов сыграть в игру")
        print(Fore.CYAN + "Также вы видите темный переулок")
        print(Fore.CYAN + "Пора выбрать действие:)))\n\tПодойти к мужчине\n\tПойти в тёмный переулок\n\tОсмотреться")
        while True:
            match user_txt():
                case "Подойти к мужчине":
                    Go_man()
                    break
                case "Пойти в темный переулок":
                    Go_dark()
                    break
                case "Осмотреться":
                    print("Вы ничего нового не заметили.")
                    repeat_woman_goman_godark()
                case "Инвентарь":
                    inventory_show("Инвентарь")
                case _:
                    nach_txt(), printd(Style.RESET_ALL + "\tНе... Чёт не то.\n")
    while True:
        match user_txt():
            case "Осмотреться":
                Osmotr()
                break
            case "Пойти в лес":
                Go_forest()
                break
            case "Пойти по асфальтированной дороге":
                Go_road()
                break
            case "Инвентарь":
                inventory_show("Инвентарь")
            case _:
                nach_txt(), printd(Style.RESET_ALL + "\tЗачем это делать? (ты сказал шо ты шаришь в этой теме...)\n")

    print(Fore.CYAN + "Выберете действие:\n\tОсмотреться\n\tПойти в лес\n\tПойти по асфальтированной дороге")
    while True:
        match user_txt():
            case "Осмотреться":
                Osmotr()
                break
            case "Пойти в лес":
                Go_forest()
                break
            case "Пойти по асфальтированной дороге":
                Go_road()
                break
            case "Инвентарь":
                inventory_show("Инвентарь")
            case _:
                nach_txt(), printd(Style.RESET_ALL + "\tЗачем это делать? (ты сказал шо ты шаришь в этой теме...)\n")

def man_game():
    def Go_dark():
        cls()
        print(Fore.CYAN + "Вы проходите через арку в здании и натыкаетесь на мужчину, который для вас кажетсья опасным")
        print(Fore.CYAN + "К сожалению вы были разрублены на несколько частей и проданы на органы\n\n\n")
        with open('Character.json', 'w', encoding='utf-8') as file:
            json.dump(man, file, indent=4, ensure_ascii=False)
        with open('Character.json', 'r', encoding='utf-8') as file:
            Character_data = json.load(file)
        with open('Table.csv', 'w', encoding='cp1251', newline='') as file:
            writer = csv.DictWriter(file, delimiter=";", fieldnames=Character_data)
            writer.writeheader()
            writer.writerow(Character_data)
        thanks()
    def Go_man():
        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Подходите, не стесняйтесь...\n")
        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Добрый день!\n")
        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Не хотите поиграть в игру?\n")
        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Ну допустим\n")
        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Вам необходимо угадать в каком из стаканчиков находиться шарик:\n")
        print(Fore.CYAN + "Перед вами три стаканчика:")
        with open('Character.json', 'w', encoding='utf-8') as file:
            json.dump(man, file, indent=4, ensure_ascii=False)

        with open('Character.json', 'r', encoding='utf-8') as file:
            Character_data = json.load(file)

        with open('Table.csv', 'w', encoding='cp1251', newline='') as file:
            writer = csv.DictWriter(file, delimiter=";", fieldnames=Character_data)
            writer.writeheader()
            writer.writerow(Character_data)
        play_game()
        thanks()
    def repeat_man_goman_godark():
        while True:
            match user_txt():
                case "Подойти к мужчине":
                    Go_man()
                    break
                case "Пойти в тёмный переулок":
                    Go_dark()
                    break
                case "Инвентарь":
                    inventory_show("Инвентарь")
                case _:
                    nach_txt(), printd(
                        Style.RESET_ALL + "\tНе... Чёт не то.\n")

    def Osmotr():
        cls()
        print(Fore.CYAN + "Вы решаете ещё осмотретья и замечаете человека, который сидит на лавочке рядом с дорогой.\nДля вас он выглядет очень старым и вам он особо не интересен.\n\nВыберете действие: \n\tПодойти к человеку\n\tПойти в лес\n\tПойти асфальтированной дороге")
        while True:
            match user_txt():
                case "Подойти к человеку":
                    print(Fore.CYAN + "Вы решаете подойти к человеку. Вы приблизились к нему" + Style.RESET_ALL)
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Добрый день!\n")
                    print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Здравствуй! (кринж но блин сорри)\n")
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- А чего вы у дороги тут стоите?\n")
                    print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Да вот... жду таких лошар, как ты)\n")
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Не пон. Ты что во мне лошару видишь?\n")
                    print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Пока да, вот сыграй в игру, может и не буду так считать))\n")
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\tНу го, что за игра?\n")
                    print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Ну смотри. У меня есть предмет, который выдаёт опредёленное число в диапазоне от 1 до 10, если угадаешь, то кое что получишь.\n")
                    print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\tНу го (я не смогу сейчас открыть инвентарь)\n")
                    numbers = ["1","2","3","4","5","6","7","8","9","10"]
                    print(Fore.CYAN + "Вы думаете какое число выбрать" + Style.RESET_ALL)
                    if user_txt() == random.choice(numbers): # Открыть инвентарь нельзя
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Не ну ты кончено хорош, но у меня есть другой выход из данной ситуации\n")
                        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\tИ какой же?\n")
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Ну вот... такой)\n")
                        print(Fore.CYAN + "Данный человек направляет на вас странный предмет, который вы не не успеваете рассмотреть, так как в вашем черепе\nпоявилась огромная дырка. Вы к сожалению умерли...\n\n\n" + Style.RESET_ALL)
                        thanks()
                    else:
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Нет, ты не угадал.\n")
                        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Да иди ты... я пошёл.\n")
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + "\t- Стой! Мне нужно знать твоё имя\n")
                        choose_your_name_man()
                        name = man.get("Имя")
                        print(Fore.RED + "\nЧеловек:"), printd(Style.RESET_ALL + f"\t- Приятно было повидаться, {name}.\n")
                        print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы *про себя*:"), printd(Style.RESET_ALL + "\t- Ну и нафига нужно было это имя?\n")
                        print(Fore.CYAN + "Вы немного расстроились из-за данной ситуации, но вам это не помешает продолжить ваше путишествие, так что скорей выберайте действие!\n\tПойти в лес\n\tПойти по асфальтированной дороге")
                        while True:
                            match user_txt():
                                case "Пойти в лес":
                                    Go_forest()
                                    break
                                case "Пойти по асфальтированной дороге":
                                    Go_road()
                                    break
                                case "Инвентарь":
                                    inventory_show("Инвентарь")
                                case _:
                                    nach_txt(), printd(Style.RESET_ALL + "\tНе... Чёт не то.\n")
                    break
                case "Пойти в лес":
                    Go_forest()
                    break
                case "Пойти по асфальтированной дороге":
                    Go_road()
                    break
                case "Инвентарь":
                    inventory_show("Инвентарь")
                case _:
                    nach_txt(), printd(Style.RESET_ALL + "\tЗачем это делать? (ты сказал шо ты шаришь в этой теме...)\n")
    def Go_forest():
        print(Fore.CYAN + "Вы решаете пойти по лесной тропинке. На половине пути, вы замечаете, что тропинка заканчивается и начинается дорога, вы решаете продолжать идти до данной дороге" + Style.RESET_ALL)
        Go_road()
    def Go_road():
        print(Fore.CYAN + "Через некоторое время, вы видите большие здания, которые вас особо не впечатлили, ибо на своей планете вы видели вещи намного круче, чем то, что видите сейчас.")
        print(Fore.CYAN + "В городе вы замечаете прилавок, за которым стоит мужчина и кричит, что готов сыграть в игру")
        print(Fore.CYAN + "Также вы видите темный переулок")
        print(Fore.CYAN + "Пора выбрать действие:)))\n\tПодойти к мужчине\n\tПойти в тёмный переулок\n\tОсмотреться")
        while True:
            match user_txt():
                case "Подойти к мужчине":
                    Go_man()
                    break
                case "Пойти в темный переулок":
                    Go_dark()
                    break
                case "Осмотреться":
                    print("Вы ничего нового не заметили.")
                    repeat_man_goman_godark()
                case "Инвентарь":
                    inventory_show("Инвентарь")
                case _:
                    nach_txt(), printd(
                        Style.RESET_ALL + "\tНе... Чёт не то.\n")
    print(Fore.CYAN + "Вы выбрали характеристики мужчины: " + Style.RESET_ALL, man)
    if inventory_return() == []:
        inventory_add("Что-то похожее на нож, но в бою бесполезное")
        first_open_inventory()
    else:
        inventory_add("Что-то похожее на нож, но в бою бесполезное")
    print("\n\t\t\t\t\t\t\t\t" + Fore.CYAN + "Вы получити новый предмет!")
    nach_txt(), print("\tТак, я готов начать.\n")
    print(Fore.CYAN + "\t\t\t\t\t\t\t\tВы осматриваете местность в которой очутились. Перед вами раскинуля большой лес и тропинка, которая ведёт в самую гущу данного леса\n\t\t\t\t\t\t\t\tСправа вы видите асфальтурованную дорогу.\n")
    print(Fore.CYAN + "Выберете действие:\n\tОсмотреться\n\tПойти в лес\n\tПойти по асфальтированной дороге")
    while True:
        match user_txt():
            case "Осмотреться":
                Osmotr()
                break
            case "Пойти в лес":
                Go_forest()
                break
            case "Пойти по асфальтированной дороге":
                Go_road()
                break
            case "Инвентарь":
                inventory_show("Инвентарь")
            case _:
                nach_txt(), printd(Style.RESET_ALL + "\tЗачем это делать? (ты сказал шо ты шаришь в этой теме...)\n")
def choose_of_character():
    print(Fore.CYAN +"Перед вами стоит выбор. Играть за женщину или мужчину. Ниже представлены описания и возможности того или иного пола: "+ Style.RESET_ALL)
    print("Мужчина: ", man)
    print("Женщина: ", woman)
    while True:
        match user_txt():
            case "Мужчина":
                man_game()
                break
            case "Женщина":
                woman_game()
                break
            case "Инвентарь":
                inventory_show("Инвентарь")
            case _:
                nach_txt(), printd(Style.RESET_ALL + "\tПо-моему... Я не могу так сделать\n")
start()
print(Fore.RED + "Неизвестный:"), printd(Style.RESET_ALL + "\t- Ты всё понял? Ты будешь отправлен туда совсем один.\n")
print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Да, вроде ничего сложного. Мне нужно будет просто записывать свои мысли?\n")
print(Fore.RED + "Неизвестный:"), printd(Style.RESET_ALL + "\t- Не только, постарайся поконтактировать c этим миром. На сколько я знаю, местные не слишком агрессивные... \n")
print(Fore.GREEN + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tВы:"), printd(Style.RESET_ALL + "\t- Хорошо, по ходу разберусь. Сколько до запуска? \n")
print(Fore.RED + "Неизвестный:"), printd(Style.RESET_ALL + "\t- Судя по показаниям приборов мы готовы. Можем начинать. Напиши: \"Готов\" если ты не против начать или \"Я не готов\" если ты ещё не готов преступить к путешествию\n")
beginning()






