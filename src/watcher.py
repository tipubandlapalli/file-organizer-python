import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BufferHandler(FileSystemEventHandler):
    def on_created(self, event):
        # ignore when not file
        if event.is_directory:
            return
        
        file_path = event.src_path
        file_name = os.path.basename(file_path)

        time.sleep(1)

        print(f"file created {file_name}")

        try:
            os.remove(file_path)
        except Exception as e:
            print("error while deleting", e)

if __name__ == "__main__":
    path = input("enter path").strip() or os.getcwd()

    if not os.path.isdir(path):
        print("invalid path")
        exit(1)
    
    handler = BufferHandler()
    observer = Observer()

    observer.schedule(handler, path=path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
