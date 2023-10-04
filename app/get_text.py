# with open('1292.txt', 'r', encoding='utf-8') as f:
#     old = f.readlines()
#     new_f = open('new_1292.txt', 'w')
#     for el in old:
#         if '.' in el:
#             new_f.write(el)
#     new_f.close()

item = '26.30.23.000'
for i in range(len(item), 0, -1):
    num = item[0: i]
    print(num)

