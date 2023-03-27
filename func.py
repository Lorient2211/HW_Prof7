from stek_class import Stekk

def balanced(string):
    qwe = Stekk()
    conect_dict = {'(':'a', '[':'b', '{':'c', ')':'a', ']':'b', '}':'c'} 
    oc_dict = {'open':['(','[','{'], 'close':[')',']','}']}
    for ind, el in enumerate(string):
        if el in oc_dict['open']:
            qwe.meaning.append(el)
        else:
            if qwe.is_empty():
                return 'Несбалансированная'
            if conect_dict[qwe.meaning[-1]] != conect_dict[string[ind]]:
                return 'Несбалансированная'
            else:
                qwe.meaning.pop()

    if qwe.is_empty():
        return 'Сбалансированная'
    else:
        return 'Несбалансированная'








