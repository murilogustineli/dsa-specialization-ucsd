# Uses python3
import sys

def get_change(m):
    #write your code here
    return m

# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))


def money_change(money):
    assert 0 <= money <= 10 ** 3
    # type here
    coin = [10, 5, 1]
    c = coin[0]
    change = 0

    while money > 0:
        if money < c:
            for i in range(len(coin)):
                if coin[i] <= money:
                    c = coin[i]
                    break
        else:
            money = money - c
            change += 1

    return change


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
    