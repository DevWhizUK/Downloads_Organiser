# Automated File Organizer

## Overview

This script is designed to automate the organization of files within your `Downloads` directory. It monitors the directory for any new or modified files and moves them into appropriate subdirectories based on their file extensions. The subdirectories include `Images`, `Downloaded_Documents`, `Downloaded_Data_Files`, and `Executables_and_Downloaders`. This organization helps maintain a clutter-free `Downloads` directory and ensures that files are easily accessible in their respective categories.

## How It Works

The script uses the `watchdog` library to detect changes in the `Downloads` directory. When a file is detected, it checks the file extension and moves the file to the corresponding subdirectory. If a file with the same name already exists in the destination directory, the script appends a number to the filename to avoid overwriting the existing file. This ensures that all files are uniquely named and safely stored in their designated locations.
