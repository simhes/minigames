import numpy as np

def menu( preSet ):
    print('<====================>')
    print(' |    MASTER MIND   |')
    print('<====================>')

    if preSet:
        userName = 'TESTUSER'
        count = '4'
        print(f'User name: {userName}')
        print(f'Count: {count}')
    else:
        userName = input('User name: ')
        while True:
            count = input('Unkonw (req. 4-5): ')
            if count.isnumeric():
                break

    return (userName, count)

def startScreen(count):
    print(' |                  |')
    print(' |                  |')
    print(f'<-{'--'*count}-->')
    print(f' |{' #'*count}')

def printxo(x, o, c):
    print(f'{' x'*x}{' o'*o}{'  '*c}')

def game( rounds, anser, count ) -> bool:

    def validation( values, anser, count) -> bool:
        error = False
        if not( len(values) == count ):
            error = True
            print('len_error')
        return error

    def score( values, anser, count ) -> tuple:
        o = 0
        x = 0
        valuesUnik = set(values)
        for c in valuesUnik:
            # antal korekta fel plats
            cInAnser = anser.count( c )
            if cInAnser > values.count( c ):
                cKorrect = values.count( c )
            else:
                cKorrect = cInAnser
            o = o + cKorrect
        for c in range( count ):
            if anser[c] == values[c]:
                x = x + 1
        return (x, o - x)

    while True:
        print(' | ', end='')
        userTry = input()
        print(' |', end='')
        values = userTry.split(' ')
        error = validation( values, anser, count )
        if error == False:
            break

    userScore = score( values, anser, count )
    printxo(userScore[0], userScore[1], count)

    rounds.append((values, userScore))
    if userScore[0] == count:
        # victory
        return True
    else:
        # not finnishd
        return False

def main():
    rounds = [] # main list, off ['userInput', 'userFeedbak']
    anser = 'ABAA'

    (UserName, strCount) = menu( True )
    count = int(strCount)

    print('Chars: ABCDEFG (A-G)')

    print(f'Anser: {anser}')
    startScreen(count)



    while not(game( rounds, anser, count )):
        pass

    print(f'Victory on turn {len(rounds)}')

    print(rounds)







main()
