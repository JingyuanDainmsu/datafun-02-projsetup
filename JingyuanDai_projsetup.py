''' This module provides functions for creating a series of project folders. '''
import math
import statistics
import Jingyuan_utils
import pathlib
import time

def create_folders_for_range(start_year, end_year):
    ''' This function generates folders for a given range (e.g., years). ''' 
    for year in range(start_year, end_year + 1):
        # Create a folder with the year as the folder name
        folder_name = str(year)
        pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)  
    

def create_folders_from_list(folder_list,to_lowercase=False, remove_spaces=False):
    ''' This function creates folders from a list of names. ''' 
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "")
        path = pathlib.Path(folder_name)
        path.mkdir(parents=True, exist_ok=True)

def create_prefixed_folders(folder_list, prefix):
    '''This function creates prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").'''
    for folder_name in folder_list:
        # Combine the prefix and folder name to create the folder path
        
        folder_path = pathlib.Path(prefix + folder_name)
        folder_path.mkdir(parents=True, exist_ok=True)

def create_folders_periodically(duration):
    '''This function create folders periodically (e.g., one folder every 5 seconds).'''
    # Create a base directory where the folders will be created
    base_dir = pathlib.Path("periodic_folders")
    base_dir.mkdir(parents=True, exist_ok=True)
    total_folders=3

    for i in range(total_folders):
        # Create a folder with a unique name (e.g., based on timestamp)
        folder_name = f"folder_{i}"
        folder_path = base_dir / folder_name
        folder_path.mkdir(exist_ok=True)
        
        # Wait for the specified duration before creating the next folder
        time.sleep(duration)

# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)


def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {Jingyuan_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)


if __name__ == '__main__':
    main()