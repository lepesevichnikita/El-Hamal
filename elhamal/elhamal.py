import math
import random

class ElHamal:

    def __init__(self, keys=None):
        random.seed()

    @staticmethod
    def encrypt(text, public_key):
        result = list(
            map(lambda letter: ElHamal.encrypt_symbol(letter, public_key),
                text)
        )
        return result

    @staticmethod
    def decrypt(cryptogramm, keys):
        result = ''.join(
            map(lambda crypto_pare: ElHamal.decrypt_symbol(crypto_pare, keys),
                cryptogramm)
        )
        return result

    @staticmethod
    def encrypt_symbol(sym, public_key):
        p, g, y = public_key
        num = ord(sym)
        k = ElHamal.gen_k(p)
        a = pow(g, k, p)
        b = (pow(y, k, p) * num) % p
        result = [a, b]
        return result

    @staticmethod
    def decrypt_symbol(crypto_sym, keys):
        p, g, y, x = keys
        a, b = crypto_sym
        num = (pow(pow(a, x, p), (p-2), p) * b) % p
        result = chr(num)
        return result


    def gen_keys(self):
        p = random.choice(self.prime_numbers())
        g = self.find_primitive_root_by_mod(p)
        x = random.choice(range(2, p - 1))
        y = pow(g, x, p)
        return [p, g, y, x]

    @staticmethod
    def gen_k(p):
        result = random.randint(2, p-1)
        while math.gcd(result, p-1) != 1:
            result = random.randint(2, p-1)
        return result

    @staticmethod
    def prime_numbers(end=2 ** 16, start=2 ** 14) -> list:
        last_number = end + 1
        end_of_range_for_filter = int(math.sqrt(last_number))
        result = list(range(3, last_number, 2))
        for x in range(start, end_of_range_for_filter, 2):
            result = list(filter(lambda a: a == x or a % x != 0, result))
        result = list(filter(lambda x: x >= start, result))
        return result

    @staticmethod
    def mod_pow(number, power, mod):
        result = 1
        while power > 0:
            if power % 2 == 0:
                result = (result**number) % mod
                power /= 2
            else:
                result = (result*number) % mod
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
        result = list(filter(lambda x: number%x == 0, range(2, number+1)))
        for x in result:
            result = list(filter(lambda k: x==k or k%x!=0, result))
        return result

    @staticmethod
    def find_all_primitive_roots(mod):
        phi = ElHamal.euler_function(mod)
        factors = ElHamal.factorize(phi)
        result = []
        for posible_root in range(2, mod):
            for factor in factors:
                power = int(phi/factor)
                mod_pow = pow(posible_root, power, mod)
                if mod_pow != 1:
                    result.append(posible_root)
                    break
        return result

    @staticmethod
    def find_primitive_root_by_mod(mod):
        result = random.choice(ElHamal.find_all_primitive_roots(mod))
        return result
