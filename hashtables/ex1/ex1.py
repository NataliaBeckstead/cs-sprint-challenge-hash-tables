def get_indices_of_item_weights(weights, length, limit):
    lookup_table = {}
    for i in range(0, length):
        lookup_table[weights[i]] = i
    for i in weights:
        if limit - i in lookup_table:
            result = [lookup_table[limit - i], weights.index(i)]
            result.sort(reverse=True)
            return result

    return None