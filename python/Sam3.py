def build_counts_dict(s):
    counts = {}
    i = 0
    while i < len(s):
        ch = s[i]
        if '0' <= ch <= '9':
            key = ord(ch) - ord('0')
            if key in counts:
                counts[key] = counts[key] + 1
            else:
                counts[key] = 1
        i += 1
    return counts


def top_3_most_frequent(s):
    counts = build_counts_dict(s)
    if not counts:
        return {}

    pairs = []
    for k in counts:
        pairs.append((k, counts[k]))

    top_pairs = []
    temp_pairs = list(pairs)
    take = 3
    while take > 0 and temp_pairs:
        max_idx = 0
        j = 1
        while j < len(temp_pairs):
            # сравним частоты
            if temp_pairs[j][1] > temp_pairs[max_idx][1]:
                max_idx = j
            elif temp_pairs[j][1] == temp_pairs[max_idx][1]:
                if temp_pairs[j][0] < temp_pairs[max_idx][0]:
                    max_idx = j
            j += 1
        top_pairs.append(temp_pairs[max_idx])
        temp_pairs.pop(max_idx)
        take -= 1

    i = 0
    while i < len(top_pairs):
        min_idx = i
        j = i + 1
        while j < len(top_pairs):
            if top_pairs[j][0] < top_pairs[min_idx][0]:
                min_idx = j
            j += 1
        if min_idx != i:
            tmp = top_pairs[i]
            top_pairs[i] = top_pairs[min_idx]
            top_pairs[min_idx] = tmp
        i += 1

    result = {}
    i = 0
    while i < len(top_pairs):
        k, cnt = top_pairs[i]
        result[k] = cnt
        i += 1

    return result

if __name__ == '__main__':
    s = "012345678901234567890123456789012345"
    s2 = "1112233344555599999000000123456789012345"
    counts_all = build_counts_dict(s2)
    top3 = top_3_most_frequent(s2)
    print("Полный словарь частот:", counts_all)
    print("Топ-3 самых частых (словарь):", top3)