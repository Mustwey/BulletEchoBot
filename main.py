from utils.ADBManager import ADBManager
from utils.UIAutomatorManager import UIAutomatorManager
from logic.bullet_echo_bot import BulletEchoBot

def main():
    # Initialize ADBManager
    adb_manager = ADBManager()

    # Setup and connect to device
    if adb_manager.setup("127.0.0.1:5555"):
        print(f"Connected to device {adb_manager.device.serial}")

        # Initialize UIAutomatorManager
        ui_automator_manager = UIAutomatorManager(adb_manager.device.serial)

        # Initialize BulletEchoBot with both ADBManager and UIAutomatorManager
        bullet_echo_bot = BulletEchoBot(adb_manager, ui_automator_manager)

        # Run the bot logic
        bullet_echo_bot.run()
    else:
        print("Failed to connect to the device.")

if __name__ == "__main__":
    main()
