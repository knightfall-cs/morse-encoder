from pydub import AudioSegment
from pydub.generators import Sine

# Define audio settings
sample_rate = 44100  # Sample rate in Hz (standard for audio)
dot_duration_ms = 50  # Duration of a dot in milliseconds
dash_duration_ms = 3 * dot_duration_ms  # Duration of a dash (3 times the dot duration)

# Create a sine wave for a dot
dot_sine_wave = Sine(1000).to_audio_segment(duration=dot_duration_ms)

# Create a sine wave for a dash
dash_sine_wave = Sine(1000).to_audio_segment(duration=dash_duration_ms)

# Export the sine waves as audio files
dot_sine_wave.export("dot.wav", format="wav")
dash_sine_wave.export("dash.wav", format="wav")

print("dot.wav and dash.wav audio files have been created.")