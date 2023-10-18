from uiautomator import Device

class UIAutomatorManager:
    def __init__(self, device_serial):
        self.ui_device = Device(device_serial)

    # Element Interactions
    def click_button(self, text):
        self.ui_device(text=text).click()

    def click_by_desc(self, desc):
        self.ui_device(description=desc).click()

    def long_click(self, text):
        self.ui_device(text=text).long_click()

    def swipe(self, direction):
        self.ui_device.swipe(direction)

    # Element Inspection
    def find_element(self, key, value):
        return self.ui_device(**{key: value})

    def find_elements(self, key, value):
        return self.ui_device(**{key: value}).all()

    def find_by_text(self, text):
        return self.ui_device(text=text)

    def find_by_desc(self, desc):
        return self.ui_device(description=desc)

    def find_by_class(self, class_name):
        return self.ui_device(className=class_name)

    # Screen Navigation
    def scroll(self, direction):
        self.ui_device(scrollable=True).scroll(direction)

    def fling(self, direction):
        self.ui_device(scrollable=True).fling(direction)

    # UI Monitoring
    def element_exists(self, text):
        return self.ui_device(text=text).exists

    def wait_for_element(self, text, timeout=5000):
        return self.ui_device(text=text).wait.exists(timeout=timeout)

    # Text Handling
    def get_text(self, text):
        return self.ui_device(text=text).info['text']

    def set_text(self, text, value):
        self.ui_device(text=text).set_text(value)
