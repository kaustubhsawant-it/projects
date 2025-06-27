import os 
import logging
import shutil
from pathlib import Path

print("Choose your choice of function from the following:\n 1. Print Files and Folders in path \n 2. Print name and extension of a file \n 3. Move File \n File Errors and Logs in file_org.log")
input_case = int(input("Enter your choice (1-3): "))

def get_file_name(x):
    return os.path.splitext(x)[0].lower()

def get_file_ext(x):
    return os.path.splitext(x)[1].lower()

match (input_case):
    case 1: 
        folder_path = input("Enter the folder path: ")
        for x in os.listdir(folder_path):
            print(f"{x}")
    case 2: 
        folder_path = input("Enter the folder path: ")
        for x in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, x)):
                print(f"{x}= {get_file_name(x)} - {get_file_ext(x)}")
    case 3: 
        
    case default:
        print("Wrong Input!! Try Again")
