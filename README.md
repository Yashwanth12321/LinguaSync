# LinguaSync
Real-time voice to voice translater....


locally installation
create virtual env for py  if you want many libs

have docker in your systems

docker cmds
cpu

        docker pull voicevox/voicevox_engine:cpu-ubuntu20.04-latest
        docker run --rm -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:cpu-ubuntu20.04-latest
gpu

        docker pull voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
        docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
    
    

get whisperai repo
cmd

        pip install git+https://github.com/openai/whisper.git 

main file cmds

    pip install pyaudio keyboard wave openai openai-whisper fsspec deep_translator requests time io json

    

pip install {all the libs below}

general libs:json,requests,io,time
#tools needed
-speech to text

-libraries req:pyaudio,keyboard,wave,openai,whisper,openai-whisper,fsspec(important for sound conversion)
    -whisperAI(speech to text)
-text translate
    -lib: deep_translator
    
-text to speech
    voicevox api,
    voicevox engine docker image running


download and run docker image which creates local server for the voicevox model
    
used most lightweight model with least parameters i.e, 'tiny', so might be inaccurate

future-dockerise this cause automation


future2- you have to download any whisper model to run it
better option using whisper docker container and requests from it
clone this repo https://github.com/ahmetoner/whisper-asr-webservice
and run this
cmds

        docker pull onerahmet/openai-whisper-asr-webservice:latest
        docker run -d -p 9000:9000 -e ASR_MODEL=base onerahmet/openai-whisper-asr-webservice:latest
