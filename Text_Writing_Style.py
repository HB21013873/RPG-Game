import time
import sys
import random


class TypeWriter:
    def __init__(self, delay=0.05, jitter=False):
        """
        delay: base delay between characters
        jitter: if True, adds random variation for a more 'human' feel
        """
        self.delay = delay
        self.jitter = jitter

    def _get_delay(self):
        if self.jitter:
            return random.uniform(self.delay * 0.6, self.delay * 1.4)
        return self.delay

    def write(self, text, newline=True):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(self._get_delay())
        if newline:
            print()




# use tw = TW(delay=0.02, jitter=True) in main file
