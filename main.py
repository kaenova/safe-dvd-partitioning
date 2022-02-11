"""
    Program ini akan melakukan pembagian suatu folder yang melebihi kapasitas DVD menjadi beberapa bagian DVD yang aman.
    Yang dimaksud aman ialah, ketika mempunyai banyak part DVD dan ketika salah satu part DVD tersebut hilang, ataupun rusak, maka tidak akan menjadi masalah, karena hanya bagian tersebut saja yang rusak.
    
    Bagaimana jika ada file yang memang memiliki size lebih dari file DVD?
        Hal tersebut akan dipisahkan dalam suatu folder yang tidak dapat di burn.
        
    Apa output dari program ini?
        Beberapa folder yang dimulai dari part 1 hingga part (x) yang siap untuk dilakukan burn dari isi file tersebut 
"""

import os
import shutil
from folder import *
from backup import *
    
if __name__ == "__main__":
    # Get input directory
    DIR = input("Insert your input directory: ")
    if not os.path.exists(DIR):
        print("Directory is not exists")
        exit()
    
    # Input directory size checking
    print("Checking input total size")
    TOTAL_SIZE = get_reccursive_size(DIR)
    print("Total input directory size:",human_byte(TOTAL_SIZE))
    
    # Get output directory
    OUT_DIR = input("Insert your output directory: ")
    if os.path.exists(OUT_DIR):
        print("Out direcotry is available. Will creating backup folder",
                "in existing directory")
    else:
        os.mkdir(OUT_DIR)
        print("New directory craeted at", OUT_DIR)
    
    # Get backup mode
    print("Backup mode:")
    print("1. Copying")
    print("2. Moving")
    BACKUP_MODE = 1
    backup_input = input("Please choose the backup mode (default: 1): ")
    if backup_input == "2":
        BACKUP_MODE = 2
    
    if BACKUP_MODE == 1:
        print("Checking available size for the output directory")
        _, _, free = shutil.disk_usage(OUT_DIR)
        print("Available size:", human_byte(free))
        if free < TOTAL_SIZE:
            print("Not enough storage for copying backup files")
            exit()
    
    print("Currently processing please wait ...")
    backup(DIR, OUT_DIR, BACKUP_MODE)
    print("Done! please check", OUT_DIR)