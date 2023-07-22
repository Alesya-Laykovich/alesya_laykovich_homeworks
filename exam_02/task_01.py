# 1. Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt. Затем переименуйте файлы на: rename_1.txt, rename_2.txt,
# rename_3.txt. После этого удалите созданную папку. Все операции выполнять с помощью
# встроенных функций библиотеки os.

import os
# os.chdir(r'C:\Users\user\Desktop')
# print(os.getcwd())
# os.mkdir('new_folder')
# with open(r'C:\Users\user\Desktop\new_folder\test_1.txt', 'w') as file:
#     print(file)
# with open(r'C:\Users\user\Desktop\new_folder\test_2.txt', 'w') as file:
#     print(file)
# with open(r'C:\Users\user\Desktop\new_folder\test_3.txt', 'w') as file:
#     print(file)
os.chdir(r'C:\Users\user\Desktop\new_folder')
# print(os.getcwd())
# os.rename('test_1.txt', 'rename_1.txt')
# os.rename('test_2.txt', 'rename_2.txt')
# os.rename('test_3.txt', 'rename_3.txt')
# os.remove('rename_1.txt')
# os.remove('rename_2.txt')
# os.remove('rename_3.txt')
os.chdir('..')
print(os.getcwd())
os.rmdir('new_folder')
