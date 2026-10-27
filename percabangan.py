print ("<======NILAI MAHASISWA======")
nama_mhs = input ("Masukan nama:")
kelas = input ("kelas:")


nilai_a= int(input("masukan nilai algoritma:"))
nilai_b = int(input("masukan nilai basisdata:"))
nilai_c = int(input("masukan nilai agama:"))
nilai_d = int(input("masukan nilai bahasaing:"))
nilai_e = int(input("masukan nilaibahasaindo:"))
nilai_f = int(input("masukan nilai pancasila:"))
nilai_g = int(input("masukan nilai logikainformatika:"))
rata_rata = (nilai_a + nilai_b + nilai_c + nilai_d + nilai_e + nilai_f + nilai_g ) / 7

# penentuan lulus atau tidak
if rata_rata >=80 and rata_rata<=100:
    print("Nilai : A")
elif rata_rata >=70 and rata_rata<=80:
    print("Nilai : B")
elif rata_rata >=50 and rata_rata<=70:
    print("Nilai : C")
elif rata_rata >=40 and rata_rata<=60:
    print("Nilai : D")
else:
    print("Nilai : E")