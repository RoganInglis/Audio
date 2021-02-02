import soundfile as sf

from scipy.signal import spectrogram

def plot_spectrogram(filename, length=10):
    # Load audio
    data, rate = sf.read(filename)

    # Crop to length
    data = data[:, :rate*length]

    # Compute spectrogram


    # Plot
