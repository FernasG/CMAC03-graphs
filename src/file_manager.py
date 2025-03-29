import numpy as np 
from os import path

"""
Read file from datasets folder and create a Numpy Array with file content
"""
def convert_file_to_np_array(filename: str):
    filepath = path.join("datasets", filename)

    f = open(filepath, "rb")
    data = np.genfromtxt(f, dtype="int32")
    f.close()

    return data


"""
Save matrix content into a file and show infos about the matrix
"""
def save_np_array_to_file(instance: str, matrix: np.ndarray, filename: str = "result.txt"):
    filepath = path.join("src", filename)
    nrows, ncols = matrix.shape

    result = f"{instance} {nrows} {ncols}"

    with open(filepath, "w") as f:
        f.write(result)

    print(result)

