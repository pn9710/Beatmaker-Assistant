import os
import discord
import openai
import argparse
from googleapiclient.discovery import build
from transformers import pipeline
from magenta.music import sequence_generator_bundle, performance_sequence_generator
from magenta.protobuf import music_pb2

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
youtube = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))

# Discord client setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Sentiment Analysis setup
sentiment_pipeline = pipeline("sentiment-analysis")

# Command line argument parser
parser = argparse.ArgumentParser(description="Belus Beats Bot CLI")
parser.add_argument("action", choices=["run", "ask", "sentiment", "recommend", "audiostellar", "beepbox", "bespoke", 
                                       "helio", "jamulus", "lmms", "mixxx", "musescore", "openmpt", "sonicpi"],
                    help="Specify the action for the bot")
parser.add_argument("--message", type=str, help="Message content for 'ask' or 'sentiment' actions")
args = parser.parse_args()

# Helper functions for each music tool
def get_audio_stellar():
    return "AudioStellar - Discover latent sound structure: https://github.com/AudioStellar/AudioStellar"

def get_beepbox():
    return "BeepBox - Create and share melodies online: https://www.beepbox.co/"

def get_bespoke_synth():
    return "Bespoke Synth - Modular synthesizer: https://github.com/BespokeSynth/BespokeSynth"

def get_helio_workstation():
    return "Helio Workstation - Music sequencer for all platforms: https://github.com/helio-fm/helio-workstation"

def get_jamulus():
    return "Jamulus - Real-time networked music performance: https://jamulus.io/"

def get_lmms():
    return "LMMS - Cross-platform music production: https://lmms.io/"

def get_mixxx():
    return "Mixxx - Free DJ software: https://mixxx.org/"

def get_musescore():
    return "MuseScore - Create and playback sheet music: https://musescore.org/"

def get_openmpt():
    return "OpenMPT - Sample-based music production tracker: https://openmpt.org/"

def get_sonic_pi():
    return "Sonic Pi - Code-based music creation and performance: https://sonic-pi.net/"

# Function to get daily song recommendation from YouTube
def get_daily_song():
    request = youtube.search().list(
        q="hip hop",
        part="snippet",
        maxResults=1,
        type="video"
    )
    response = request.execute()
    if response['items']:
        video = response['items'][0]
        title = video['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
        return title, video_url
    return None, None

# Function to generate a GPT-3 response
def generate_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Function to analyze sentiment
def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]["label"], result[0]["score"]

# Discord bot event listeners
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ask"):
        prompt = message.content[len("!ask "):]
        response = generate_gpt3_response(prompt)
        await message.channel.send(response)

    elif message.content.startswith("!sentiment"):
        text = message.content[len("!sentiment "):]
        label, score = analyze_sentiment(text)
        await message.channel.send(f"Sentiment: {label}, Score: {score:.2f}")

    elif message.content.startswith("!dailysong"):
        title, video_url = get_daily_song()
        if title and video_url:
            await message.channel.send(f"Today's recommended track: {title} - {video_url}")
        else:
            await message.channel.send("Couldn't find a song recommendation.")

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# CLI command handler
if args.action == "run":
    # Run the bot
    client.run(os.getenv("DISCORD_TOKEN"))

elif args.action == "ask" and args.message:
    # Ask GPT-3 for a response
    response = generate_gpt3_response(args.message)
    print("GPT-3 Response:", response)

elif args.action == "sentiment" and args.message:
    # Analyze sentiment
    label, score = analyze_sentiment(args.message)
    print(f"Sentiment: {label}, Score: {score:.2f}")

elif args.action == "recommend":
    # Get daily song recommendation
    title, video_url = get_daily_song()
    if title and video_url:
        print(f"Today's recommended track: {title} - {video_url}")
    else:
        print("Couldn't find a song recommendation.")

# Tool link commands
elif args.action == "audiostellar":
    print(get_audio_stellar())
elif args.action == "beepbox":
    print(get_beepbox())
elif args.action == "bespoke":
    print(get_bespoke_synth())
elif args.action == "helio":
    print(get_helio_workstation())
elif args.action == "jamulus":
    print(get_jamulus())
elif args.action == "lmms":
    print(get_lmms())
elif args.action == "mixxx":
    print(get_mixxx())
elif args.action == "musescore":
    print(get_musescore())
elif args.action == "openmpt":
    print(get_openmpt())
elif args.action == "sonicpi":
    print(get_sonic_pi())


 
