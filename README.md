# Safe DVD Burner Partitioning

**Permasalahan**  
Kalau misalkan kita ingin melakukan burning DVD yang lebih dari 4.7 GB, biasanya kita akan melakukan pengarsipan dengan menggabungkan seluruh file tersebut menjadi zip/rar multi-part. Sedangkan, jika kita kehilangan salah satu DVD tersebut maka, kita terkadang tidak bisa mengembalikan seluruh data.

**Penyelesaian**  
Disini saya membuat aplikasi dimana user akan memasukkan input direktori yang ingin dilakukan burn ke DVD dan program ini akan melakukan pempartisian dari direktori input menjadi folder yang kurang dari 4.7 GB. Jika ada file yang melebihi 4.7 GB akan dipisahkan secara tersendiri, dikarenakan tidak bisa di burn secara single part.

## How to use it.
*tested on windows  
1. Lakukan `clone` repository github ini.
2. Jalankan python dari `main.py`. Gausah ragu, saya menggunakan native library `python 3.7.2+`
3. Ikuti prosedur yang diminta pada program tersebut.

Example
![image](https://user-images.githubusercontent.com/61568092/153565168-6e82041e-3da7-4426-a9f1-0721a063d182.png)

