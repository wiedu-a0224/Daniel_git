import librosa
import numpy as np
from tacotron.text import text_to_sequence

def preprocess_text(text):
    # Text normalization and conversion to sequence of phonemes
    sequence = text_to_sequence(text, ['basic_cleaners'])
    return sequence

def preprocess_audio(audio_path):
    # Load audio file
    y, sr = librosa.load(audio_path, sr=None)
    # Normalize audio
    y = librosa.util.normalize(y)
    # Convert to mel-spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(y, sr=sr, n_mels=80)
    mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)
    return mel_spectrogram

text = "Hello, how are you?"
audio_path = "path_to_audio_file.wav"

text_sequence = preprocess_text(text)
mel_spectrogram = preprocess_audio(audio_path)
