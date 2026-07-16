# Audio Noise Reduction using Digital Filters (DSP)

A Python-based simulation of electrical filters to remove high-frequency noise from human voice signals. This project was developed as a practical application of Electrical Circuits concepts, utilizing Digital Signal Processing (DSP) techniques instead of physical hardware components.

## 📌 Project Overview
The objective of this project is to process a noisy audio file (corrupted by a harsh 6000 Hz whistle-like noise) and recover the clean human voice. The signal processing pipeline implements mathematical models of analog RLC circuits to achieve high-precision noise cancellation.

## ⚙️ How It Works (Filter Architecture)
The project utilizes a two-stage filtering process:

1. **Notch Filter (6000 Hz):** 
   Acts as a highly selective trap to target and eliminate the specific high-frequency noise spike without affecting the surrounding audio frequencies.
   
2. **10th-Order Butterworth Bandpass Filter (300 - 3400 Hz):** 
   Isolates the standard human voice frequency range. To prevent the **numerical instability** often caused by high-order differential equations, the filter is implemented using **Second-Order Sections (SOS)**. This cascaded architecture guarantees 100% mathematical stability and prevents signal loss.

## 🛠️ Technologies & Libraries
* **Python 3.x**
* **SciPy:** For signal processing, filter design (`butter`, `iirnotch`), and SOS implementation (`sosfiltfilt`).
* **NumPy:** For matrix operations and amplitude normalization.
* **Matplotlib:** For visualizing the time-domain frequency response.

## 🚀 How to Run
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install numpy scipy matplotlib
