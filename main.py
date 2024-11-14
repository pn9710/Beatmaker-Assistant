import os
import discord
import openai
import tkinter as tk
import threading
from googleapiclient.discovery import build
from transformers import pipeline
from discord_bot import run_bot  # Import the main function that runs your bot

def start_bot():
    threading.Thread(target=run_bot).start()

# Setting up the GUI window
window = tk.Tk()
window.title("Belus Beats Bot")
window.geometry("300x150")

# Start Button
start_button = tk.Button(window, text="Start Bot", command=start_bot)
start_button.pack(pady=20)

# Close Button
close_button = tk.Button(window, text="Close", command=window.destroy)
close_button.pack(pady=10)

window.mainloop()

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
youtube = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))

# Discord client setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Sentiment Analysis setup
sentiment_pipeline = pipeline("sentiment-analysis")

# YouTube sample search function
def youtube_sample_search(query, max_results=5):
    youtube = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))
    search_response = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results
    ).execute()

    results = []
    for item in search_response['items']:
        video_title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        results.append((video_title, video_url))

    return results

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

# Helper functions
def generate_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result[0]["label"], result[0]["score"]

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

# Run the bot
client.run(os.getenv("DISCORD_TOKEN"))

