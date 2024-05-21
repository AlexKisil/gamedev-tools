# GameDev Tools

A collection of useful tools for game development.

## Audio Normalizer

Audio Normalizer is a Python script that normalizes the volume of all audio files in a specified directory. It supports .wav, .mp3, .mp4, and .ogg file formats.

### Prerequisites

- Python 3.x
- Pydub library

### Installation

1. Clone the repo:
`git clone https://github.com/your-username/gamedev-tools.git`
2. Navigate to the project directory:
`cd gamedev-tools`
3. Install pydub:
`pip install pydub`
### Usage

To normalize audio files in a given directory, run the following command:
`python normalize_audio.py path/to/audio/files/directory`

Replace `path/to/audio/files/directory` with the path to your audio files.

The script will process all the supported audio files in the specified directory and create normalized versions of each file with the prefix `normalized_`. 

### Example
`python normalize_audio.py audio_files`
This command will normalize all the audio files in the `audio_files` directory.

### Notes

- The script ignores files that already have the `normalized_` prefix to avoid duplicate processing.
- Make sure you have the necessary permissions to read and write files in the specified directory.