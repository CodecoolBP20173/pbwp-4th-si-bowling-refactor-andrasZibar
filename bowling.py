def getScoreFor(game):
    result = 0
    frame = 1
    isFirstRoll = True
    for i in range(len(game)):
        currentRoll = game[i]
        isSpare = currentRoll == '/'
        isStrike = currentRoll.upper() == 'X'
        if isSpare:
            result += 10 - last
        else:
            result += getPointsFor(currentRoll)
        if frame < 10 and getPointsFor(currentRoll) == 10:
            result = getBonusPoints(game, i, result)
        last = getPointsFor(currentRoll)
        if not isFirstRoll:
            frame += 1
        isFirstRoll = checkIfFirstRoll(isFirstRoll)
        if isStrike:
            isFirstRoll = True
            frame += 1
    return result

def checkIfFirstRoll(isFirstRoll):
    if isFirstRoll:
        isFirstRoll = False
    else:
        isFirstRoll = True
    return isFirstRoll

def getBonusPoints(game, i, result):
    if game[i] == '/':
        result += getPointsFor(game[i + 1])
    elif game[i] == 'X' or game[i] == 'x':
        result += getPointsFor(game[i + 1])
        if game[i + 2] == '/':
            result += 10 - getPointsFor(game[i + 1])
        else:
            result += getPointsFor(game[i + 2])
    return result


def getPointsFor(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
