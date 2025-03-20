import os

def check_sudo_perms():
    sudo_perms = os.popen("sudo -l").read()
    return sudo_perms if "NOPASSWD" in sudo_perms else "No obvious misconfigurations"

def check_world_writable():
    writable_dirs = os.popen("find / -type d -perm -0002 2>/dev/null").read()
    return writable_dirs if writable_dirs else "No world-writable directories found"

if __name__ == "__main__":
    print("🔍 Checking sudo privileges...")
    print(check_sudo_perms())
    print("\n🔍 Scanning for world-writable directories...")
    print(check_world_writable())
