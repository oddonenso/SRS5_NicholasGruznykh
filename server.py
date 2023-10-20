import socket

new_socket = socket.socket()
new_socket.bind(("127.0.0.1", 50))
new_socket.listen()

print("Сервер запущен")
name = input('Введите свое имя: ')
conn, addr = new_socket.accept()

print(name + ' присоединился')

conn.send(name.encode())

while True:
    message = conn.recv(1024).decode()
    print(name, ':', message)
    message = input('Я: ')
    conn.send(message.encode())