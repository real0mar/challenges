from math import gcd


def find_triplets(max_length: int) -> int:
    num_valid = 0
    m = 2
    while 2 * m * m < max_length:
        n = 1
        while n < m:
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                sum_abc = a + b + c

                diff = abs(b - a)

                if diff > 0 and c % diff == 0:
                    num_valid += max_length // sum_abc
            n += 1
        m += 1
    return num_valid


# Given perimeter limit
perimeter_limit = 100_000_000
valid_triples_count_fixed = find_triplets(perimeter_limit)

print(valid_triples_count_fixed)
