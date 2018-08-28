import os
import time
import threading


class FolderMonitor(threading.Thread):
    def __init__(self, directory):
        threading.Thread.__init__(self)
        self.directory = directory
        self.files = set(os.listdir(path=self.directory))
        self.active = True

    def run(self):
        while self.active:
            time.sleep(0.001)
            self.current_files = set(os.listdir(path=self.directory))
            self.added = self.current_files - self.files
            self.deleted = self.files - self.current_files
            self.files = self.current_files
            self.status()

    def start_checking(self):
        self.active = True


    def status(self):
        if self.added:
            print('Added:\n', self.added)
        if self.deleted:
            print('Deleted:\n', self.deleted)

    def stop_checking(self):
        self.active = False


