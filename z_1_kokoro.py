from kokoro import KPipeline
from pydub import AudioSegment
import numpy as np
import os

PIPELINES = {
    "pt": KPipeline(lang_code="p"),
    "en": KPipeline(lang_code="a"),
}
# • pf_dora. Voz feminina (Dora).
# • pm_alex. Voz masculina (Alex).
# • pm_santa. Voz masculina grave (Santa)

VOZES = {
    "pt": "pm_alex",
    "en": "af_heart",
}

def gerar_audio(texto: str, idioma: str, nome_arquivo: str) -> str:
    idioma = idioma.lower()

    if idioma not in PIPELINES:
        raise ValueError("Use 'pt' ou 'en'.")

    pipeline = PIPELINES[idioma]
    voz = VOZES[idioma]

    trechos = [
        audio
        for _, _, audio in pipeline(texto, voice=voz, speed=1.0)
    ]

    if not trechos:
        raise RuntimeError("Nenhum áudio foi gerado.")

    audio_completo = np.concatenate(trechos)

    # pydub recebe áudio PCM de 16 bits; o Kokoro gera a 24 kHz
    audio_int16 = (audio_completo * 32767).clip(-32768, 32767).astype(np.int16)
    segmento = AudioSegment(
        data=audio_int16.tobytes(),
        sample_width=2,
        frame_rate=24000,
        channels=1,
    )

    caminho = nome_arquivo
    if not caminho.lower().endswith(".mp3"):
        caminho += ".mp3"

    segmento.export(caminho, format="mp3", bitrate="192k")
    return caminho

def read_txt(path):
    with open(path, 'r') as file:
        texto = file.read()
    
    return texto


if __name__ == '__main__':
    texto = read_txt('./exemploTexto.txt')

    arquivo = gerar_audio(
    texto,
    "pt",
    "conto_contadoPorAlex"
    )
    print(f"Salvo em: {arquivo}")
