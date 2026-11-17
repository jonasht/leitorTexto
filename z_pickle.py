import pickle

def write_pkl(data):
    # salvar
    with open("dados.pkl", "wb") as f:
        pickle.dump(data, f)

def read_pkl():
    # ler de volta
    with open("dados.pkl", "rb") as f:
        data = pickle.load(f)
    return data

LANGUAGES = [
"Africâner",
"Amárico",
"Árabe",
"Búlgaro",
"Bengali",
"Bósnio",
"Catalão",
"Tcheco",
"Galês",
"Dinamarquês",
"Alemão",
"Grego",
"Inglês",
"Espanhol",
"Estoniano",
"Bascuense",
"Finlandês",
"Francês",
"Francês (Canadá)",
"Galego",
"Gujarati",
"Hauçá",
"Hindi",
"Croata",
"Húngaro",
"Indonésio",
"Islandês",
"Italiano",
"Hebraico",
"Japonês",
"Javanês",
"Khmer",
"Canarês",
"Coreano",
"Latim",
"Lituano",
"Letão",
"Malayalam",
"Marata",
"Malaio",
"Birmanês",
"Nepali",
"Holandês",
"Norueguês",
"Punjabi (Gurmukhi)",
"Polonês",
"Português (Brasil)",
"Português (Portugal)",
"Romeno",
"Russo",
"Cingalês",
"Eslovaco",
"Albanês",
"Sérvio",
"Sundanês",
"Sueco",
"Suaíli",
"Tâmil",
"Telugu",
"Tailandês",
"Filipino",
"Turco",
"Ucraniano",
"Urdu",
"Vietnamita",
"Cantonês",
"Chinês (Simplificado)",
"Chinês (Mandarim/Taiwanês)",
"Chinês (Mandarim)"
]
dic_langPt = {
'Português (Brasil)':'pt',
'Inglês':'en',
'Espanhol':'es',
'Português (Portugal)':'pt-PT',

'Africâner':'af',
'Amárico':'am',
'Árabe':'ar',
'Búlgaro':'bg',
'Bengali':'bn',
'Bósnio':'bs',
'Catalão':'ca',
'Tcheco':'cs',
'Galês':'cy',
'Dinamarquês':'da',
'Alemão':'de',
'Grego':'el',
'Estoniano':'et',
'Bascuense':'eu',
'Finlandês':'fi',
'Francês':'fr',
'Francês (Canadá)':'fr-CA',
'Galego':'gl',
'Gujarati':'gu',
'Hauçá':'ha',
'Hindi':'hi',
'Croata':'hr',
'Húngaro':'hu',
'Indonésio':'id',
'Islandês':'is',
'Italiano':'it',
'Hebraico':'iw',
'Japonês':'ja',
'Javanês':'jw',
'Khmer':'km',
'Canarês':'kn',
'Coreano':'ko',
'Latim':'la',
'Lituano':'lt',
'Letão':'lv',
'Malayalam':'ml',
'Marata':'mr',
'Malaio':'ms',
'Birmanês':'my',
'Nepali':'ne',
'Holandês':'nl',
'Norueguês':'no',
'Punjabi (Gurmukhi)':'pa',
'Polonês':'pl',
'Romeno':'ro',
'Russo':'ru',
'Cingalês':'si',
'Eslovaco':'sk',
'Albanês':'sq',
'Sérvio':'sr',
'Sundanês':'su',
'Sueco':'sv',
'Suaíli':'sw',
'Tâmil':'ta',
'Telugu':'te',
'Tailandês':'th',
'Filipino':'tl',
'Turco':'tr',
'Ucraniano':'uk',
'Urdu':'ur',
'Vietnamita':'vi',
'Cantonês':'yue',
'Chinês (Simplificado)':'zh-CN',
'Chinês (Mandarim/Taiwanês)':'zh-TW',
'Chinês (Mandarim)':'zh'
}
if __name__ == '__main__':
    
    import gtts
    import func_ansiColors as c  
    def enfeitar():
        print('=-'*30+'=')
    
    # lang = gtts.lang.tts_langs() # type:ignore
# 
    # for (k, v), lang_pt in zip(lang.items(), LANGUAGES):
        # print(f'{k}: {v}={lang_pt}')
        # lang[k]=lang_pt
# 
    # lang = dict(zip(lang.keys(), LANGUAGES))
    # enfeitar()
    # print(lang)
    # 
    # lang = dict(zip(lang.values(), lang.keys()))
    # enfeitar()
    # print(lang)
    # enfeitar()
    # 
    # for k, v in lang.items():
        # print(k, v)
    # 
    # write_pkl(lang)
    # 
    # for k, v in lang.items():
        # print(f"'{k}':'{v}',")
        
    print(read_pkl())    
    