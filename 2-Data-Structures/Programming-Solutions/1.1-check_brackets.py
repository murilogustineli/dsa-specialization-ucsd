# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            pass


def checkBracket(string):
    dic = {'(': ')', '[': ']', '{': '}'}
    stack = []

    if len(string) <= 1:
        return 1

    for i, char in enumerate(string):
        if char in dic.keys():
            stack.append(char)
        elif char not in dic.values():
            continue
        else:
            if len(stack) < 1:
                return string.index(char)+1
            top = stack.pop()
            if dic[top] != char:
                return i+1
    if len(stack) == 0:
        return 'Success'
    else:
        return string.index(top) + 1


def main():
    text = input()
    mismatch = checkBracket(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
