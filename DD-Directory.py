"""
Calculates the total size of a directory and its subdirectories

#Questions? 
1. What is the stimated size of the directory?

2. Is it necesary to use symbolic directories? (infinity loop)

3. We need to return the size in specific format?

4. Is there any specific language that i need to code with?

I feel more comfortable using Python as it has already some libraries
that can help me , such as os , os.path.


Approach
1. Naive
def calculate_directory_size given a directory
For loop using the root directory as argument,iterating an looking at
each file and subdirectory in it.
varaible counter→ total_size → int 0
library methods loop.os() -  
O(n)


"""
#Import the libraries
import os 
import os.path
import math
#from hurry.filesize import size

def calculate_directory_size(directory):
    total_size = 0

    # Recorremos el directorio usando os.walk()
    for dirpath, dirnames, filenames in os.walk(directory):
        print(f"Calculando el tamaño de {dirpath}")
        print(f"Directorios: {dirnames}")
        print(f"Archivos: {filenames}")
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            print(f"Calculando el tamaño de {filepath}")
            # Verificamos que el archivo sea válido y no un enlace roto
            if os.path.isfile(filepath):
                total_size += os.path.getsize(filepath) # Sumamos el tamaño del archivo al tota

    return total_size



# # Ejemplo de uso
# directory_path = "C:/Users/Usuario/Desktop/TelecomParis/3A/Stage"
# size_in_bytes = calculate_directory_size(directory_path)
# #size_in_bytes = size(size_in_bytes)
# print(f"El tamaño total del directorio es: {size_in_bytes} bytes")
"""
def convert size ( bytes)
    if size == 0:
        return "0B"
    size = ('B','KB')



import from size
size(1000)

2. Optimize solution
"""

import os

def calculate_directory_size_tree(directory):
    directory_tree = {}

    for dirpath, dirnames, filenames in os.walk(directory): #os.walk() returns a generator that yields a 3-tuple 
        #containing the directory path, the subdirectories in the directory, and the files in the directory.
        subdir_and_files = {
            'subdirectories': dirnames,
            'files': {}
        }#dictionary to store subdirectories and files in the current directory
        for filename in filenames: #Iterating over the files in the current directory
            filepath = os.path.join(dirpath, filename) #Joining the directory path with the filename to get the full path
            if os.path.isfile(filepath): #Checking if the file is valid and not a broken symlink
                subdir_and_files['files'][filename] = os.path.getsize(filepath) #Adding the file and its size to the dictionary

        directory_tree[dirpath] = subdir_and_files #Adding the current directory and its contents to the directory tree
    return directory_tree #Returning the directory tree



"""
3. Paralelize solution
"""

import os
import concurrent.futures


# Function to calculate the size of an individual file
def calcuate_file_size(filepath):
    if os.path.isfile(filepath): #Checking if the file is valid and not a broken symlink
        return os.path.getsize(filepath)
    return 0 #Return 0 if the file is not valid

def calculate_directory_size_tree(directory):
    directory_tree = {}

    with concurrent.futures.ThreadPoolExecutor() as executor: #Creating a ThreadPoolExecutor
        future_to_file = {} #Dictionary to store the future objects
        for dirpath, dirnames, filenames in os.walk(directory): #os.walk() returns a generator that yields a 3-tuple 
            #containing the directory path, the subdirectories in the directory, and the files in the directory.
            subdir_and_files = {
                'subdirectories': dirnames,
                'files': {}
            }#dictionary to store subdirectories and files in the current directory
            for filename in filenames: #Iterating over the files in the current directory
                filepath = os.path.join(dirpath, filename) #Joining the directory path with the filename to get the full path
                if os.path.isfile(filepath): #Checking if the file is valid and not a broken symlink
                    subdir_and_files['files'][filename] = calcuate_file_size    (filepath) #Adding the file and its size to the dictionary

            directory_tree[dirpath] = subdir_and_files #Adding the current directory and its contents to the directory tree

        for future in concurrent.future.as_completed(future_to_file): #Iterating over the future objects
            dirpath, filename = future_to_file[future] #Getting the directory path and filename from the future object
            try:
                file_size = future.result() #Getting the result of the future object
                directory_tree[dirpath]['files'][filename] = file_size #Adding the file and its size to the directory tree
            except Exception as exc: #Handling exceptions
                print(f'File {filename} generated an exception: {exc}')

        return directory_tree #Returning the directory tree


