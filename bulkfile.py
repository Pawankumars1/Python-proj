import os

def bulk_rename(directory, prefix, extension):
    count = 1
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            new_name = f"{prefix}{count}.{extension}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            count += 1


directory = "C:\\Users\\HP\\Desktop\\BULKFILES"
prefix = "file"
extension = "txt"
bulk_rename(directory, prefix, extension)
