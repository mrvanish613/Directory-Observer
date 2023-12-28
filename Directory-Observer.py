import time
import logging
import ctypes
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    # Initializes the watcher with the directory to observe
    def __init__(self, dir_to_observe):
        self.observer = Observer()
        self.dir_to_observe = dir_to_observe

    # Runs the observer to monitor the directory
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.dir_to_observe, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("[-] Observer stopped.")
        self.observer.join()

class Handler(FileSystemEventHandler):
    # Handles the event based on its type and prints it
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print(f"[+] Event created -> {event.src_path}")
        elif event.event_type == 'modified':
            print(f"[+] Event modified -> {event.src_path}")

# Checks for administrator permissions
def checkadminperms():
    if ctypes.windll.shell32.IsUserAnAdmin():
        print("[+] Privileges detected")
        return True
    else:
        print("[!] This script requires administrator privileges.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(1)

if __name__ == '__main__':
    checkadminperms()
    # Configures logging format
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s', 
                        datefmt ='%Y-%m-%d %H%M%S')
    
    dir_to_observe = input(r"Directory to observe >> ")
    watcher = Watcher(dir_to_observe)
    watcher.run()
