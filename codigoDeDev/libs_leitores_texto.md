# Bibliotecas de texto para fala (TTS) em Python

| Biblioteca | Link | Online / Offline | Gratuita ou paga | Precisa de chave | Português | Observações |
|---|---|---|---|---|---|---|
| **gTTS** (a que você usa) | https://pypi.org/project/gTTS | Online | Gratuita | Não | Sim (pt-BR) | Voz robótica, sem controle de tom ou velocidade, depende do Google Translate. |
| **edge-tts** | https://pypi.org/project/edge-tts | Online | Gratuita | Não | Sim (vozes pt-BR como Francisca e Antonio) | Usa as vozes neurais do Microsoft Edge. Qualidade alta e controle de velocidade e tom. Uso não oficial, pode deixar de funcionar se a Microsoft mudar o serviço. |
| **pyttsx3** | https://pypi.org/project/pyttsx3 | Offline | Gratuita | Não | Depende das vozes instaladas no sistema | Usa a voz nativa do sistema (SAPI5 no Windows, NSSpeechSynthesizer no macOS, eSpeak no Linux). Qualidade básica, mas muito simples de usar. |
| **Piper** | https://pypi.org/project/piper-tts | Offline | Gratuita | Não | Sim (vozes pt-BR) | Vozes neurais leves e rápidas, rodam bem em CPU. Ótima relação entre qualidade e custo computacional. |
| **Kokoro** | https://pypi.org/project/kokoro | Offline | Gratuita (Apache 2.0) | Não | Sim (pt-BR, versão 1.0 em diante) | Modelo de 82M de parâmetros, qualidade muito boa. Exige PyTorch e mais recursos. |
| **Coqui TTS (XTTS v2)** | https://pypi.org/project/TTS | Offline | Gratuita (licença não comercial no modelo XTTS) | Não | Sim | Permite clonar voz a partir de alguns segundos de áudio. Pesado e lento sem GPU. Empresa Coqui encerrada, pacote mantido pela comunidade. |
| **Silero TTS** | https://github.com/snakers4/silero-models | Offline | Gratuita | Não | Limitado (confira se há modelo pt-BR) | Modelos leves, bons para inglês, russo e outros idiomas. |
| **Amazon Polly** (boto3) | https://aws.amazon.com/polly | Online | Paga (camada gratuita de 12 meses) | Sim (credenciais AWS) | Sim (pt-BR, vozes Camila e Ricardo) | Vozes neurais de excelente qualidade, cobrança por caractere. |
| **Azure Speech SDK** | https://pypi.org/project/azure-cognitiveservices-speech | Online | Paga (camada gratuita de 500 mil caracteres por mês) | Sim (chave e região) | Sim (pt-BR, muitas vozes) | Vozes muito naturais e muitas opções de estilo de fala. |
| **Google Cloud TTS** | https://pypi.org/project/google-cloud-texttospeech | Online | Paga (camada gratuita limitada) | Sim (conta de serviço JSON) | Sim (pt-BR) | Versão paga do gTTS, com vozes WaveNet e Neural2 bem melhores. |
| **OpenAI TTS** | https://pypi.org/project/openai | Online | Paga | Sim | Sim (multilíngue) | Vozes naturais e fáceis de usar, cobrança por caractere. |
| **ElevenLabs** | https://pypi.org/project/elevenlabs | Online | Freemium (plano grátis limitado) | Sim | Sim | Muito realista, inclusive com clonagem de voz. O plano grátis tem poucos caracteres por mês. |

## Qual escolher

- **Sem pagar e sem chave, com internet:** edge-tts.
- **Sem internet, leve:** Piper.
- **Sem internet, mais qualidade:** Kokoro (precisa de mais recursos).
- **Uso profissional e estável:** Azure, Polly ou Google Cloud.
