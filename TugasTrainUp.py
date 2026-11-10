Name = input("Masukkan Nama Lengkap Anda : ")
NIM = int(input("Masukkan NIM Anda : "))
Class_ID = input("Masukkan Kelas Anda : ")
Program = input("Masukkan Program Studi Anda : ")
Age = int(input("Masukkan Umur : "))
Phone = input("Masukkan No. Telpon Anda : ")

DATA = ( Name, NIM, Class_ID, Program, Age, Phone )

print("Data anda : ")

for data in DATA:
    print(f"{data}")
