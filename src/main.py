import file_manager

if __name__ == "__main__":
    filename = input("Type file name: ")

    matrix = file_manager.convert_file_to_np_array(filename)
    file_manager.save_np_array_to_file(filename, matrix)
    
