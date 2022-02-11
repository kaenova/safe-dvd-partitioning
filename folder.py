"""
    File ini digunakan untuk menaruh fungsi-fungsi tambahan yang berhubungan dengan sistem file ataupun folder.
"""

import os
import math

def get_reccursive_size(dir: str) -> int:
    """
        Fungsi untuk menjumlahkan total size yang ada pada directory aktif
        
        :param dir: Path yang ingin dilihat
        :type dir: str
        :return: total bit yang ada pada direcotry aktif
        :rtype: int
    """
    size = 0        # In bytes
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
        size += get_reccursive_size(i)
    
    for i in list_file:
        size += os.path.getsize(i)
    
    return size


def human_byte(size_bytes: int) -> str:
    """
        Fungsi untuk melakukan print dari bytes ke dalam bentuk "human readable"
        ref: https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
        
        :param size_bytes: Jumlah bytes
        :type dir: int
        :return: Hasil konversi
        :rtype: str
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])