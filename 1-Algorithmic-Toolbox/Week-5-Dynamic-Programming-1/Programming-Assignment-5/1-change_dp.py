# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    dp = [m + 1] * (m + 1)
    dp[0] = 0

    for a in range(1, m + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[m]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
