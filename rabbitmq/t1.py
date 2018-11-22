import re

typed = {'error':0,'abc':0,'ded':0,'fds':0,'jffg':0}
def get_type_count(type):
    with open(r'C:\Users\Administrator\Desktop\appu\test.txt', 'r') as f:
        texts = f.readlines()
        for text in texts:
            matcher = re.compile('^{}:'.format(type)).match(text)
            if matcher:
                typed[type] = typed.get(type,0)+1

for type in typed.keys():
    get_type_count(type)

print(typed)