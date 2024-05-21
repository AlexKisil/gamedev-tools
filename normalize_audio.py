import os
import sys
from pydub import AudioSegment, effects

def normalize_audio_files(directory):
    supported_extensions = [".wav", ".mp3", ".mp4", ".ogg"]
    
    for filename in os.listdir(directory):
        if filename.startswith("normalized_"):
            continue  # Skip files with "normalized_" prefix
        
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            
            if extension.lower() in supported_extensions:
                print(f"Normalizing {filename}...")
                
                audio = AudioSegment.from_file(file_path, format=extension[1:])
                normalized_audio = effects.normalize(audio)
                
                normalized_filename = f"normalized_{filename}"
                normalized_file_path = os.path.join(directory, normalized_filename)
                
                normalized_audio.export(normalized_file_path, format=extension[1:])
                
                print(f"Normalized audio exported as {normalized_filename}")
    
    print("Audio normalization complete.")

# Check if the file path argument is provided
if len(sys.argv) < 2:
    print("Please provide the directory path as a command-line argument.")
    sys.exit(1)

# Get the directory path from the command-line argument
audio_directory = sys.argv[1]

# Run the audio normalization
normalize_audio_files(audio_directory)