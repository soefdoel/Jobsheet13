# Sistem Konversi Berat
def Weight_conversion():
    berat = int(input("Masukan berat badan anda: "))
    tipe = input("Lbs atau Kg:")

    if tipe.upper() == "K":
        print(f"Berat badan anda adalah {round(berat * 2.205)} Pound")
    elif tipe.upper() == "L":
        print(f"Berat badan anda adalah {round(berat / 2.205)} Kg")
    else:
        print("Tipe salah!")

