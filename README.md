# Belus Beats Bot

Welcome to **Belus Beats Bot** — a powerful Discord bot integrated with AI and music discovery tools. This bot allows users to explore music samples, ask AI-generated questions, analyze sentiments, and more, all while offering a user-friendly GUI for easy control.

## Features
- **YouTube Sample Search**: Search YouTube for music samples using keywords.
- **GPT-3 Responses**: Ask the bot any question, and it will generate a response based on OpenAI's GPT-3 engine.
- **Sentiment Analysis**: Analyze the sentiment of any text to determine its emotional tone.
- **Daily Song Recommendation**: Get a daily song recommendation from YouTube, based on current trends.
- **Discord Integration**: Easily integrate the bot with your Discord server to respond to user queries in real time.

## Requirements
- Python 3.7 or higher
- `discord.py` library
- `openai` library
- `google-api-python-client` library
- `transformers` library
- `tkinter` for GUI functionality

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/belus-beats-bot.git
   cd belus-beats-bot
   ```

2. **Install dependencies**:
   Make sure you have Python 3.7+ installed, and then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**:
   Add your API keys and tokens in a `.env` file in the root directory.
   
   Example:
   ```
   OPENAI_API_KEY=your_openai_api_key
   YOUTUBE_API_KEY=your_youtube_api_key
   DISCORD_TOKEN=your_discord_token
   ```

4. **Run the bot**:
   Once everything is set up, you can run the bot using the following command:
   ```bash
   python app.py
   ```

5. **Start the GUI**:
   A simple graphical user interface (GUI) will appear with buttons to start or close the bot.

## Commands
- **`!ask [question]`**: Ask the bot a question and get a GPT-3 response.
- **`!sentiment [text]`**: Analyze the sentiment of the provided text.
- **`!dailysong`**: Get a daily song recommendation from YouTube.
- **`!sample [keyword]`**: Search for YouTube samples based on the keyword provided.

## Example Usage

### Start the bot:
1. Press the "Start Bot" button in the GUI window to start the bot in Discord.
   
### Ask a question:
1. In your Discord channel, type:
   ```
   !ask What is the weather today?
   ```
   The bot will respond with an AI-generated answer.

### Sentiment analysis:
1. Type the following to analyze the sentiment of a statement:
   ```
   !sentiment I love coding with Python!
   ```
   The bot will respond with the sentiment analysis.

## Contributing
If you'd like to contribute to **Belus Beats Bot**, feel free to fork the repository, create a branch, and submit a pull request. Please make sure to follow the standard Python coding conventions.

## License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
