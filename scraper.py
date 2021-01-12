import socket

print(" ______     ______     ______     ______     ______   ______   ______     ______   ") 
print("/\  ___\   /\  ___\   /\  == \   /\  __ \   /\  == \ /\  == \ /\  ___\   /\  == \  ") 
print("\ \___  \  \ \ \____  \ \  __<   \ \  __ \  \ \  _-/ \ \  _-/ \ \  __\   \ \  __<  ") 
print(" \/\_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\    \ \_\    \ \_____\  \ \_\ \_\ ")
print("  \/_____/   \/_____/   \/_/ /_/   \/_/\/_/   \/_/     \/_/     \/_____/   \/_/ /_/ ")
print("\n Version : 1.0 \n \n")



hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


print(f"Bienvenido - {hostname}")
print(f"Tu dirreción ip es - {ip}")
