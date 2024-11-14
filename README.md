# Belus Beats Bot

Belus Beats Bot is a music production tool and assistant designed for Discord, enabling easy access to music generation, sample search, sentiment analysis, daily music recommendations, and other creative functionalities. Inspired by the mythology of Olympus and dedicated to the God of Sound, Apollo, this bot is built to support your musical journey, whether you're creating beats, searching for inspiration, or analyzing lyrics.

## Features

1. **YouTube Sample Search**: Find YouTube samples by BPM, genre, mood, or keywords.
   - Use `!sample <query>` to search for samples directly from YouTube, returning relevant video links to inspire your beats.

2. **AI Music Generation**: Leverage Magenta's AI for unique, MIDI-generated music ideas.
   - Use `!generate_music` to create MIDI samples on the fly.

3. **Sentiment Analysis**: Analyze the mood of lyrics or messages.
   - Use `!sentiment <text>` to get sentiment ratings (e.g., positive, neutral, negative) for your lyrics or ideas.

4. **Daily Song Recommendation**: Get a daily recommended song from YouTube based on genre or mood.
   - Use `!dailysong` to get the current day’s handpicked track to keep you inspired.

5. **GPT-3.5/4 Chat Integration**: Use OpenAI's language model to answer questions, provide songwriting help, or brainstorm.
   - Use `!ask <question>` to chat with the bot on any topic, from music theory to mythology.

## Setup

### Prerequisites

- Python 3.7+
- Discord API Token
- YouTube Data API Key
- OpenAI API Key

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/belus-beats-bot.git
   cd belus-beats-bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file in the root of the project and add your API keys:

   ```bash
   DISCORD_TOKEN=your_discord_token
   OPENAI_API_KEY=your_openai_key
   YOUTUBE_API_KEY=your_youtube_data_api_key
   ```

### Running the Bot

Run the bot with:

```bash
python belus-beats-bot.py
```

## Usage

Add Belus Beats Bot to your Discord server, and use the following commands:

- **Sample Search**: `!sample <query>` - Searches YouTube for music samples based on your keywords.
- **Generate AI Music**: `!generate_music` - Creates a new AI-generated MIDI file.
- **Sentiment Analysis**: `!sentiment <text>` - Analyzes the sentiment of the provided text.
- **Daily Song Recommendation**: `!dailysong` - Provides a daily music recommendation.
- **Chat with GPT**: `!ask <question>` - Ask the bot any question for help with music theory, inspiration, or general knowledge.

## Integrations

Belus Beats Bot integrates several tools for a diverse music production experience:

- **YouTube Data API** for finding sample material on YouTube.
- **Magenta AI** for music generation.
- **OpenAI GPT-3.5/4** for conversational assistance.
- **Hugging Face Transformers** for sentiment analysis.

## Contributing

We welcome contributions to enhance Belus Beats Bot. Please submit a pull request or open an issue to get started.

---

This README file now documents the app's functionality, setup, and usage instructions, making it easier for users to understand how to get started and make use of the bot's features.
