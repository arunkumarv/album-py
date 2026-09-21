import os

def get_unique_destination_path(destination_folder, filename):
    """
    Returns a filepath in destination_folder for filename.
    If a file with the same name already exists in destination_folder,
    appends _1, _2, etc., to avoid overwriting.
    """
    base_name, extension = os.path.splitext(filename)
    counter = 1
    target_path = os.path.join(destination_folder, filename)
    
    while os.path.exists(target_path):
        target_path = os.path.join(destination_folder, f"{base_name}_{counter}{extension}")
        counter += 1
        
    return target_path

