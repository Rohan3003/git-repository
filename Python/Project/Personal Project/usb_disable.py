import winreg as reg

def disable_usb_ports():
    try:
        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(registry_key, "Start", 0, reg.REG_DWORD, 4)
        reg.CloseKey(registry_key)
        print('USB ports have been disabled.')
    except Exception as e:
        print(f"An error occured as : {e}")


def enable_usb_ports():
    try:
        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(registry_key, "Start", 0, reg.REG_DWORD, 3)
        reg.CloseKey(registry_key)
        print('USB ports have been enabled.')
    except Exception as e:
        print(f"An error occured as : {e}")


if __name__ == "__main__":
    #disable_usb_ports()
    enable_usb_ports()
