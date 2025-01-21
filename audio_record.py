import pyaudio
import wave

def record_audio(file_name="output.wav", duration=5, channels=1, rate=44100, chunk=1024):
    """
    Records audio for the specified duration and saves it as a .wav file.

    :param file_name: Name of the output audio file
    :param duration: Duration of the recording in seconds
    :param channels: Number of audio channels (1 for mono, 2 for stereo)
    :param rate: Sampling rate (standard is 44100 Hz)
    :param chunk: Buffer size for audio frames
    """
    audio = pyaudio.PyAudio()

    print("Recording started...")

    # Open the audio stream
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=channels,
        rate=rate,
        input=True,
        frames_per_buffer=chunk
    )

    frames = []

    # Record for the specified duration
    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    print("Recording finished.")

    # Save the recorded frames as a .wav file
    with wave.open(file_name, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {file_name}")
    return file_name

# # Record a 5-second audio clip
# record_audio()

import speech_recognition as sr

def audio_to_text(file_name):
    """
    Converts an audio file to text using the SpeechRecognition library.

    :param file_name: Path to the audio file
    """
    recognizer = sr.Recognizer()

    try:
        # Load the audio file
        with sr.AudioFile(file_name) as source:
            print("Processing the audio...")
            audio_data = recognizer.record(source)

        # Recognize and convert to text
        text = recognizer.recognize_google(audio_data)
        print("Converted Text: ")
        print(text)
        return text

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except FileNotFoundError:
        print("Audio file not found. Please check the file path.")

# Convert saved audio file into text
# audio_to_text("output.wav")