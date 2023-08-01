import subprocess

def get_wifi_passwords():
    try:
        results = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
        profiles = [line.split(":")[1][1:-1] for line in results if "All User Profile" in line]

        wifi_passwords = {}

        for profile in profiles:
            try:
                output = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8")
                password_lines = [line.split(":")[1][1:-1] for line in output.split("\n") if "Key Content" in line]
                wifi_passwords[profile] = password_lines[0]
            except subprocess.CalledProcessError:
                wifi_passwords[profile] = "Password not found."

        return wifi_passwords

    except OSError as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    wifi_passwords = get_wifi_passwords()
    if wifi_passwords:
        print("Saved WiFi Passwords:")
        for wifi_name, password in wifi_passwords.items():
            print(f"WiFi Name: {wifi_name}\tPassword: {password}")
    else:
        print("Failed to retrieve WiFi passwords.")
