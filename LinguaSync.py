import wave
import keyboard
import pyaudio
import whisper
import requests
import json
import io
import time
import deep_translator 


# Global variables
recording = False
audio_data = []

def text_to_speech(text):
    
   
    #11,-male
    #2-female
    # 69-child
    speaker_id = 2 # Choose the appropriate speaker_id based on your requirement
    params=(("text",text),
            ("speaker",speaker_id),
            ("postPhonemeLength", 1.0),
            ("prePhonemeLength", 1.0),
            ("intonationScale", 1.5),
            ("speedScale", 1.7),
            ("volumeScale", 4.0)
            )

    response = requests.post("http://127.0.0.1:50021/audio_query",params=params )
    res=requests.post("http://127.0.0.1:50021/synthesis",
                    headers={"Content-Type":"application/json"},
                    params=params,
                    data=json.dumps(response.json()))
    audio=io.BytesIO(res.content)

    with wave.open(audio,'rb') as f:
                p = pyaudio.PyAudio()

                def _callback(in_data, frame_count, time_info, status):
                    data = f.readframes(frame_count)
                    return (data, pyaudio.paContinue)

                stream = p.open(format=p.get_format_from_width(width=f.getsampwidth()),
                                channels=f.getnchannels(),
                                rate=f.getframerate(),
                                output=True,
                                stream_callback=_callback)

                stream.start_stream()
                while stream.is_active():
                    time.sleep(0.1)

                stream.stop_stream()
                stream.close()
                p.terminate()

def translate(text):
     translated = deep_translator.GoogleTranslator(source='auto', target='ja').translate(text)
     return translated


def start_recording(filename, channels, sample_rate):
    global audio_data
    audio_data = []

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=1024)

    print("Recording started. Press and hold 'v' to stop recording.")
    
    frames = []
    while recording:
        data = stream.read(1024)
        frames.append(data)
        if not keyboard.is_pressed('v'):
            break

    print("Recording stopped.")
    
    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_data = b''.join(frames)
    
    mode = 'wb' if not keyboard.is_pressed('v') else 'ab'
    with wave.open(filename, mode) as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data)

    print(f"Recording appended to {filename}")

    # Perform transcription after recording stops
    model = whisper.load_model('tiny')
    text = model.transcribe(filename)
    print("Transcription:")
    print(text['text'])
    return text['text']


def main():
    global recording

    filename = "recorded_audio.wav"
    channels = 1
    sample_rate = 44100

    while True:
        keyboard.wait("v", suppress=True)
        recording = True
        text=start_recording(filename, channels, sample_rate)
        recording = False
        translated_text=translate(text=text)
        text_to_speech(text=translated_text)

if __name__ == "__main__":
    main()
