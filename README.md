# Discord Screen Monitor

A simple Python project that captures screenshots from a computer and sends them to a private Discord channel using a Discord bot.

## 💻 About the Project

The original idea came from a situation where a school class is divided into two or more groups that take the same test at different times.

This inspired an experiment with remote screen monitoring and Discord automation. The concept explored whether screenshots could be transferred between two computers without requiring them to be connected to the same local network.

The project is intended for cybersecurity education and testing on computers where the user has explicitly authorized screen capture.

## ⚙️ How It Works

1. The Python script connects to Discord using a bot token.
2. The bot automatically creates a new text channel named `session-DD-MM-YYYY`.
3. It sends a startup message containing the current date and time.
4. The bot listens for commands in its session channel.
5. When the `start` command is received, it begins capturing screenshots.
6. Screenshots are uploaded directly to the Discord channel approximately every few seconds.

### Communication Flow

```text
        COMPUTER
            |
      Python Script
            |
     Screenshot Capture
            |
       Discord API
            |
     Discord Bot Server
            |
    #session-DD-MM-YYYY
            |
      Screenshot Images
```

## 🚀 Features

- Automatic Discord channel creation
- Date and time logging
- Remote command handling
- Screenshot capture using Pillow
- Automatic screenshot uploads
- Temporary screenshot file cleanup
- Asynchronous programming with asyncio
- Communication across different networks

## 🛠️ Technologies

**Language:** Python 3

**Libraries:**
- discord.py
- Pillow
- asyncio
- tempfile
- pathlib
- datetime
- os

## 🔒 Security & Disclaimer

This project is a proof of concept for learning Python, Discord API integration, and remote monitoring.

Screen capture must only be performed on devices with the owner's or administrator's explicit permission.

Do not use this software to monitor other users without consent, capture confidential information, or obtain school examination materials without authorization.

## 📌 Project Status

**Experimental / Proof of Concept**

Created for educational cybersecurity research and Python programming practice.