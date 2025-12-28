# imports
import os
import sys

# paths
kitty_conf_location = ""
pacman_conf_location = ""
libs = "firefox kitty fish telegram-desktop steam git curl fastfetch wget unzip zenity xdg-desktop-portal-gtk flatpak"

# def's

def install_yay():
	print("Installing yay")
	os.system("python3 yay.py")

def install_chaotic():
	print("Installing Chaotic-Aur")
	os.system("pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com")
	os.system("pacman-key --lsign-key 3056513887B78AEB")
	os.system("sudo pacman -U --noconfirm 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst'")
	os.system("sudo pacman -U --noconfirm 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'")
	with open("/etc/pacman.conf", "r+") as f:
		if "[chaotic-aur]" not in f.read():
			f.write("\n[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist\n")
	os.system("pacman -Sy")

def install_package():
	print("Installing packages...")
	os.system(f"pacman -S --noconfirm {libs}")

def sudo_gain():
	if os.geteuid() != 0:
		print("Use 'sudo python3 installer.py'")
		sys.exit(1)

def install_package_via_yay():
	print("Installing packages via yay...")
	user = os.environ.get('SUDO_USER')
	os.system(f"sudo -u {user} yay -S --noconfirm amneziavpn-bin google-chrome")
	input("Что бы у тебя смог забилдиться opentabletdriver включи VPN, после этого нажми любую клавишу...")
	os.system(f"sudo -u {user} yay -S --noconfirm opentabletdriver")

def setting_kitty():
	print("Setting kitty...")
	url = "https://undershort.s-ul.eu/I2SCZeIc"
	user = os.environ.get('SUDO_USER')
	path = f"/home/{user}/.config/kitty"
	os.system(f"mkdir -p {path}")
	os.system(f"curl -L {url} -o {path}/kitty.conf")
	os.system(f"chown -R {user}:{user} {path}")

def setting_fish():
	print("Setting fish...")
	url = "https://undershort.s-ul.eu/IODIJDi5"
	user = os.environ.get('SUDO_USER')
	path = f"/home/{user}/.config/fish"
	os.system(f"mkdir -p {path}")
	os.system(f"curl -L {url} -o {path}/config.fish")
	os.system(f"chown -R {user}:{user} {path}")

def install_osu():
	print("Installing osu!...")
	user = os.environ.get('SUDO_USER')
	cmd = "git clone https://github.com/NelloKudo/osu-winello.git && cd osu-winello && chmod +x ./osu-winello.sh && ./osu-winello.sh"
	os.system(f"sudo -u {user} bash -c '{cmd}'")

def install_sober():
	print("Installing Sober (Roblox)...")
	user = os.environ.get('SUDO_USER')
	cmd = "flatpak install -y flathub org.vinegarhq.Sober"
	os.system(f"sudo -u {user} bash -c '{cmd}'")

def download_osu_lazer():
	print("Download osu!lazer to /home...")
	user = os.environ.get('SUDO_USER')
	cmd = f"wget -O /home/{user}/osu.AppImage https://github.com/ppy/osu/releases/latest/download/osu.AppImage && chmod +x /home/{user}/osu.AppImage"
	os.system(f"sudo -u {user} bash -c '{cmd}'")

def setting_otd():
	print("Setting OpenTabletDriver...")
	user = os.environ.get('SUDO_USER')
	uid = os.popen(f"id -u {user}").read().strip()
	os.system("echo 'blacklist wacom' > /etc/modprobe.d/blacklist-wacom.conf")
	os.system("rmmod wacom 2>/dev/null")
	os.system("echo 'blacklist hid_uclogic' > /etc/modprobe.d/blacklist-uclogic.conf")
	os.system("rmmod hid_uclogic 2>/dev/null")
	os.system("udevadm control --reload-rules && udevadm trigger")
	cmd = f"export XDG_RUNTIME_DIR=/run/user/{uid} && systemctl --user daemon-reload && systemctl --user enable opentabletdriver --now"
	os.system(f"sudo -u {user} bash -c '{cmd}'")

# call def's
sudo_gain()
install_yay()
install_chaotic()
install_package()
install_package_via_yay()
install_osu()
install_sober()
download_osu_lazer()
setting_kitty()
setting_fish()
setting_otd()
