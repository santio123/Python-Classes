import os

s = input("Do you wish to shutdown your computer ? (yes / no)")

if s == 'no':
    exit()
    else:
        os.system("shutdown /s /t 1")