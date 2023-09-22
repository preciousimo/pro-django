import yaml

def yaml_coerce(value):
    # Check if the input value is a string
    if isinstance(value, str):
        # Create a temporary YAML string with a dummy key-value pair
        # This is done to ensure that the string can be loaded as YAML
        # Use SafeLoader to parse the YAML content securely
        parsed_yaml = yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)
        
        # Retrieve the value associated with the 'dummy' key and return it
        return parsed_yaml['dummy']
    
    # If the input value is not a string, return it as is
    return value
