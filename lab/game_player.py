from time import sleep, time
import pydirectinput
import pyautogui



# Decorator for printing what has been done step by step
# ---------------------------------------------------------------------
def print_what_has_been_done(some_function):
    def wrapper(*args, **kwargs):
        result = some_function(*args, **kwargs)
        print(f"executed: '{some_function.__name__}'; "
              f"params: {', '.join([str(arg) for arg in args[1:]])}")
        return result
    return wrapper


# The Definition
# ---------------------------------------------------------------------
class GamePlayer:
    def __init__(self):
        pass

# The Mouse
# ---------------------------------------------------------------------

    @staticmethod
    def __center_mouse():
        pyautogui.moveTo(960, 540, 0.5)

    def move_mouse_additive_x_y(self, add_to_x, add_to_y):
        self.__center_mouse()
        x, y = pyautogui.position()
        pyautogui.move(x + add_to_x, y + add_to_y, 1)
        self.wait_seconds(0.1)

# The other things
# ---------------------------------------------------------------------

    @print_what_has_been_done
    def wait_seconds(self, seconds):
        sleep(seconds)

    @print_what_has_been_done
    def left_click(self):
        pydirectinput.leftClick()
        self.wait_seconds(0.2)

    @print_what_has_been_done
    def right_click(self):
        pydirectinput.rightClick()
        self.wait_seconds(0.2)

    @print_what_has_been_done
    def hold_key_for_seconds(self, key, seconds):
        pydirectinput.keyDown(key)
        self.wait_seconds(seconds)
        pydirectinput.keyUp(key)

    @print_what_has_been_done
    def press_key(self, key):
        pydirectinput.press(key)

# The Sequence
# ---------------------------------------------------------------------

class MySequence:
    def __init__(self):
        self.game = GamePlayer()

    def sequence1(self):
        self.game = GamePlayer()
        self.game.wait_seconds(3)

        self.game.move_mouse_additive_x_y(200, 200)
        self.game.wait_seconds(1)

        self.game.left_click()
        self.game.press_key('2')

        self.game.wait_seconds(2)

# The Execution
# ---------------------------------------------------------------------

play = MySequence()
play.sequence1()
