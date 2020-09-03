def has_negatives(a):
    num_hash = {}
    for i in a:
        if i < 0:
            num_hash[i] = True

    result = []
    for i in a:
        if -i in num_hash:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
