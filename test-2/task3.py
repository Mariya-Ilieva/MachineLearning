def sort_key(k):
    return k[1]

def occurs_most_often(s, n):
    elements = {}

    for el in s:
        if el.isalpha():
            el = el.lower()
            elements[el] = elements.get(el, 0) + 1

    output = sorted(elements.items(), key=sort_key, reverse=True)[:n]
    result = [x for x, _ in output]

    return result

print(occurs_most_often('Hello There', 3))
print(occurs_most_often('Good morning world!', 4))
print(occurs_most_often('abababababababababababa', 3))
