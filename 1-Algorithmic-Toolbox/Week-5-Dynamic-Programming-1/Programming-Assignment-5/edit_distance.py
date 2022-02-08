# Uses python3
def edit_distance(s, t):
    #write your code here
    len_s = len(s) + 1
    len_t = len(t) + 1

    # Create a distance matrix and write in initial values.
    d = [[x] + [0] * (len_t - 1) for x in range(len_s)]
    d[0] = [x for x in range(len_t)]

    for i in range(1, len_s):
        for j in range(1, len_t):

            # Levenshtein distance calculation.
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1

    # The last element of the matrix is edit distance metric.
    return d[-1][-1]
    

if __name__ == "__main__":
    print(edit_distance(input(), input()))
