def deep_update(base_dict, update_with):
    # Iterate through the items in the dictionary to update (update_with)
    for key, value in update_with.items():
        
        # Check if the current value is a dictionary
        if isinstance(value, dict):
            # Get the corresponding value from the base dictionary
            base_dict_value = base_dict.get(key)
            
            # Check if the corresponding value in the base dictionary is also a dictionary
            if isinstance(base_dict_value, dict):
                # If both values are dictionaries, recursively call deep_update to merge them
                deep_update(base_dict_value, value)
            else:
                # If the base dictionary value is not a dictionary, replace it with the new value
                base_dict[key] = value
                
        else:
            # If the current value is not a dictionary, replace it in the base dictionary
            base_dict[key] = value
    
    # Return the updated base dictionary
    return base_dict
