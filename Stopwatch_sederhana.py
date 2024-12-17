# Stopwatch Sederhana
import time

def main():
    print("\nStopwatch Sederhana")
    while True:
        print("\nPilih opsi:")
        print("1. Mulai stopwatch")
        print("2. Keluar")

        pilihan = input("Pilih menu (1-2): ")
        if pilihan == "2":
            print("Terima kasih telah menggunakan stopwatch. Sampai jumpa!")
            break

        if pilihan == "1":
            input("Tekan Enter untuk memulai stopwatch...")
            mulai = time.time()
            input("Tekan Enter lagi untuk menghentikan stopwatch...")
            selesai = time.time()
            durasi = selesai - mulai
            print(f"Waktu yang tercatat: {durasi:.2f} detik")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
