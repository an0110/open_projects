import threading
import time
import os

my_path = "J:/threads/"




def writeA(text, file):
    with open (os.path.join(my_path, file.join(".txt")), "a+") as fh:
        fh.write("{} {}".format(writeA.__name__, text))
    # time.sleep(2)


def writeB(text):
    print (text)
    # time.sleep(2)


if __name__ == "__main__":
    text = "asdasdasdasd"

    while True:
        for el in text:
            x = threading.Thread(target=writeA( text,el))
            x.start()
        print("-")

        # time.sleep(1)



#
