import edge_tts
import asyncio
import json


def exemplo_():
    texto = "Olá! Este é um exemplo de conversão de texto para fala."
    voz = "pt-BR-FranciscaNeural"

    edge_tts.Communicate(texto, voz).save_sync("saida.mp3")


async def mostrar_vezes():
    vozes = await edge_tts.list_voices()
    for v in vozes:
        if v["Locale"] == "pt-BR":
            print(v["ShortName"], "-", v["Gender"])
# mostrar todas vozes em portugues:
# asyncio.run(mostrar_vezes())

def get_allVoicesOnline():
    vozes = asyncio.run(edge_tts.list_voices())
    
    return vozes

# escrever VOZES infos do json
def write_json(info_voices):
    file_name = 'edgeTss_voices.json'
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(info_voices, file, ensure_ascii=False, indent=4)

# ler as vozes infos do json
def read_json():
    file_name = 'edgeTss_voices.json'
    with open(file_name, 'r') as file:
        infos = json.load(file)
        
    return infos

# transforma texto em audio num arquivo mp3
def trans_txt_To_audioMP3(texto='este é um texto em portugues', voz='pt-BR-FranciscaNeural', nameFile='saida.mp3'):

    edge_tts.Communicate(texto, voz).save_sync(nameFile)

# pega os nomes de vozes para usar pela localização, como brasil: 'pt-br'
def get_names(locale='pt-BR'):
    infos = read_json()
    for i in infos:
        if i["Locale"] == locale:
            print('shortname', i['ShortName'])

if __name__ == '__main__':
    
    pessoaNome1 = 'pt-BR-ThalitaMultilingualNeural'
    pessoaNome2 = 'pt-BR-AntonioNeural'
    pessoaNome3 = 'pt-BR-FranciscaNeural'
    
    frase = 'bom dia, boa tarde, boa noite, boa madrugada. como o tomate atravessou a rua?'

    # trans_txt_To_audioMP3(frase, pessoaNome1, nameFile='1'+pessoaNome1 + '.mp3')
    # trans_txt_To_audioMP3(frase, pessoaNome2, nameFile='2'+pessoaNome2 + '.mp3')
    # trans_txt_To_audioMP3(frase, pessoaNome3, nameFile='3'+pessoaNome3 + '.mp3')

    
