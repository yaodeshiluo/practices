

fn = 'test.txt'
file(fn, 'w+').write('test\ntest2')
content = file(fn, 'r').read()
print content.replace('\r', '\\r').replace('\n', '\\n')

for link in links:
    img = opener(link)
    filename = link.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(img)


