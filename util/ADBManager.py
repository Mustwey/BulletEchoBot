import subprocess
from ppadb.client import Client as AdbClient
import re

class ADBManager:
    def __init__(self, host="127.0.0.1", port=5037):
        self.host = host
        self.port = port
        self.adb_client = None
        self.device = None

    def start_server(self):
        subprocess.run(["adb", "start-server"])

    def initialize_client(self):
        self.adb_client = AdbClient(host=self.host, port=self.port)

    def connect_device(self, device_address):
        subprocess.run(["adb", "connect", device_address])
        devices = self.adb_client.devices()
        if not devices:
            return False
        self.device = devices[0]
        return True

    def is_device_connected(self):
        devices = self.adb_client.devices()
        print(devices)
        return bool(devices) and self.device in devices

    def is_network_connected(self):
        output = self.device.shell("ping -c 1 8.8.8.8")
        return "1 packets transmitted, 1 received" in output

    def is_app_running(self, package_name):
        output = self.device.shell(f"pm list packages {package_name}")
        return package_name in output

    def launch_app(self, package_name, activity_name):
        self.device.shell(f"am start -n {package_name}/{activity_name}")

    def get_device_info(self):
        return self.device.get_properties()

    def push_file(self, source, destination):
        self.device.push(source, destination)

    def pull_file(self, source, destination):
        self.device.pull(source, destination)

    def install_app(self, apk_path):
        self.device.install(apk_path)

    def uninstall_app(self, package_name):
        self.device.uninstall(package_name)

    def input_text(self, text):
        self.device.shell(f"input text {text}")

    def press_key(self, key_code):
        self.device.shell(f"input keyevent {key_code}")

    def take_screenshot(self, save_path):
        self.device.screencap(save_path)

    def get_logs(self, log_path):
        logcat = self.device.shell("logcat -d")
        with open(log_path, "w") as f:
            f.write(logcat)

    def setup(self, device_address):
        self.start_server()
        self.initialize_client()
        return self.connect_device(device_address)

    def has_enough_storage(self):
        output = self.device.shell("df /data")
        lines = output.strip().split("\n")
        for line in lines:
            if "/data" in line:
                match = re.search(r'(\d+)\s+\d+%\s+/data', line)
                if match:
                    available_storage_kb = int(match.group(1))
                    return available_storage_kb >= 10240
        return False
