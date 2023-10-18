from logic.navigation.launchapp import *
from logic.monitoring import *
from logic.actions import *

class BulletEchoBot:
    def __init__(self, adb_manager, ui_automator_manager):
        self.adb_manager = adb_manager
        self.ui_automator_manager = ui_automator_manager
        self.app_launcher = AppLauncher(adb_manager)

    def run(self):        
        self.app_launcher.launch_app("com.zeptolab.bulletecho.google", "com.zf3.GameActivity")
