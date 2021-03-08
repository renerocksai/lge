#!/usr/bin/env python
import random

vowels = ['A', 'E', 'I', 'O', 'U']
consonants = [chr(c) for c in range(65, 65+26) if chr(c) not in vowels]

def gen_name(length=8):
    ret = []

    order = [0, 1]
    random.shuffle(order)

    for i in range(length):
        letters = [random.choice(consonants), random.choice(vowels)]
        for o in order:
            ret.append(letters[o])
    return ''.join(ret)


if __name__ == '__main__':
    print('username ; points')
    for _ in range(20):
        print(f'{gen_name(random.randint(2,6)).lower()}{random.randint(1,999)};{random.randint(0, 10000)}')

