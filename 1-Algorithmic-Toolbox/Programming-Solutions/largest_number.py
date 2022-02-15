#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    for x in a:
        res += x
    return res

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))
    


def isBetter(number, max_num):
    if (str(number) + str(max_num)) > (str(max_num) + str(number)):
        return number
    else:
        return max_num


def largest_number(numbers):
    numbers = list(map(str, numbers))
    max_num, salary = 0, []

    while len(numbers) > 0:
        for i in range(len(numbers)):
            max_num = numbers.index(isBetter(numbers[i], numbers[max_num]))

        salary.append(numbers[max_num])
        numbers.pop(max_num)
        max_num = 0

    max_salary = int("".join(salary))

    return max_salary


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
