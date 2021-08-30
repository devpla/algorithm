def is_group_words(words):
    group_words = {words[0]}
    not_group_words = set()
    prev = words[0]

    for char in words:
        if char != prev and char in group_words:
            not_group_words.add(char)
        elif char not in group_words:
            group_words.add(char)
        prev = char

    return set(words) == (group_words - not_group_words)


result = 0

for _ in range(int(input())):
    words = input()

    if is_group_words(words):
        result += 1

print(result)
