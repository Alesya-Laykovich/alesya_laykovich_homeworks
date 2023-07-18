# 1. Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите
# на печать в терминал ее содержимое, как и всех подкаталогов(вывести имя папки и имена файлов)
import os
os.chdir('D:\original text')
# print(os.getcwd())
# print(f'Вложенные папки: {os.listdir()}')
# for path, folder, file in os.walk("."):
#     for folder_name in folder:
#         print(f'Подкаталог: {os.path.join(path, folder_name)}')
#     for file_name in file:
#         print(f'Файл: {os.path.join(path, file_name)}')

for path, folder, file in os.walk("."):
    for folder_name in folder:
        print(f'Подкаталог: {folder_name}')
    for file_name in file:
        print(f'Файл: {file_name}')


