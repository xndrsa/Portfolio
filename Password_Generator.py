import random

#opciones para elegir
option1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
option2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="

choice = int(input("Which option do you prefer: 1. - Numbers & Letters >> Example: AFdu45L1qt 2. - Numbers, letters and symbols >> Example: ZIw%0c!cc@Lf*# "))

length_password = int(input("Input the lenght you want for your password: "))

password = ""

if choice == 1:
 for a in range(length_password):
    character = random.choice(option1)
    password += character
else:

 for a in range(length_password):
    character = random.choice(option2)
    password += character

print("Your new password is: " + password)