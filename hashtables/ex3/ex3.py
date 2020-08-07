def intersection(arrays):
    
    num_hash = {}

    for i in arrays[0]:
        num_hash[i] = 0

    for i in range(1, len(arrays)):
        for num in arrays[i]:
            if num in num_hash:
                if num_hash[num] == i - 1:
                    num_hash[num] = i
                else:
                    del num_hash[num]

    result = []
    for item in num_hash.items():
        if item[1] == len(arrays) - 1:
            result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

