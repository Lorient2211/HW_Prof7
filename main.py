from stek_class import Stekk
from func import balanced


if __name__ == '__main__':
    qwer = Stekk()
    qwer.meaning = [1,2,3,4,5]
    qwer.push(0)


    print(qwer.meaning)
    print(qwer.is_empty())
    print(qwer.peek())
    print(qwer.size())
    print(qwer.pop())
    print(qwer.meaning)

    print(balanced(r'([)]'))
    print(balanced(r'{{[(])]}}'))
    print(balanced(r'[[{())}]'))
    print(balanced(r'[([])((([[[]]])))]{()}'))






