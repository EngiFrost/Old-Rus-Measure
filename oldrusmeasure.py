import math


def introduction(func):
    def wrapper():
        HELLO_MESSAGE = ("Привет!\n" +
                         "Это программа-конвертер, она поможет тебе перевести твои нищебродские миллиметры в царские сажени, аршины и вершки :)\n" +
                         "Просто вводи свои размеры и нажимай Enter, пока они не кончатся!\n" +
                         "ПРИМЕЧАНИЕ: если вершков получится не целое количество, значение будет округлено до целого вниз!\n" +
                         "Чтобы выйти из программы, в любой момент введи 'exit' или 'quit'.\n" +
                         "Чтобы начать конвертацию, введи 'start'")

        print(HELLO_MESSAGE)

        while True:
            instruction = input('\nКоманда: ')

            if instruction == 'start':
                func()
                return '\nПрограмма успешно завершена'
            elif instruction in ('exit', 'quit'):
                return '\nПрограмма успешно завершена'
            else:
                print('Твои команды мне неизвестны, попробуй еще раз')

    return wrapper


def wordforming(mmvalue, values):
    result = '    ' + str(mmvalue) + ' мм ='

    if values[0] != 0:
        if (values[0] % 10 in (2, 3, 4)) and (values[0] // 10 != 1):
            result += f' {values[0]} сажени'
        else:
            result += f' {values[0]} сажень'

    if values[1] != 0:
        if values[1] % 10 == 1:
            result += f' {values[1]} аршин'
        else:
            result += f' {values[1]} аршина'

    if not(((values[0] != 0) or (values[1] != 0)) and (values[2] == 0)):
        if (values[2] % 10 in (2, 3, 4)) and (values[2] // 10 != 1):
            result += f' {values[2]} вершка'
        elif (values[2] % 10 == 1) and (values[2] // 10 != 1):
            result += f' {values[2]} вершок'
        else:
            result += f' {values[2]} вершков'

    return result


@introduction
def oldRusConvert():
    SAGEN = 2111
    ARSHIN = 700
    VERSHOK = 44

    while True:
        mmvalue = input('\nКонвертируемый размер в миллиметрах: ')

        if mmvalue in ('quit', 'exit'):
            break
        elif mmvalue.isdigit():
            mmvalue = int(mmvalue)

            sagnum = mmvalue // SAGEN
            arnum = mmvalue % SAGEN // ARSHIN
            vernum = math.floor(mmvalue % SAGEN % ARSHIN / VERSHOK)

            print(wordforming(mmvalue, [sagnum, arnum, vernum]))
        else:
            print('Твои команды мне неизвестны, попробуй еще раз')
            continue

    return '\nПрограмма успешно завершена'


print(oldRusConvert())
