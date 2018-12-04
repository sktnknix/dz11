import requests, os, sys

def get_text_path():
    lst=[]
    while 1:
        file_dir = input('Введите путь к файлу для перевода. Нажмите [q], если набрали достаточно файлов\n')
        if file_dir != 'q':
            if file_dir not in lst:
                if file_dir == '':
                    file_dir = os.path.abspath(os.path.dirname(__file__))
                    file_path = os.path.join(file_dir, os.path.basename(file_dir))
                else:
                    file_path = file_dir
                if os.path.isfile(file_path):
                    lst.append(file_path)
                else:
                    print('Нет такого файла:', file_path)
            else:
                print('Вы уже вводили такой файл, выберите другой')
        else:
            break
    if len(lst) == 0:
        print('Нечего переводить, закрываемся ...')
        sys.exit()
    else:
        print('Будем переводить следующие файлы: ')
        for file in lst:
            print(file)
    return lst

def get_result_path():
    while 1:
        res = input('Куда сохранить результат перевода ? Нажмите ENTER, если сохранить в текущей директории: ')
        if res == '':
            res_path = os.path.abspath(os.path.dirname(__file__))
        else:
            res_path = res
        if os.path.isdir(res_path):
            result_dir = os.path.join(res_path, 'Result')
            if not os.path.exists(result_dir):
                os.makedirs(result_dir)
            return result_dir
        else:
            print('Такого каталога не существует ', res_path)

def translate_it(lst, path_to_result, lang_to = 'ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    for file in lst:
        text = open(file, encoding='utf-8').read()
        lang_from = os.path.splitext(os.path.basename(file))[0].lower()
        params = {
            'key': key,
            'lang': lang_from + '-' + lang_to,
            'text': text,
        }
        response = requests.get(url, params=params).json()
        result_file = os.path.basename(file)
        with open(os.path.join(path_to_result, 'from_' + result_file), 'w', encoding='utf-8') as translated:
            try:
                translated.write(''.join(response['text']))
            except Exception:
                print('Не удается перевести на язык ' + lang_to)

if __name__ == '__main__':
    lst = get_text_path()
    path_to_result = get_result_path()
    lang_to = input('На какой язык перевести или нажмите ENTER, чтобы перевести на русский: ')
    if lang_to == '':
        translate_it(lst, path_to_result)
    else:
        translate_it(lst, path_to_result, lang_to)
