import requests, os

def get_text_path():
    while 1:
        FR_dir = input('Введите путь до директории с FR текстом. Нажмите ENTER, если файл - в текущей директории: ')
        if FR_dir == '':
            FR_dir = os.path.abspath(os.path.dirname(__file__))
            FR_path = os.path.join(FR_dir, 'FR.txt')
        else:
            FR_path = os.path.join(FR_dir, 'FR.txt')
        if os.path.isfile(FR_path):
            break
        else:
            print('Файла FR.txt нет в директории ', FR_dir)
    while 1:
        ES_dir = input('Введите путь до директории с ES текстом. Нажмите ENTER, если файл - в текущей директории: ')
        if ES_dir == '':
            ES_dir = os.path.abspath(os.path.dirname(__file__))
            ES_path = os.path.join(ES_dir, 'ES.txt')
        else:
            ES_path = os.path.join(ES_dir, 'ES.txt')
        if os.path.isfile(ES_path):
            break
        else:
            print('Файла ES.txt нет в директории ', ES_dir)
    while 1:
        DE_dir = input('Введите путь до директории с DE текстом. Нажмите ENTER, если файл - в текущей директории: ')
        if DE_dir == '':
            DE_dir = os.path.abspath(os.path.dirname(__file__))
            DE_path = os.path.join(DE_dir, 'DE.txt')
        else:
            DE_path = os.path.join(DE_dir, 'DE.txt')
        if os.path.isfile(DE_path):
            break
        else:
            print('Файла DE.txt нет в директории ', DE_dir)
    return FR_path, ES_path, DE_path

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

def translate_it(FR_path, ES_path, DE_path, path_to_result, lang_from, lang_to = 'ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    textFR = open(FR_path).read()
    textES = open(ES_path).read()
    textDE = open(DE_path).read()

    paramsFR = {
        'key': key,
        'lang': lang_from + '-' + lang_to,
        'text': textFR,
    }
    paramsES = {
        'key': key,
        'lang': lang_from + '-' + lang_to,
        'text': textES,
    }
    paramsDE = {
        'key': key,
        'lang': lang_from + '-' + lang_to,
        'text': textDE,
    }
    responseFR = requests.get(url, params=paramsFR).json()
    responseES = requests.get(url, params=paramsES).json()
    responseDE = requests.get(url, params=paramsDE).json()

    with open(os.path.join(path_to_result, 'from_FR.txt'), 'w') as FR:
        try:
            FR.write(''.join(responseFR['text']))
        except Exception:
            print('Не удается перевести на язык ' + lang_to)

    with open(os.path.join(path_to_result, 'from_ES.txt'), 'w') as ES:
        try:
            ES.write(''.join(responseES['text']))
        except Exception:
            print('Не удается перевести на язык ' + lang_to)

    with open(os.path.join(path_to_result, 'from_DE.txt'), 'w') as DE:
        try:
            DE.write(''.join(responseDE['text']))
        except Exception:
            print('Не удается перевести на язык ' + lang_to)

    FR.close()
    ES.close()
    DE.close()

if __name__ == '__main__':
    FR_path, ES_path, DE_path = get_text_path()
    path_to_result = get_result_path()
    translate_it(FR_path, ES_path, DE_path, path_to_result, 'de', 'en')
