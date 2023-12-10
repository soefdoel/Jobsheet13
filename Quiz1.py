def Guess_number():
    angka_rahasia = 64
    batas = 5
    jawaban = 0

    while jawaban < batas:
        user = int(input("Masukan angka rahasia (1 - 100): "))
        if user == angka_rahasia:
            print("Selamat! Kamu berhasil menemukan angka rahasia")
            break
        elif user < angka_rahasia and user >= (angka_rahasia - 5):
            print("Hampir! Naikkan sedikit lagi!")
            jawaban += 1
        elif user > angka_rahasia and user <= (angka_rahasia + 5):
            print("Hampir! Turunkan sedikit lagi!")
            jawaban += 1
        else:
            print("Salah! Coba lagi")
            jawaban += 1

    else:
        print(f"Maaf, Kamu tidak bisa menemukan angka rahasia, angka rahasianya adalah {angka_rahasia}")


