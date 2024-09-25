import subprocess

def get_wifi_adaptor_name():
    command = "netsh wlan show interfaces"
    result = subprocess.run(command,capture_output=True,text=True,shell=True)
    
    if result.returncode == 0:
        output = result.stdout
        for line in output.splitlines():
            if "Name" in line:
                adapter_name = line.split(":")[1].strip()
                return adapter_name
    return None


def disable_wifi(adapter_name):
    if adapter_name:
        command = f"netsh interface set interface \"{adapter_name}\"admin=disabled"
        subprocess.run(command,shell=True)
        print(f"Disabled Wi-Fi adaptor: {adapter_name}")
    else:
        print("No Wi-Fi adaptor found.")

if __name__ == "__main__":
    wifi_adaptar_name = get_wifi_adaptor_name()
    print(f"Wi-Fi Adapter Name: {wifi_adaptar_name}")
    disable_wifi(wifi_adaptar_name)
