import logging

class App(object):

    def __init__(self):
        logging.basicConfig(
            filename = "cvgenerator.log",
            level = logging.DEBUG,
            format = "%(asctime)s [%(levelname)s] %(module)s (%(filename)s:%(lineno)d) : %(funcName)s : %(message)s",
            datefmt = "%Y-%m-%d %H:%M:%S")

    def main(self):
        logging.debug("main")

if __name__ == "__main__":
    __app = App()
    __app.main()