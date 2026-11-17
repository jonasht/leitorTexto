import gtts
import pickle
from qt_material import list_themes
import re


PATH_LANGPT = './dados.pkl'


def get_themes():
    return list_themes()

def get_themes_fmt():
    lista = get_themes()
    lista = [re.sub(r'\.xml', '', v) for v in lista]
    lista = [re.sub(r'_', ' ', v) for v in lista]
    lista = [v.title() for v in lista]

    return lista
    

# read audio, cria o audio com o texto txt.mp3
def read_audio(txt, lang:str, path='audio.mp3'):
    # se txt = str, txt = list()
    if type(txt) == str: txt = [txt]
    
    for linha in txt:
        frase = gtts.gTTS(linha, lang=lang)
        frase.save(path)



def write_theme(themeName=''):
    file_name='./config.txt'
    with open(file_name, 'w') as file:
        file.write(themeName)

def read_theme() -> str:
    file_name='./config.txt'
    with open(file_name, 'r') as file:
        return file.read()
    
def write_pkl(data, path=PATH_LANGPT):
    # salvar 
    with open(path, 'wb') as f:
        pickle.dump(data, f)

def read_pkl(path=PATH_LANGPT):
    # ler 
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data

def get_audioLangs(lang='pt') -> dict:
    '''
    Docstring para get_audioLangs
    
    :param lang: idioma, portugues ou ingles
    :return: returna dicionario das linguas pt ou en
    :rtype: dict['portuges', 'pt', 'ingles': 'en'...]
    '''
    if lang=='pt':
        return read_pkl()
    
    # default retorna em ingles 
    lang = gtts.lang.tts_langs() # type:ignore
    # invertando dicionario
    lang = dict(zip(lang.values(), lang.keys()))

    return lang

def get_audioLangs_keys():
    return list(get_audioLangs().keys())

def get_themes_desfmt(tema:str) -> str:
    # desformatar tema
    tema = re.sub(r'\s', '_', tema)
    tema = tema+'.xml'
    tema = tema.lower()
    return tema
    

if __name__ == '__main__':
    print(get_audioLangs()['Português (Brasil)'])