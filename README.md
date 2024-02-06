# NOW DEPRECATED



# LinguaSync

English to japanese voice translater






## Run Locally

### requirements
  -Docker

Clone the project

```bash
  git clone https://github.com/Yashwanth12321/LinguaSync.git
```

Go to the project directory

```bash
  cd LinguaSync
```

Install dependencies

    #### linux users- before proceeding run the following command(necessary for pyaudio lib to run)
```bash
    sudo apt-get install portaudio19-dev
```
install dependencies
```bash
    pip install -r requirements.txt
    pip install fsspec
```

Pull the docker image
```bash
      docker pull voicevox/voicevox_engine:cpu-ubuntu20.04-latest
```
Run the docker image
```bash
      docker run --rm -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:cpu-ubuntu20.04-latest
```

Install whisperai repo Locally
```bash 
      pip install git+https://github.com/openai/whisper.git 
```

Run
```bash
    python3 Linguasync.py
```


## Tech Stack

**Client:** Python3

**Server:** Voicevox docker image

