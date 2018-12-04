import sys, os
def get_text_path():
    lst = []
    print('Введите путь к файлам для перевода (через ENTER). Для завершения ввода нажмите Ctrl+D: \n')

    enter = sys.stdin.read().split()
    for line in enter:
        if os.path.isfile(line):
                lst.append(line)
        else:
                print('Файл ' + line + ' не найден')
        if len(lst) == 0:
            print('Ни одного файла из указанных не найдено :(')
            sys.exit()
        else:
            print('Будем переводить следующие файлы: ')
            for file in lst:
                print(file)
    return lst

def get_result_path():
    input('Enter result dir path: ') ### на этой строке EOF. 
