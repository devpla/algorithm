from re import sub, findall


def dtb(p):
    p = sub('<[a-zA-Z]+>', '', p)
    p = sub('<[/a-zA-Z ]+>', '', p)
    p = sub('[ ]+', ' ', p)
    return p


h = input().split('<p>')

for p in h:
    t = findall('"[a-zA-z0-9_ ]+"', p)
    if t:
        if '</p>' in p:
            p = p.split('</p>')
            p = p[0]
            print(dtb(p).strip())
        res = t[0].strip('"').strip()
        print(f'title : {res}')
    else:
        print(dtb(p).strip())
