def num_of_divisor(num, div):
    count = 0
    while num % div == 0:
        count += 1
        num /= div
    return count


if __name__ == '__main__':
    n, m = input().strip("\n\t\r ").split(" ")
    n = int(n)
    m = int(m)
    arr = input().strip("\n\t\r ").split(" ")
    for it in range(0, n):
        arr[it] = int(arr[it])
    divisors = {arr[0]: [num_of_divisor(arr[0], 2), num_of_divisor(arr[0], 3),
                         num_of_divisor(arr[0], 5), num_of_divisor(arr[0], 7)]}

    for it in range(1, n):
        prev_count = divisors[arr[it - 1]]
        new_count = [num_of_divisor(arr[it], 2) + prev_count[0], num_of_divisor(arr[it], 3) + prev_count[1],
                     num_of_divisor(arr[it], 5) + prev_count[2], num_of_divisor(arr[it], 7) + prev_count[3]]
        divisors[arr[it]] = new_count

    print(divisors)

    for it in range(0, m):
        l, r = input().strip("\n\t\r ").split(" ")
        l = int(l) - 2
        r = int(r) - 1
        r_count = divisors[arr[r]]
        l_count = [0, 0, 0, 0] if l == -1 else divisors[arr[l]]
        res = 1
        for jt in range(0, 4):
            res = (res * (r_count[jt] - l_count[jt] + 1)) % 1000000007
        print(res)
