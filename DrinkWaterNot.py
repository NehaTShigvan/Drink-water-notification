
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water!!!",
            message = "Stay hydrated. It is necessary to drink minimum 2.7L of water per day for females and 3.7L for males.",
            app_icon = "C:\Users\Neha Tukaram Shigvan\Desktop\PythonProject\skillLab\waterGlass",
            timeout = 5
        )
        time.sleep(8)