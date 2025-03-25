# entrada = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
# lineas = len(entrada)
# columnas = len(entrada[0])
# print(entrada[::-1])
# final = []

# while True:
#     nueva = []
#     for i in entrada:
#         contador = 0
#         for y in i:
#             if contador == 0:
#                 nueva.append(y)
#                 i.remove(y)
#                 contador = 1
#         final.append(nueva)
#         if columnas == 1:
#             break
#         columnas -= 1
#     for i in final:
#         print(str(i).replace(" ", ""))

entrada = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
final = []
# i = 0
for i in range(len(entrada[0])):
    # res = []
    res = []
    res.append(entrada[0][i])
    # res = [1, ]
    for j in range(1, len(entrada)):
        # res = [1, 4, 7, 10, 13]
        res.append(entrada[j][i])
    # final = [[1, 4, 7, 10, 13], ]
    final.append(res)

print(final)
