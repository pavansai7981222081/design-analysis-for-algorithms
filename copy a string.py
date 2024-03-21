def copy_string(source, destination, index=0):
    """
    Recursively copies characters from source string to destination string.
    
    Parameters:
    source (str): The string to copy from.
    destination (str): The string to copy to.
    index (int): The index of the current character being copied.
    """
    if index == len(source):
        return destination
    
    destination += source[index]
    
    return copy_string(source, destination, index + 1)


source_string = "Hello, world!"
destination_string = ""
copied_string = copy_string(source_string, destination_string)
print("Source String:", source_string)
print("Copied String:", copied_string)
