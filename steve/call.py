import os
import requests
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM_NUMBER")
ELEVENLABS_KEY = os.getenv("ELEVEN_API_KEY")

def generate_audio(text: str) -> bytes:
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL/audio"
    headers = {
        "xi-api-key": ELEVENLABS_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.content

def make_call(to_number: str, audio_url: str):
    from twilio.rest import Client
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    call = client.calls.create(
        twiml=f'<Response><Play>{audio_url}</Play></Response>',
        to=to_number,
        from_=TWILIO_FROM
    )
    return call.sid
