# Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1. Добавьте игру против бота
# 2. Подумайте как наделить бота 'интеллектом'
# Оба задания обязательны

import random
import sys

candies = 150
max_candies_in_round = 28
coin_predict = int(input('Определим очередность. 1 или 0? : '))
coin = random.randint(0, 1)
players_turn= True
comp_turn = True
players_candies = 0
comp_candies = 0
first_turn_fail = False

if coin_predict == coin:
    players_candies = int(input('Угадал! Ходи первым! Возьми от 1 до 28 конфет: '))
    players_turn = False
    candies -= players_candies
    
else:
    print('Не повезло тебе, я хожу первым!')
    comp_candies = candies % (max_candies_in_round + 1)
    
    if comp_candies == 0:
        comp_candies = 1
        first_turn_fail = True
        
    comp_turn = False
    candies -= comp_candies
    print(f'Я взял {comp_candies} конфет! Осталось {candies}! Твоя очередь ходить!')
    
while candies > 0:
    if players_turn:
        players_candies = int(input('Возьми от 1 до 28 конфет: '))
        candies -= players_candies
        if candies <= 0:
            sys.exit('Поздравляю! Ты выиграл! Все конфеты твои!')
            
        players_turn = False
        comp_turn = True
        print(f'Осталось {candies} конфет! Моя очередь ходить!')
    
    else:
        if first_turn_fail:
            comp_candies = max_candies_in_round - players_candies
            candies -= comp_candies
            players_turn = True
            comp_turn = False
            print(f'Я взял {comp_candies} конфет! Осталось {candies}! Твоя очередь ходить!')
            
        elif (candies > (max_candies_in_round * 2 )) or (candies == max_candies_in_round + 1):
            comp_candies = max_candies_in_round + 1 - players_candies
            candies -= comp_candies
            players_turn = True
            comp_turn = False
            print(f'Я взял {comp_candies} конфет! Осталось {candies}! Твоя очередь ходить!')
            
        elif (max_candies_in_round + 1) < candies < (max_candies_in_round * 2):
            comp_candies = candies - max_candies_in_round - 1
            candies -= comp_candies
            players_turn = True
            comp_turn = False
            print(f'Я взял {comp_candies} конфет! Осталось {candies}! Твоя очередь ходить!')
            
        else:
            sys.exit(f'Я взял {candies} конфет! Конфет не осталось! Я выиграл!')