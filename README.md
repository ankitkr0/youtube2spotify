# YouTube to Spotify Converter

Welcome to the YouTube to Spotify Converter! This handy tool watches for any YouTube Music links you copy to your clipboard and instantly transforms them into Spotify links for your convenience.

https://github.com/ankitkr0/youtube2spotify/assets/162094577/0a746510-171b-4257-accb-ab64db1b54d3

## Getting Started: A Step-by-Step Guide

We've made setting up this tool as straightforward as possible, so you don't need to be a developer to get it up and running! Just follow these simple steps:

### Step 1: Check Your Python Version

This project runs on Python, so you'll need to have it installed on your computer. Specifically, you need Python version 3.6 or newer. If you're not sure what version of Python you have, or if you need to install it, here's how you can check:

- Open your command line or terminal.
- Type `python --version` and press Enter.
- If you see a version number starting with 3.6 or higher, you're all set! If not, or if you see an error message, you'll need to install Python. Visit [python.org](https://www.python.org/downloads/) for download instructions and select the version that's right for your operating system.

### Step 2: Download the Project

Next, you'll need to get a copy of this project onto your computer. This process is called "cloning" in Git terminology. Don't worry; it's quite simple:

- If you don't already have Git installed, you'll need to install it. You can download it from [git-scm.com](https://git-scm.com/downloads).
- Once Git is installed, open your command line or terminal.
- Navigate to the folder where you want to download the project. Use the `cd` command to change directories. For example, if you want to download it to your Desktop, you might type `cd Desktop`.
- Now, type the following command and press Enter: `git clone https://github.com/your-username/YouTube-to-Spotify-Converter.git` (Note: replace "your-username" with the actual username where the project is hosted).
- The project will be downloaded to your chosen directory.

### Configuration

Before you start using the YouTube to Spotify Converter, you need to configure it with your own API keys. This project requires API keys for both YouTube and Spotify to function correctly.

- **YouTube API Key**: You'll need a YouTube Data API key to fetch video details from YouTube. You can obtain this key from the [Google Cloud Console](https://console.cloud.google.com/).
- **Spotify API Key**: This project also requires a Spotify API key (Client ID and Client Secret) to interact with the Spotify Web API. You can get these keys from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

Once you have obtained your API keys, open the `config.py` file located in the root directory of this project. Replace the placeholder values with your actual API keys as shown below:

Make sure to save your changes to `config.py`. With your API keys configured, you're now ready to start converting YouTube Music links to Spotify links!

--------

Once done, just run python3 main.py to start using the tool.
