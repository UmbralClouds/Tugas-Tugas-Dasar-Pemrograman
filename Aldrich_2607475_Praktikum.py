# def Fibbseq(Time = 10):
#     a = 0
#     b = 1
#     c = 1
#     for i in range(Time):
#        c = a + b
#        print(c)
#        a = c + b
#        print(a)
#        b = a + c
#        print(b)

# loop = int(input("How long does the chain go? "))
# Fibbseq(loop)

def fibonacci_seq(count):
    a, b = 0, 1
    for _ in range(count):
        print(a)
        a, b = b, a + b

loop = int(input("How long does the chain go? "))
fibonacci_seq(loop)

###################################################

def tabung_vol(r, t):
    print(3.14*(r*r)*t)

tabung_vol(1,5)
tabung_vol(3,6)

###################################################

def hitung_total_dan_rata(*angka):
    if not angka:
        return 0, 0
    
    total = sum(angka)
    rata_rata = total / len(angka)
    
    return total, rata_rata

def hitung_statistik(daftar_angka):
    # Calculate total and average
    total = sum(daftar_angka)
    rata_rata = total / len(daftar_angka)
    
    return total, rata_rata

contoh = (1, 0)
nilai_total, nilai_rata = hitung_statistik(contoh)

print("Total:", nilai_total)
print("Rata-rata:", nilai_rata)

###################################################

def validasi_login(password):
    password_benar = "Latihan"
    
    return password == password_benar


def jalankan_sistem_login():
    kesempatan = 3
    login_berhasil = False
    
    while kesempatan > 0:
        print("Masukan username: Daspro2023")
        password_input = input("Masukan password: ")
        
        if validasi_login(password_input):
            print("Anda telah masuk")
            login_berhasil = True
            break
        else:
            kesempatan -= 1
            if kesempatan > 0:
                print(f"Login Salah! Kesempatan Anda {kesempatan}x kali lagi.")
                
    if not login_berhasil:
        print("Anda tidak diperkenankan mengakses aplikasi ini.")

jalankan_sistem_login()


