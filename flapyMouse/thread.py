import logging
import threading
import time
from pynput.mouse import Listener
test = False
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    def on_move(x,y):
        print('Pointer moved to {0}'.format(
        (x,y)))

    def on_click(x,y,button, pressed):
        test = True
        print(test)
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x,y)))
        if not pressed:
            return False

    def on_scroll(x,y,dx,dy):
        print('Scrolled {0}'.format(
            (x,y)))
    with Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
        listener.join()
def main():
    while(True):
        test = False
        if test:
            print(test)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    print("ok")
    # x.join()
    logging.info("Main    : all done")


main()
