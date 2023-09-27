from functools import reduce

def get(nested_dict: dict, key: str):
    return reduce(lambda d, k: d[k], key.split('.'), nested_dict)