def isNum(input):
    try:
        float(input)
    except ValueError:
        return False
    return True


def __getPrio(char):
    priority = {
        "p0": "(",
        "p1": "+-)",
        "p2": "*/%",
        "p3": "^"
    }
    if char in priority['p0']:
        return 0
    elif char in priority['p1']:
        return 1
    elif char in priority['p2']:
        return 2
    else:
        return 3


def __compPrio(new, topstack):
    """returns true if prio of new is bigger than prio of topstack"""
    return __getPrio(new) > __getPrio(topstack[len(topstack) - 1])


def convertToRNP(inStr):
    """convert string to rnp stack"""
    temp = inStr.split(" ")
    tempStack = []
    rpnStack = []
    for elem in temp:
        if elem.isdigit():
            rpnStack.append(elem)
        elif elem == '(':
            tempStack.append(elem)
        elif elem == ')':
            elem = tempStack.pop()
            while len(tempStack) != 0 and elem != '(':
                rpnStack.append(elem)
                elem = tempStack.pop()
        else:
            if len(tempStack) == 0 or __compPrio(elem, tempStack):
                tempStack.append(elem)
            else:
                while len(tempStack) != 0 and not __compPrio(elem, tempStack):
                    rpnStack.append(tempStack.pop())
                tempStack.append(elem)
    while len(tempStack) != 0:
        rpnStack.append(tempStack.pop())
    return ' '.join(rpnStack)


def evaluateRNP(inStr):
    """gets string in rnp and calculates result, then returns it"""
    inStr = inStr.split(" ")
    tempStack = []
    for elem in inStr:
        if isNum(elem):
            tempStack.append(elem)
        else:
            a = tempStack.pop()
            b = tempStack.pop()
            elem = elem if elem != '^' else '**'
            equation = str(b) + elem + str(a)
            equation = eval(equation)
            tempStack.append(equation)
    return tempStack[0]
