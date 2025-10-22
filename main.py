def play(hod):
    while hod != 10:
        if hod == 0:
            print('Добро пожаловать в игру! Уважаемые игроки, введите свои имена в систему через пробел, иначе просто нажмите клавишу Enter')
            names = str(input()).split(' ')
            if names[0] != '':
                name[0],name[1] = names[1],names[0]
            print(f'Уважаемые {name[1]} и {name[0]}, перед тем, как придступить к игре, хотелось бы вам напомнить правила:')
            print(print_play_game())
        else:
            print(f'{name[0]}, делайте свой {hod_pl[int((hod - 1)%2)]} ход!  Укажите номер ячейки, в которую вы поставите {hod_zn[hod%2]}')
            place[int(input())] = hod_zn[int(hod%2)]
            print_place()
            if if_win() == 1:
                print(f'{name[hod%2]}, поздравляю, вы победили!')
                break

        hod += 1
