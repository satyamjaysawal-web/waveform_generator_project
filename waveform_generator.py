import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import csv

# Base class for Waveform
class Waveform(ABC):
    def __init__(self, frequency=1.0, amplitude=1.0, phase=0.0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase

    @abstractmethod
    def generate(self, time):
        pass

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude

    def set_phase(self, phase):
        self.phase = phase


# SineWave class
class SineWave(Waveform):
    def generate(self, time):
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time + self.phase)


# SquareWave class
class SquareWave(Waveform):
    def generate(self, time):
        sine_wave = np.sin(2 * np.pi * self.frequency * time + self.phase)
        return self.amplitude * np.sign(sine_wave)


# Generate waveform data
def generate_waveform_data(waveform, duration=1.0, sample_rate=1000):
    time_values = np.linspace(0, duration, int(sample_rate * duration))
    waveform_values = waveform.generate(time_values)
    return time_values, waveform_values


# Save waveform data to CSV file
def save_waveform_to_csv(time_values, waveform_values, filename="waveform.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Amplitude'])
        for t, v in zip(time_values, waveform_values):
            writer.writerow([t, v])
    print(f"Data saved to {filename}")


# Plot the waveform
def plot_waveform(time_values, waveform_values):
    plt.plot(time_values, waveform_values)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()


# Main function to run the program
def main():
    print("Select waveform type:")
    print("1: Sine Wave")
    print("2: Square Wave")
    choice = int(input("Enter choice (1 or 2): "))

    frequency = float(input("Enter frequency (Hz): "))
    amplitude = float(input("Enter amplitude: "))
    phase = float(input("Enter phase (optional, default 0): ") or 0.0)

    if choice == 1:
        waveform = SineWave(frequency, amplitude, phase)
    elif choice == 2:
        waveform = SquareWave(frequency, amplitude, phase)
    else:
        print("Invalid choice!")
        return

    duration = float(input("Enter duration (seconds, default 1): ") or 1.0)
    sample_rate = int(input("Enter sample rate (samples/second, default 1000): ") or 1000)

    time_values, waveform_values = generate_waveform_data(waveform, duration, sample_rate)

    # Save to CSV or visualize
    save_to_csv = input("Save to CSV? (y/n): ").lower() == 'y'
    if save_to_csv:
        save_waveform_to_csv(time_values, waveform_values)
    else:
        plot_waveform(time_values, waveform_values)


if __name__ == "__main__":
    main()
