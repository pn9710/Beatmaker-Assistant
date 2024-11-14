# Belus Beats Bot 🎶

**Belus Beats Bot** is a versatile Discord bot built for music producers, DJs, and audio enthusiasts. It integrates a range of powerful music production tools and APIs for generating beats, analyzing sentiment, discovering samples, and interacting with AI models—all from a simple CLI or directly on Discord!

---

## Features 🚀

- **GPT-3 & GPT-4 Chat Integration**: Generate text-based responses using OpenAI's models.
- **Hugging Face Sentiment Analysis**: Analyze the sentiment of text to determine positivity, negativity, or neutrality.
- **AI Music Generation**: Create music with the Magenta AI Performance RNN.
- **Daily Song Recommendations**: Get a new song recommendation using the YouTube API.
- **Samplette.io Integration**: Fetch random or keyword-specific samples from Samplette.io.
- **Open Source Music Tools**: Easily access and use tools like AudioStellar, BeepBox, LMMS, Sonic Pi, and more.
- **Easy-to-Use CLI**: Perform actions directly from the command line.

## Requirements 📋

- Python 3.8+
- [Discord API Token](https://discord.com/developers/applications)
- OpenAI API Key (GPT-3/GPT-4)
- Hugging Face Transformers library
- YouTube API Key
- Samplette API Key (if required)

## Installation ⚙️

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/Belus-Beats-Bot.git
   cd Belus-Beats-Bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   Create a `.env` file in the root directory and add your keys:
   ```plaintext
   DISCORD_TOKEN=your_discord_token
   OPENAI_API_KEY=your_openai_api_key
   YOUTUBE_API_KEY=your_youtube_api_key
   SAMPLETTE_API_KEY=your_samplette_api_key
   ```

4. **Run the bot:**
   ```bash
   python belus-beats-bot.py
   ```

## Commands and Usage 🎛️

### Discord Bot Commands

- **GPT-3 Chat**: `!ask [question]` - Ask GPT-3 a question.
- **Sentiment Analysis**: `!sentiment [text]` - Analyze the sentiment of a message.
- **Generate AI Music**: `!generate_music` - Generate a MIDI file using Magenta AI.
- **Daily Song**: `!dailysong` - Fetch a daily song recommendation from YouTube.
- **Samplette Sample**: `!samplette [keyword]` - Get a sample from Samplette.io (use without keyword for a random sample).

### CLI Commands

1. **GPT-3 Chat**:
   ```bash
   python belus-beats-bot.py ask --message "Write a haiku about AI."
   ```

2. **Sentiment Analysis**:
   ```bash
   python belus-beats-bot.py sentiment --message "I love making music!"
   ```

3. **Generate AI Music**:
   ```bash
   python belus-beats-bot.py generate_music
   ```

4. **Daily Song Recommendation**:
   ```bash
   python belus-beats-bot.py dailysong
   ```

5. **Samplette.io Samples**:
   - Random sample:
     ```bash
     python belus-beats-bot.py samplette
     ```
   - Specific sample (e.g., "drums"):
     ```bash
     python belus-beats-bot.py samplette --message "drums"
     ```

## Supported Music Tools 🛠️

Explore and experiment with these open-source tools:
- **AudioStellar** - Explore latent sound structure.
- **BeepBox** - Sketch and share melodies.
- **Bespoke Synth** - Modular synthesizer.
- **Helio Workstation** - Multi-platform music sequencer.
- **LMMS** - Cross-platform DAW.
- **Mixxx** - DJ software.
- **MuseScore** - Sheet music creation.
- **Sonic Pi** - Code-based music creation.

## Contributing 🤝

Contributions are welcome! If you have suggestions for new features, feel free to open an issue or pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy producing! 🎶 Let **Belus Beats Bot** elevate your music journey.
```
