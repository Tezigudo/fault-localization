import os

def delete_empty_logs(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.log'):
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) == 0:
                    print(f"Deleting empty log file: {file_path}")
                    os.remove(file_path)

directory = "data/rxjava-jdbc/percentage_of_removed_log"
delete_empty_logs(directory)
