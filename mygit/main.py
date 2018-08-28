from folder_monitor import FolderMonitor
repo = FolderMonitor('D:\dimarepo')
repo.start()
while True:
    command = input()
    if command == 'start':
        repo.start_checking()
    if command == 'stop':
        repo.stop_checking()