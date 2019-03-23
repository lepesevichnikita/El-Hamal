import math
import random
from itertools import count, islice


class ElHamal:

    def __init__(self):
        random.seed()

    @staticmethod
    def encrypt(text, public_key) -> list:
        result = list(
            map(lambda letter: ElHamal.encrypt_symbol(letter, public_key),
                text)
        )
        return result

    @staticmethod
    def cryptogram_to_str(cryptogram) -> str:
        result = ' '.join(
            [str(letter) for bigram in cryptogram for letter in bigram])
        return result

    @staticmethod
    def cryptogram_from_string(cryptogram_str) -> list:
        result = [int(x) for x in cryptogram_str.split(' ')]
        result = [result[i:i+2] for i in range(0, len(result)-2, 2)]
        result = list(result)
        return result

    @staticmethod
    def decrypt(cryptogram, keys) -> str:
        result = ''.join(
            map(lambda crypto_pare: ElHamal.decrypt_symbol(crypto_pare, keys),
                cryptogram)
        )
        return result

    @staticmethod
    def encrypt_symbol(sym, public_key) -> list:
        p, g, y = public_key
        num = ord(sym)
        k = ElHamal.gen_k(p)
        a = pow(g, k, p)
        b = (pow(y, k, p) * num) % p
        result = [a, b]
        return result

    @staticmethod
    def decrypt_symbol(digram, keys) -> str:
        p, g, y, x = keys
        a, b = digram
        num = (pow(pow(a, x, p), (p - 2), p) * b) % p
        result = chr(num)
        return result

    def gen_keys(self):
        p = random.choice(self.prime_numbers())
        g = self.get_random_primitive_root_by_mod(p)
        x = random.choice(range(2, p - 1))
        y = pow(g, x, p)
        while y == 1:
            x = random.choice(range(2, p-1))
            y = pow(g, x, p)
        return [p, g, y, x]

    @staticmethod
    def is_prime(num) -> bool:
        result = num > 1
        result &= all(
            num % i for i in islice(count(2), int(math.sqrt(num) - 1)))
        return result

    @staticmethod
    def fast_pow(num, power, mod):
        result = 1
        while power > 0:
            if power % 2 == 1:
                result = (result * num) % mod
            power = power / 2
            num = (num ** 2) % mod
        return result

    @staticmethod
    def gen_k(p):
        result = random.randint(2, p - 1)
        while math.gcd(result, p - 1) != 1:
            result = random.randint(2, p - 1)
        return result

    @staticmethod
    def prime_numbers(end=2 ** 16, start=2 ** 14) -> list:
        last_number = end + 1
        end_of_range_for_filter = int(math.sqrt(last_number))
        result = [2] + list(range(3, last_number, 2))
        for x in range(3, end_of_range_for_filter, 2):
            result = list(filter(lambda a: a == x or a % x != 0, result))
        result = list(filter(lambda x: x >= start, result))
        return result

    @staticmethod
    def mod_pow(number, power, mod):
        result = 1
        while power > 0:
            if power % 2 == 0:
                result = (result ** number) % mod
                power /= 2
            else:
                result = (result * number) % mod
                power -= 1
        return result

    @staticmethod
    def is_mutually_prime(a, b):
        return math.gcd(a, b) == 1 and (a != 1 or b != 1)

    @staticmethod
    def euler_function(n):
        result = list(filter(lambda x: ElHamal.is_mutually_prime(x, n),
                             range(n)))
        return len(result)

    @staticmethod
    def factorize(number):
        result = list(filter(lambda x: number % x == 0, range(2, number + 1)))
        for x in result:
            result = list(filter(lambda k: x == k or k % x != 0, result))
        return result

    @staticmethod
    def is_primitive_root_by_mod(possible_primitive_root, mod):
        result = True
        phi = ElHamal.euler_function(mod)
        factors = ElHamal.factorize(phi)
        for factor in factors:
            power = int(phi / factor)
            mod_pow = pow(possible_primitive_root, power, mod)
            if mod_pow == 1:
                result = False
                break
        return result

    @staticmethod
    def find_all_primitive_roots(mod):
        result = []
        phi = ElHamal.euler_function(mod)
        factors = ElHamal.factorize(phi)
        for possible_primitive_root in range(2, mod):
            for factor in factors: power = int(phi / factor)
            mod_pow = pow(possible_primitive_root, power, mod)
            if mod_pow == 1:
                result.append(possible_primitive_root)
                break
        return result

    @staticmethod
    def get_random_primitive_root_by_mod(mod):
        result = random.choice(ElHamal.find_all_primitive_roots(mod))
        return result
