# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product

def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    max_index1 = -1
    n = len(numbers)
    for i in range(n):
        if max_index1 == -1 or (numbers[i] > numbers[max_index1]):
            max_index1 = i
    
    max_index2 = -1
    for i in range(n):
        if (i != max_index1) and (max_index2 == -1 or numbers[i] > numbers[max_index2]):
            max_index2 = i
    
    return numbers[max_index1] * numbers[max_index2]

    ## Optimized solution
    # numbers.sort()
    # return numbers[-1]*numbers[-2]

if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))

