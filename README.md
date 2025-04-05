# Spiking-Neural-Network (SNN)

This project is an implementation of a basic SNN library that supports simple image classification example.

### Built With

- [scikit-learn](https://scikit-learn.org/stable/install.html)
- [Numpy](https://numpy.org/install/)
- [Matplotlib](https://matplotlib.org/stable/index.html)
- [OpenCV](https://pypi.org/project/opencv-python/)

## Getting Started

### Prerequisites

- Python version 3.11.3 >

  ```sh
  https://www.python.org/
  ```

- Virtualenv

  ```sh
  https://pypi.org/project/virtualenv/
  ```

### Installation

1. Clone the repository

   ```sh
   git clone https://github.com/Albert-Osei/SNN-implementation.git
   ```

2. Create Virtual Environment

   ```sh
   virtualenv .spike-venv
   ```

   OR


   ```sh
   python -m venv spike-venv
   ```

3. Activate Virtual Environment

   ```sh
   source spike-venv\scripts\activate ~ on~windows
   ```

   ```sh
   source spike-venv/bin/. activate ~ on~mac
   ```

4. Install Dependencies

   ```sh
   pip install -r requirements.txt
   ```

### Running

* cd into the root where the project is cloned
* run classification/classify.py
* this command will use pregenerated weights and output the results of classifying the test images

### Weight Reconstruction (Training)

* to reconstruct the weights, run binary_class/learning.py
* this command will generate new weights file and output `neuron[1-3].png` which will show the reconstructed weights. One neuron should look random, the other two will produce a pattern similar to the O, and another a pattern similar to the X.
