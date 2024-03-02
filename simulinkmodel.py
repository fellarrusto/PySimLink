import matlab.engine
import json
import numpy as np

class SimulinkModel:
    def __init__(self, verbose=False):
        
        self.parameters_json = None
        self.verbose = verbose  # Store the verbose flag

        if self.verbose:
            print("MATLAB engine starting...")

        self.eng = matlab.engine.start_matlab()
        
        if self.verbose:
            print("MATLAB engine started")

    def set(self, parameters_dict):
        self.parameters_json = json.dumps(parameters_dict)
        if self.verbose:
            print("Parameters set:", self.parameters_json)

    def run(self):
        if self.parameters_json is None:
            raise ValueError("Model parameters have not been set.")
        
        if self.verbose:
            print("Running the model with parameters:", self.parameters_json)
        
        # Run the model in Simulink
        results = self.eng.mdl_wrapper(self.parameters_json, nargout=1)
        
        if isinstance(results, list):
            results = np.array(results)
        
        if self.verbose:
            print("Model run completed. Results obtained.")
        
        return results

    def __del__(self):
        self.eng.quit()
        if self.verbose:
            print("MATLAB engine stopped")
