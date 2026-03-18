from google import genai
from google.genai import types
from dotenv import load_dotenv
import logging
import wave

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()


model_name ="gemini-2.5-flash-preview-tts"

prompt = "i'm dinesh  , how can i help you"

response = client.models.generate_content(
    model = model_name,
    contents = f"say: {prompt}",
    config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)


data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data)

