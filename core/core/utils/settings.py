import os
from .misc import yaml_coerce

def get_settings_from_environment(prefix):
    # Calculate the length of the prefix string
    prefix_len = len(prefix)
    
    # Create a dictionary comprehension to extract settings from environment variables
    # This comprehension iterates over key-value pairs in the environment variables
    # and includes them in the resulting dictionary if the key starts with the specified prefix.
    # The values associated with the keys are also coerced using the yaml_coerce function.
    return {
        key[prefix_len:]: yaml_coerce(value)
        for key, value in os.environ.items() if key.startswith(prefix)
    }
