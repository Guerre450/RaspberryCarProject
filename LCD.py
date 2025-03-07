from rpi_lcd import LCD
import time
import threading

class TextScreen(threading.Thread):
    def __init__(self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.lcd = LCD()
        self.msg2 = ""

    def run(self):
        self.kill = False
        message = []
        word = ["V","R","O","O","M"]
        word.reverse()
        queue = []
        lastInsert = None
        for i in range(0,16):
            message.append(" ")
        while not self.kill:
            if not lastInsert or time.time() > (lastInsert + 10):
                lastInsert = time.time()
                queue.extend(word)
            message.pop(0)
            message.insert(-1,queue.pop(0) if len(queue) > 0 else " ")
            # reversedMessage = message.copy()
            # reversedMessage.reverse()
            text = "".join(message[i] for i in range(len(message) - 1, 0 , -1))
            self.lcd.text(text, 1)
            self.lcd.text(self.msg2, 2)
            time.sleep(0.35)

        self.lcd.clear()
