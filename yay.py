import os
import sys

user = os.environ.get('SUDO_USER')

if not user:
    sys.exit(1)

os.system("pacman -S --needed --noconfirm git base-devel")
os.system("rm -rf yay")
os.system("git clone https://aur.archlinux.org/yay.git")
os.system(f"chown -R {user}:{user} yay")
os.system(f"cd yay && sudo -u {user} makepkg -si --noconfirm")
