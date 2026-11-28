from kokoro import KPipeline
from pydub import AudioSegment
import numpy as np
import os

PIPELINES = {
    "pt": KPipeline(lang_code="p"),
    "en": KPipeline(lang_code="a"),
}

VOZES = {
    "pt": "pf_dora",
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



if __name__ == '__main__':
    texto = '''A Importância da Educação na Sociedade Moderna
A educação é considerada um dos pilares fundamentais para o desenvolvimento de qualquer sociedade. Através do conhecimento e da aprendizagem contínua, os indivíduos adquirem habilidades essenciais para enfrentar os desafios do mundo contemporâneo.
Nos dias atuais, o acesso à educação de qualidade tornou-se ainda mais crucial. Com o avanço da tecnologia e a transformação digital, profissionais precisam estar constantemente atualizados e preparados para se adaptar às mudanças do mercado de trabalho. A educação não apenas fornece conhecimento técnico, mas também desenvolve competências como pensamento crítico, criatividade e inteligência emocional.
Além disso, a educação promove a inclusão social e reduz desigualdades. Quando pessoas de diferentes origens têm acesso a oportunidades educacionais, há uma redistribuição de chances e a possibilidade de mobilidade social. Investir em educação é investir no futuro de uma nação.
No entanto, ainda existem barreiras significativas que impedem muitos de acessar uma educação adequada. A falta de infraestrutura, recursos limitados e desigualdades econômicas continuam sendo obstáculos importantes em várias regiões do mundo.
Portanto, é responsabilidade de governos, instituições e sociedade em geral priorizar e apoiar a educação como um direito fundamental de todos.
'''
    arquivo = gerar_audio(
    texto,
    "pt",
    "conversa"
    )
    print(f"Salvo em: {arquivo}")
