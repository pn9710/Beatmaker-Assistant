# Belus Beats Bot
Discord bot for Belus Beats that recommends unique hip-hop inspired songs, leveraging machine learning for trend analysis.

A multi-functional Discord bot for the music producer community, providing AI-driven music generation, song recommendations, sentiment analysis on lyrics, and trend-driven responses. The bot is inspired by the god of sound, Apollo, and helps users explore unique beats and sounds within the hip-hop genre.
## Features
1. **GPT-3 Chat** (`!ask`): Get insightful responses to questions and creative prompts.
2. **Sentiment Analysis** (`!sentiment <text>`): Analyze the sentiment of a text, useful for lyrics and song content.
3. **AI Music Generation** (`!generate_music`): Generates a unique 30-second MIDI music sequence based on AI models from Google Magenta.
4. **Daily Song Recommendation** (`!dailysong`): Recommends a daily hip-hop track using the Spotify API.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YOUR-USERNAME/Belus-Beats-Bot.git
    cd Belus-Beats-Bot
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Variables**: Create a `.env` file in the root folder and add the following variables:
    ```plaintext
    DISCORD_TOKEN=<your_discord_token>
    OPENAI_API_KEY=<your_openai_api_key>
    SPOTIPY_CLIENT_ID=<your_spotify_client_id>
    SPOTIPY_CLIENT_SECRET=<your_spotify_client_secret>
    ```

4. **Set up Magenta model**:
    - Download the Magenta `performance_rnn.mag` model and place it in the project directory. Update the path in the `generate_music` function.

## Usage

Run the bot:
```bash
python belus_beats_bot.py
