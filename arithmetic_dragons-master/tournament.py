# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *


def cheat(x):
    if x == 'Jopkins':
        start_game_plus()
    else:
        pass




def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = input(message)
        except ValueError:
            answer = int(answer)
    return answer


def troll_tournament(hero, troll_list):
    for troll in troll_list:
        print('Вышел', troll._color,'!')
        while troll.is_alive() and hero.is_alive():
            print('Вопрос:', troll.question())
            answer = annoying_input_int('Ответ:')

            if troll.check_answer(answer):
                hero.attack(troll)
                print('Верно! \n** тролль кричит от боли **')
            else:
                troll.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
                if hero.is_alive() != True:
                    print('К сожалению, Вы проиграли...')
                    print('Хотите начать заново?')
                    if input() == 'да':
                        start_game()
        if troll.is_alive():
            break
        print(troll._color, 'повержен!\n')
        if hero.is_alive():
            print('Поздравляем! Вы победили!')
            hero.exp_gain(troll)
            print('Ваш накопленный опыт:', hero._experience)
            if hero.is_lvl_up() == True:
                hero.lvl_up()
                print('Поздравляем! Новый уровень, ваши характеристики возросли')
                hero.exp_down()    


def game_tournament(hero, dragon_list):
    
    for dragon in dragon_list:
        print('Вышел', dragon._color,'!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
                if hero.is_alive() != True:
                    print('К сожалению, Вы проиграли...')
                    print('Хотите начать заново?')
                    if input() == 'да':
                        start_game()
        if dragon.is_alive():
            break
        print(dragon._color, 'повержен!\n')
        if hero.is_alive():
            print('Поздравляем! Вы победили!')
            hero.exp_gain(dragon)
            print('Ваш накопленный опыт:', hero._experience)
            if hero.is_lvl_up() == True:
                hero.lvl_up()
                print('Поздравляем! Новый уровень, ваши характеристики возросли')
                hero.exp_down()

def start_game_plus():

    try:
        
        print('вы ввели чит код, представтесь')
        hero = Hero(input())
        troll_number = 3
        troll_list = generate_troll_list(troll_number)
        assert(len(troll_list) == 3)
        print('У Вас на пути', troll_number, 'троллей!')
        troll_tournament(hero, troll_list)


    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами и не только!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())
        cheat(hero.name)
        troll_number = 3
        troll_list = generate_troll_list(troll_number)
        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)
        assert(len(troll_list) == 3)
        print('У Вас на пути', troll_number, 'троллей!')
        troll_tournament(hero, troll_list)


    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
