import socket

while True:
    try:
        url = str(input("Enter the url:\n>"))
        break
    except:
        print("Please enter a string value")

target = socket.gethostbyname(url)
print(f"Target scanning: {target}")

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except:
    print("Error occurred...")