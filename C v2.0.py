def check(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        elif s[i] == '|':
            if len(stack) != 0 and stack[-1] == '(':
                stack.append('|')
            else:
                return [False, False]
        elif s[i] == ')':
            if len(stack) < 2 or stack[-1] != '|' or stack[-2] != '(':
                return [False, False]
            else:
                stack.pop()
                stack.pop()
    if len(stack) != 0:
        return [False, True]
    return [True, True]

def expected_check(s, i):
    expected = []
    for symbol in ['(', '|', ')']:
        s_new = s[:i] + symbol
        if check(s_new)[1]:
            expected.append(symbol)
    s_new = s[:i]
    if check(s_new)[0]:
        expected.append('END')
    return expected

def algorithm(s):
    stack = []
    length = len(s)
    for i in range(len(s)):
        position = i
        found = s[i]
        if s[i] == '(':
            stack.append('(')
        elif s[i] == '|':
            if len(stack) != 0 and stack[-1] == '(':
                stack.append('|')
            else:
                return False, [position + 1, expected_check(s, i), found]
        elif s[i] == ')':
            if len(stack) < 2 or stack[-1] != '|' or stack[-2] != '(':
                return False, [position + 1, expected_check(s, i), found]
            else:
                stack.pop()
                stack.pop()
    if len(stack) != 0:
        position = length
        found = 'END'
        return False, [position + 1, expected_check(s, position), found]
    return True, [length]

def printer(flag, mass):
    if flag:
        print('correct, length =', mass[0])
    else:
        print('at position ', mass[0], ': expected ', sep = '', end = '')
        if len(mass[1]) != 0:
            for i in range(len(mass[1]) - 1):
                print(mass[1][i], ' or ', sep = '', end = '')
            print(mass[1][-1],', found ', mass[2], sep = '', end = '\n')
        else:
            print(', found ', mass[2], sep = '', end = '\n')

def main(s):
    flag, mass = algorithm(s)
    printer(flag, mass)


s = input()
main(s)


