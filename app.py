from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# File destination and source
source_directory = "/Users/devwhizuk/Downloads"
destination_directory_images = "/Users/devwhizuk/Downloads/Images"
destination_directory_documents = "/Users/devwhizuk/Downloads/Downloaded_Documents"
destination_directory_data = "/Users/devwhizuk/Downloads/Downloaded_Data_Files"
destination_directory_executables = "/Users/devwhizuk/Downloads/Executables_and_Downloaders"

# Supported image types
image_extensions = [
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
    ".webp", ".svg", ".heic", ".heif", ".ico", ".psd",
    ".eps", ".ai", ".raw", ".cr2", ".nef", ".orf",
    ".sr2", ".arw", ".dng", ".raf", ".rw2", ".pef", ".3fr",
    ".ptx", ".srw", ".x3f", ".jpf", ".jp2", ".j2k", ".jpx",
    ".jpm", ".pgm", ".ppm", ".pbm", ".pnm", ".hdr", ".exr",
    ".cgm", ".svgz", ".avif"
]

# Supported document types
document_extensions = [
    ".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt",
    ".md", ".wps", ".wpd", ".xls", ".xlsx", ".ods",
    ".ppt", ".pptx", ".key", ".pages", ".epub", ".mobi",
    ".azw", ".azw3", ".ibooks"
]

# Supported data file types
data_extensions = [
    ".csv", ".xml", ".json", ".yaml", ".yml", ".sql",
    ".db", ".dbf", ".mdb", ".accdb", ".sqlite", ".sqlite3",
    ".tsv", ".sav", ".sas7bdat", ".rda", ".rdata"
]

# Supported executables and downloader file types
executable_extensions = [
    ".exe", ".dmg", ".zip"
]

def redundancy_checker(destination, name):
    filename, extension = splitext(name)
    counter = 1
    # If file exists, adds number to the end of the filename
    while exists(f"{destination}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_file(destination, entry, name):
    if exists(f"{destination}/{name}"):
        unique_name = redundancy_checker(destination, name)
        old_name = join(destination, name)
        new_name = join(destination, unique_name)
        move(entry.path, new_name)
        print(f"Moved {entry.path} to {new_name}")
    else:
        move(entry.path, destination)
        print(f"Moved {entry.path} to {destination}")

class DownloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(source_directory) as entries:
            for entry in entries:
                if entry.is_file():
                    name = entry.name
                    file_extension = splitext(name)[1].lower()
                    if file_extension in image_extensions:
                        move_file(destination_directory_images, entry, name)
                    elif file_extension in document_extensions:
                        move_file(destination_directory_documents, entry, name)
                    elif file_extension in data_extensions:
                        move_file(destination_directory_data, entry, name)
                    elif file_extension in executable_extensions:
                        move_file(destination_directory_executables, entry, name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source_directory, recursive=False)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
