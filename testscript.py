import matplotlib.pyplot as plt
import numpy as np
from simulinkmodel import SimulinkModel

if __name__ == "__main__":
    mdl = SimulinkModel(verbose=True)
    
    # Define model parameters as a dictionary
    params = {}

    params["model_name"] = "testmdl"
    params["c"] = 3.0
    params["f"] = 10.0
    params["ts"] = 10.0

    # Set the model parameters using a dictionary
    mdl.set(params)

    # Run the model with the set parameters
    res = mdl.run()

    scale_factor = 1e-3
    times = np.arange(len(res)) * scale_factor
    plt.plot(times, res)
    plt.title('Simulink output')
    plt.xlabel('Time (s)')
    plt.ylabel('Output')
    plt.show()