import re



test1 = """can tid ter 9


choon tid ter 50


can tid ter 50


bart tid ter 5"""






a = test1.split('\n')
b = test.split('\n')


for i in a:
    if 'tid' in i:
        print(re.findall('(.+) tid (.+)', i))
