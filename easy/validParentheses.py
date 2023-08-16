# https://leetcode.com/problems/valid-parentheses/
    # recursion may work here.
    # but for lack of cleverness.

#  make sure these are opened and closed correctly.. '(){}[]'

def isValid(s):
    incoming = list(s)
    closer_converter = { ')' : '(', ']' : '[', '}' : '{'}
    starters = ['(', '[', '{']
    pile = []

    for parenthese in incoming:
        print(parenthese)
        if parenthese in starters:
            pile.append(parenthese)
        else:
            if pile:
                print("pile")
                if closer_converter[parenthese] == pile[-1]:
                    pile.pop()
                else:
                    return False
            else:
                return False
    if pile:
        return False
    else:
        return True


def main():
    False
    print(isValid('(])'))
    # True
    print(isValid("()[]{}"))
    # # True
    print(isValid('()[][][[]]')) # len = 10
    # # False
    # print(isValid('[])'))

if __name__ == '__main__':
    main()
