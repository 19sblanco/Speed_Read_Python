from pages.page import page
import time
import os
import json
from pynput import keyboard
import sys

class read_page(page):
    __READ_MENU = """
██████╗ ███████╗ █████╗ ██████╗ ██╗         
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║         ↑ to speed up 
██████╔╝█████╗  ███████║██║  ██║██║         ↓ to slow down
██╔══██╗██╔══╝  ██╔══██║██║  ██║╚═╝         Speed: {speed:.2f} seconds
██║  ██║███████╗██║  ██║██████╔╝██╗         ESC to return to main menu
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝
"""

    def __init__(self, lines, start_idx, main_menu):
        super().__init__()
        self.__lines = lines
        self.__curr_idx = start_idx
        self.__main_menu = main_menu
        self.__lines_to_display = []
        self.__SAVE_FILE = "save.json"
        self.__speed = 5  # default speed
        self.__listener = None
        self.__running = False

        self.load_settings()
        self.start_listener()
        self.display()

    def start_listener(self):
        self.__listener = keyboard.Listener(on_press=self.change_speed)
        self.__listener.start()

    def display(self):
        self.__running = True
        while self.__running and self.__curr_idx < len(self.__lines):
            self.__lines_to_display.append(self.__lines[self.__curr_idx])
            super().clear_console()
            print(self.__READ_MENU.format(speed=self.__speed))
            for line in self.__lines_to_display[-10:]:  # Display last 10 lines
                print(line)
            time.sleep(self.__speed)
            self.__curr_idx += 1

        self.cleanup()

    def change_speed(self, key):
        if key == keyboard.Key.up:
            self.__speed = max(0.5, self.__speed / 1.1)  # Speed up (lower delay)
        elif key == keyboard.Key.down:
            self.__speed = min(10, self.__speed * 1.1)  # Slow down (higher delay)
        elif key == keyboard.Key.esc:
            self.__running = False  # Stop the display loop

    def cleanup(self):
        self.__listener.stop()
        self.save_settings()
        self.flush_input()
        self.__main_menu()

    def flush_input(self):
        """Clear the input buffer."""
        if sys.platform.startswith('win'):
            self.flush_input_windows()
        else:  # Unix-like systems (Linux, macOS)
            self.flush_input_unix()

    def flush_input_windows(self):
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()

    def flush_input_unix(self):
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

    def load_settings(self):
        if os.path.exists(self.__SAVE_FILE):
            with open(self.__SAVE_FILE, "r") as save_file:
                self.__speed = json.load(save_file)["speed"]
        else:
            self.save_settings()

    def save_settings(self):
        data = {"speed": self.__speed}
        with open(self.__SAVE_FILE, "w") as save_file:
            json.dump(data, save_file, indent=4)