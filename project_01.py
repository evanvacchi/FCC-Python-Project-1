def arithmetic_arranger(lst, solve = False):
    lst1 = list()
    lst2 = list()
    lst3 = list()
    lst4 = list()
    biglst = list()
    for x in lst:
        nospace = x.replace(' ', '') #replaces spaces with no spaces
        if len(lst) > 5:
            return 'Error: Too many problems.'
        if '/' in x:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if '*' in x:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if len(nospace) == 0:
            return 'Error: Numbers must only contain digits.'
        if x is None:
            return 'Error: Numbers must only contain digits.'
        if '-' in x:
            nospace = nospace.split('-')
            try:
                first = int(nospace[0]) #first number
                second = int(nospace[1]) #second number
            except:
                return 'Error: Numbers must only contain digits.'
            if len(nospace[0]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            if len(nospace[1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            subtraction = first - second
            pieceone = str(first)
            piecetwo = str(second)
            piecethree = str(subtraction)
            dash = '------'
            minus = '-'
            if len(pieceone) >= len(piecetwo) and len(piecethree):
                newdash = dash[0:len(pieceone)+2].rjust(0)
                if len(pieceone) - len(piecetwo) == 0:
                    pieceone = pieceone.rjust(len(pieceone)+2).rstrip()
                    piecetwo = (minus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                elif len(pieceone) - len(piecetwo) == 1:
                    pieceone = pieceone.rjust(len(pieceone)+2).rstrip()
                    piecetwo = (minus + '  ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                elif len(pieceone) - len(piecetwo) == 2:
                    pieceone = pieceone.rjust(len(pieceone)+2).rstrip()
                    piecetwo = (minus + '   ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                else:
                    pieceone = pieceone.rjust(len(pieceone)+2).rstrip()
                    piecetwo = (minus + '    ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))

            elif len(piecetwo) >= len(pieceone) and len(piecethree):
                newdash = dash[0:len(piecetwo)+2].rjust(0)
                if len(piecetwo) - len(pieceone) == 0:
                    pieceone = pieceone.rjust(len(pieceone)+2).rstrip()
                    piecetwo = (minus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                elif len(piecetwo) - len(pieceone) == 1:
                    pieceone = pieceone.rjust(len(pieceone)+3).rstrip()
                    piecetwo = (minus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                elif len(piecetwo) - len(pieceone) == 2:
                    pieceone = pieceone.rjust(len(pieceone)+4).rstrip()
                    piecetwo = (minus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                else:
                    pieceone = pieceone.rjust(len(pieceone)+5).rstrip()
                    piecetwo = (minus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))

            lst1.append(pieceone.rstrip())
            lst2.append(piecetwo.rstrip())
            lst3.append(newdash)
            lst4.append(piecethree.rstrip())

        elif '+' in x:
            nospace = nospace.split('+')
            try:
                first = int(nospace[0])
                second = int(nospace[1])
            except:
                return 'Error: Numbers must only contain digits.'
            if len(nospace[0]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            if len(nospace[1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            addition = first + second
            pieceone = str(first)
            piecetwo = str(second)
            piecethree = str(addition)
            dash = '------'
            plus = '+'
            if len(pieceone) >= len(piecetwo) and len(piecethree):
                newdash = dash[0:len(pieceone)+2].rjust(0)
                if len(pieceone) - len(piecetwo) == 0:
                    pieceone = (pieceone.rjust(len(pieceone)+2)).rstrip()
                    piecetwo = (plus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                elif len(pieceone) - len(piecetwo) == 1:
                    pieceone = (pieceone.rjust(len(pieceone)+2)).rstrip()
                    piecetwo = (plus + '  ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                elif len(pieceone) - len(piecetwo) == 2:
                    pieceone = (pieceone.rjust(len(pieceone)+3)).rstrip()
                    piecetwo = (plus + '   ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                else:
                    pieceone = pieceone.rjust(len(pieceone)+4).rstrip()
                    piecetwo = (plus + '    ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))

            elif len(piecetwo) >= len(pieceone) and len(piecethree):
                newdash = dash[0:len(piecetwo)+2].rjust(0)
                if len(piecetwo) - len(pieceone) == 0:
                    pieceone = (pieceone.rjust(len(pieceone)+1)).rstrip()
                    piecetwo = (plus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                elif len(piecetwo) - len(pieceone) == 1:
                    pieceone = (pieceone.rjust(len(pieceone)+3)).rstrip()
                    piecetwo = (plus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                elif len(piecetwo) - len(pieceone) == 2:
                    pieceone = (pieceone.rjust(len(pieceone)+4)).rstrip()
                    piecetwo = (plus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))
                else:
                    pieceone = (pieceone.rjust(len(pieceone)+4)).rstrip()
                    piecetwo = (plus + ' ' + piecetwo).rjust(0).rstrip()
                    piecethree = piecethree.rjust(len(newdash))

            lst1.append(pieceone.rstrip())
            lst2.append(piecetwo.rstrip())
            lst3.append(newdash)
            lst4.append(piecethree.rstrip())

    fourspaces = '    '
    biglst.append(lst1)
    biglst.append(lst2)
    biglst.append(lst3)
    biglst.append(lst4)

    otherlst = list()
    otherlst.append(lst1)
    otherlst.append(lst2)
    otherlst.append(lst3)
    #print(biglst)

    if solve == True:
        solution = '    '.join(lst1) + '\n' + '    '.join(lst2) + '\n' + '    '.join(lst3) + '\n' + '    '.join(lst4)
        print(solution)
        return solution
    else:
        solution = '    '.join(lst1) + '\n' + '    '.join(lst2) + '\n' + '    '.join(lst3)
        return solution






lst = ['32 - 698', '598- 40']

arithmetic_arranger(lst, True)
