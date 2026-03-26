import math


def create_set_M(input_set):
    result = set()
    for value in input_set:
        if value >= 42:
            result.add(math.ceil(value / 2))
    return result


def create_set_o(input_set):
    result = set()
    for value in input_set:
        if value <= 25 or value > 35:
            result.add(value ** 4)
    return result


def create_set_Lambda(union_set):
    result = set()
    for value in union_set:
        if -57 <= value <= 40:
            result.add(3 * value)
    return result


def create_set_E(set_M):
    result = set()
    for value in set_M:
        if not (-19 <= value <= -16):
            result.add(math.ceil(value / 3))
    return result


def calculate_sum(set_E):
    total = 0
    for value in set_E:
        total += math.ceil(value / 2)
    return total


def calculate_product(set_Lambda):
    product = 1
    for value in set_Lambda:
        product *= math.ceil(value / 3)
    return product


def main(Ξ):
    M = create_set_M(Ξ)
    o = create_set_o(Ξ)
    
    X = o.union(M)
    
    Λ = create_set_Lambda(X)
    E = create_set_E(M)
    
    sum_part = calculate_sum(E)
    prod_part = calculate_product(Λ)
    
    return sum_part - prod_part
