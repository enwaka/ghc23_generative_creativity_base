import soundfile as sf
import sounddevice as sd
import openai
import os
import whisper
from dotenv import load_dotenv
from flask import Flask, render_template

# load environment variables
load_dotenv()

# Select from the following models: "tiny", "base", "small", "medium", "large"
model = whisper.load_model("base")

app = Flask(__name__)


@app.route("/home")
def index():
    return render_template("/input.html")


@app.route("/record", methods=['POST', 'GET'])
def voice_rec():
    raise NotImplementedError

'''
This method transcribe voice input
'''


def transcribe():
    raise NotImplementedError

'''
calls openai text-davinci-002 model
'''


def generate_lyrics(text):
    raise NotImplementedError


if __name__ == '__main__':
    app.run()
