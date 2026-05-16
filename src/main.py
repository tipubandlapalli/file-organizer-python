import os
import shutil

EXTENSION_MAP = {
    "FILEs":[".pdf", ".docs"],
    "IMAGEs":[".jpeg", ".jpg"],
    "TextFiles": [".txt"]
}
def dst_folder(file):
    ext = os.path.splitext(file)[1]
    for folder, file_types in EXTENSION_MAP.items():
        if ext in file_types:
            return folder
    return None
def sort_files(folder_path):
    for file in os.listdir(folder_path):            
        src = os.path.join(folder_path, file)
        if os.path.isfile(src) and (dst:= dst_folder(file)):
            os.makedirs(os.path.join(folder_path, dst), exist_ok=True)
            dst = os.path.join(folder_path, dst, file)

            shutil.move(src, dst)

            print(f"{file} --> {dst}")
    

if __name__ == "__main__":
    folder = input("Enter the folder").strip() or os.getcwd()
    if folder and not os.path.isdir(folder):
        print("Invalid folder path")
    
    sort_files(folder)
    print("Done !!!")
    