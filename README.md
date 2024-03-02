
# Simulink Model Integration with Python

This repository contains a Python wrapper for running Simulink models from MATLAB within a Python environment. It enables setting parameters for a Simulink model, running simulations, and retrieving results for further analysis in Python. The wrapper uses MATLAB Engine API for Python to interact with MATLAB.

## Contents

- `simulinkmodel.py`: A Python class that serves as a wrapper for interacting with Simulink models through MATLAB's Engine API.
- `mdl_wrapper.m`: A MATLAB script that is called by the Python wrapper to set parameters, run the Simulink model, and return simulation results.
- `testscript.py`: An example Python script demonstrating how to use the `SimulinkModel` class to run a simulation and plot the results.
- `testmdl.slx`: A simple Simulink model used in the provided `testscript.py`.

## Prerequisites

- MATLAB with Simulink: Ensure you have MATLAB installed with Simulink and the MATLAB Engine API for Python configured properly.
- Python: A Python environment with version 3.9, 3.10, or 3.11.
- Required Python packages: `matlabengine`, `json`, `numpy`, `matplotlib`.

## Setup

2. **Clone the Repository**: Clone or download this repository to your local machine.

   ```bash
   git clone <repository-url>
   cd PySimLink
   ```

3. **Install Python Dependencies**: Ensure you have the required Python packages installed. You can install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Example

2. **Run the Example Script**: Execute `testscript.py` to run the simulation. This script sets up model parameters, runs the simulation, and plots the results using matplotlib.

   ```bash
   python testscript.py
   ```

## Usage Example

To use the `SimulinkModel` class to run a Simulink simulation from Python, follow these steps:

1. **Initialize the SimulinkModel**: Create an instance of the `SimulinkModel` class. You can enable verbose mode to get detailed logs.

    ```python
    mdl = SimulinkModel(verbose=True)
    ```

2. **Define Model Parameters**: Set up your model parameters as a dictionary. This includes specifying the model name and any other simulation parameters required by your model. The parameter `model_name` is mandatory.

    ```python
    params = {}

    params["model_name"] = "testmdl"
    params["c"] = 3.0
    params["f"] = 10.0
    params["ts"] = 10.0
    ```

3. **Set the Parameters**: Use the `set` method of your `SimulinkModel` instance to pass the parameters to your model.

    ```python
    mdl.set(params)
    ```

4. **Run the Simulation**: Call the `run` method to execute the simulation. The results will be returned as a NumPy array which you can then use for further analysis or plotting.

    ```python
    res = mdl.run()
    ```

This example demonstrates how to integrate MATLAB Simulink simulations into a Python workflow, allowing for dynamic parameter tuning and analysis of simulation results in Python.

## Notes

- The `SimulinkModel` class and `mdl_wrapper.m` script are designed to work with generic Simulink models. You may need to adjust them based on the specific requirements of your model.
- Ensure that MATLAB is correctly configured and accessible from your Python environment.
- The example provided in `testscript.py` is a basic demonstration. Modify the parameters and the script according to your Simulink model's needs.
