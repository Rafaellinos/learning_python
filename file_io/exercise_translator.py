# pip install translate
from translate import Translator

try:
    with open("translate_to", "r") as file:
        jp = Translator(to_lang="ja")
        print(''.join([jp.translate(line) for line in file.readlines()]))

            
except Exception as err:
    print(f'Erro: {err}')