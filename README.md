<div align="center">

# Saline Concentration Analysis

##### Analyzing the saline concentration dynamics over time in a connected sweet lake and salt lake system using numerical methods and phase portraits in Python.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

</div>

## Overview

This repository contains Python scripts for studying the variation of saline concentration over time in a sweet lake connected to a salt lake via a river. The analysis is performed using a system of differential equations, and two different approaches are implemented in separate files.

## Repository Contents

### Main Scripts


1. **EulerDE.py**
   - *Description:* In the `EulerDE.py` file, we employ Euler's method to numerically approximate the concentration changes. This script provides a quantitative analysis of the saline concentration dynamics over time.

2. **PhasePortrait.py**
   - *Description:* The `PhasePortrait.py` file focuses on a qualitative analysis of the concentration changes by utilizing phase portraits. This script provides insights into the system's behavior and its stability over time.


## Usage 

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Make sure you have the following installed on your machine:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/)
- [Numpy](https://numpy.org/)

### Installation

- Clone the repository:

    ```bash
    git clone https://github.com/HumbertoBM2/Saline-Concentration-Analysis
    ```

- Navigate to the project directory:

    ```bash
    cd Saline-Concentration-Analysis
    ```

- Open a terminal and run one of the following commands:

    ```bash
    python EulerDE.py
    ```

    ```bash
    python PhasePortrait.py
    ```

Each application will display an interactive menu guiding you through each step. Follow the instructions of each menu and enjoy.
