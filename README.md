# Study Reminders

A lightweight Discord bot that sends study session reminders.

## Features
- Scheduled reminders for your study plan
- Easy to configure times and messages
- Built with discord.py

### Installation & Setup

The project uses modern Python tooling with **`uv`** (from Astral), which is fast and replaces `pip` + `virtualenv` + `poetry` in many cases.

# Clone the repo
```bash
git clone https://github.com/shaarkz/study-rem.git
cd study-rem
```

# Install dependencies & create virtual environment
```bash
uv sync
```

# Create config.py file and add your token
```bash
echo "TOKEN=your_bot_token_here" > config.py
```

# Run the bot
```bash
uv run python main.py
``` 

## Development

See [Uv Docs](https://docs.astral.sh/uv/) :)