"""
    File ini digunakan untuk menaruh fungsi ataupun kelas yang dibutuhkan yang berhubungan dalam proses backup
"""

import os
import shutil

class BackupFolder:
    def __init__(self, base_input:str, out_dir:str, 
                 suffix:str, mode: int, max_size: int):
        self.size = 0 # In bytes
        self.base_out = out_dir+"\\Backup"+str(suffix)
        self.base_input = base_input
        self.mode = mode
        self.max_size = max_size
        if not os.path.exists(self.base_out):
            os.mkdir(self.base_out)
        
    def is_full(self, file_dir:str) -> bool:
        if os.path.getsize(file_dir) + self.size > self.max_size:
            return True
        return False
    
    def backup(self, file_dir:str):
        self.size += os.path.getsize(file_dir)
        
        stripped = file_dir.replace(self.base_input, "")
        folder_lst = stripped.split("\\")[1:]
        file_name = folder_lst.pop()
        temp = self.base_out
        
        for i in folder_lst:
            if not os.path.exists(temp+"\\"+i):
                os.mkdir(temp+"\\"+i)
            temp += "\\"+i
        
        if self.mode == 1:
            shutil.copy(file_dir, temp)
        if self.mode == 2:
            shutil.move(file_dir, temp)

class BackupFolderManager:
    MAX_DVD_SIZE = 4598669056 # In bytes
    def __init__(self, inp_dir, out_dir, mode):
        self.folders = []
        self.backup_num = 1
        self.out_dir = out_dir
        self.inp_dir = inp_dir
        self.mode = mode
        
        # Initializing Backup Folders
        self.add_backup_folder()
        self.unbackupable_folder = BackupFolder(self.inp_dir, self.out_dir,
                                                " Unbackupable", self.mode, 
                                                self.MAX_DVD_SIZE)
        
    def add_backup_folder(self):
        self.folders.append(BackupFolder(self.inp_dir, self.out_dir, 
                                         str(self.backup_num), self.mode,
                                         self.MAX_DVD_SIZE))
        self.backup_num += 1
        
    def get_latest_folder(self) -> BackupFolder:
        return self.folders[len(self.folders) - 1]
    
def traverse_one_go(dir: str, mng: BackupFolderManager):
    """
        Fungsi rekursi ini digunakan untuk melakukan pemindahan file secara satu per satu
        
        :param dir: direktori aktif yang dikunjungi
        :param mng: Backup Folder Manager yang digunakan untuk melakukan pembackupan 
    """
    print("Looking at", dir)
    list_dir = []
    list_file = []
    dir_items = os.listdir(dir)
    for i in dir_items:
        target = dir+"\\"+i
        if os.path.isfile(target):
            list_file.append(target)
        elif os.path.isdir(target):
            list_dir.append(target)        
            
    for i in list_dir:
        traverse_one_go(i, mng)
        
    # Backup files
    for i in list_file:
        if os.path.getsize(i) >= mng.MAX_DVD_SIZE:
            mng.unbackupable_folder.backup(i)
        else:
            backup_folder = mng.get_latest_folder()
            if backup_folder.is_full(i):
                mng.add_backup_folder()
                backup_folder = mng.get_latest_folder()
            backup_folder.backup(i)
        
def backup(inp_dir:str, out_dir:str, mode: int):
    """
        Fungsi ini digunakan untuk membuat backup yang tergantung dengan mode yang dipilih.
        
        :param inp_dir: direktori folder yang akan dipecah
        :param out_dir: direktori tujuan
        :param mode: 1: Copy 2: Move
    """
    backup_mng = BackupFolderManager(inp_dir, out_dir, mode)    
    traverse_one_go(inp_dir, backup_mng)