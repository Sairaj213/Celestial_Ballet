import yaml
import os

def load_config(filepath="config.yaml"):
    """
    Loads a configuration dictionary from a YAML file.

    Args:
        filepath (str): The path to the YAML configuration file.

    Returns:
        dict: A dictionary containing the configuration settings.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Configuration file not found at: {filepath}")
        
    with open(filepath, 'r') as f:
        config = yaml.safe_load(f)
        
    return config

config_content = """
# Default settings for the Three-Body Simulator

simulation_defaults:
  preset: "figure_eight.json"
  duration_seconds: 20
  time_steps: 2000
  integrator_method: "RK45"

ui_theme:
  default_mode: "dark"
  primary_color: "#636EFA" # Default Plotly blue
  font: "sans-serif"

logging:
  level: "INFO"
  directory: "data/logs"
"""

try:
    with open("config.yaml", "w") as f:
        f.write(config_content)
    print("Successfully created 'config.yaml' file.")
except Exception as e:
    print(f"Error creating config file: {e}")

try:
    app_config = load_config()
    print("\nSuccessfully loaded configuration:")
    from pprint import pprint
    pprint(app_config)
    default_preset = app_config.get('simulation_defaults', {}).get('preset')
    assert default_preset == "figure_eight.json"
    print(f"\nVerification successful. Default preset is: {default_preset}")

except Exception as e:
    print(f"\nAn error occurred during verification: {e}")

