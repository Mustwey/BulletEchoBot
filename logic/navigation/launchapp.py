import time

class AppLauncher:
    MAX_RETRIES = 3  # Maximum number of times to retry launching an app

    def __init__(self, adb_manager):
        self.adb_manager = adb_manager

    def _is_app_running(self, package_name):
        return self.adb_manager.is_app_running(package_name)

    def _is_device_connected(self):
        return self.adb_manager.is_device_connected()

    def _is_network_connected(self):
        return self.adb_manager.is_network_connected()

    def _has_enough_storage(self):
        return self.adb_manager.has_enough_storage()

    def launch_app(self, package_name, activity_name):
        # Check if the device is connected
        # Currently the adb_manager gives a broken method for this
#        if not self._is_device_connected():
#            print("Device is not connected. Aborting...")
#            return False

        # Check for network connectivity
        if not self._is_network_connected():
            print("No network connection detected. Aborting...")
            return False

        # Check for sufficient storage
        if not self._has_enough_storage():
            print("Not enough storage space. Aborting...")
            return False

        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                print(f"Launching {package_name}... Attempt {retries + 1}")
                self.adb_manager.launch_app(package_name, activity_name)

                # Wait for a few seconds to allow the app to launch
                time.sleep(3)

                # Check if the app is running
                if self._is_app_running(package_name):
                    print(f"Successfully launched {package_name}")
                    return True
                else:
                    print(f"Failed to verify that {package_name} is running. Retrying...")
                    retries += 1

            except Exception as e:
                print(f"Failed to launch {package_name}. Error: {e}. Retrying...")
                retries += 1

        print(f"Exceeded maximum retries ({self.MAX_RETRIES}) for launching {package_name}. Aborting...")
        return False
