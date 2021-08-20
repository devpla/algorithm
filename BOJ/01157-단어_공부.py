from collections import Counter

string = input().upper()

if len(string) == 1:
    print(string)
else: 
    cnt = Counter(string).most_common()
    if cnt[0][1] == cnt[1][1]:
        print('?')
    else:
        print(cnt[0][0])
