# LinguaSync
Real-time voice to voice translater....


locally installation
create virtual env for py  if you want many libs

have docker in your systems

pip install {all the libs below}

general libs:json,requests,io,time
#tools needed
-speech to text
    -libraries req:pyaudio,keyboard,wave,openai,whisper,openai-whisper,fsspec(important for sound conversion)
    -whisperAI(speech to text)
-text translate
    -lib: deep_translator
-text to speech
    -lib- voicevox api,
    voicevox engine docker image running
    cmds->(cpu)
    docker pull voicevox/voicevox_engine:cpu-ubuntu20.04-latest
docker run --rm -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:cpu-ubuntu20.04-latest
    (gpu)
    docker pull voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest'

    download and run docker image which creates local server for the voicevox model
    

more-dockerise this cause automation