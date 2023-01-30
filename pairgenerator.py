import random


def generate(low_limit, high_limit, number_of_pairs):
    pair_list = []
    while number_of_pairs:
        pair_list.append((random.uniform(low_limit, high_limit), random.uniform(low_limit, high_limit)))
        number_of_pairs -= 1
    return pair_list
